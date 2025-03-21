import base64
import os
from pathlib import Path
from typing import Any

from google.api_core import retry
from google.cloud import storage
from google_crc32c import Checksum
from snakemake.exceptions import CheckSumMismatchException


class Crc32cCalculator:
    """
    A wrapper to write a file and calculate a crc32 checksum.

    The Google Python client doesn't provide a way to stream a file being
    written, so we can wrap the file object in an additional class to
    do custom handling. This is so we don't need to download the file
    and then stream-read it again to calculate the hash.
    """

    def __init__(self, fileobj: Any) -> None:
        self._fileobj = fileobj
        self.checksum = Checksum()

    def write(self, chunk: bytes) -> None:
        self._fileobj.write(chunk)
        self._update(chunk)

    def _update(self, chunk: bytes) -> None:
        """
        Given a chunk from the read in file, update the hexdigest
        """
        self.checksum.update(chunk)

    def hexdigest(self) -> str:
        """
        Return the hexdigest of the hasher.

        The Base64 encoded CRC32c is in big-endian byte order.
        See https://cloud.google.com/storage/docs/hashes-etags
        """
        return base64.b64encode(self.checksum.digest()).decode("utf-8")


def google_cloud_retry_predicate(ex: Exception) -> bool:
    """
    Google cloud retry with specific Google Cloud errors.

    Given an exception from Google Cloud, determine if it's one in the
    listing of transient errors (determined by function
    google.api_core.retry.if_transient_error(exception)) or determine if
    triggered by a hash mismatch due to a bad download. This function will
    return a boolean to indicate if retry should be done, and is typically
    used with the google.api_core.retry.Retry as a decorator (predicate).

    Arguments:
      ex (Exception) : the exception passed from the decorated function
    Returns: boolean to indicate doing retry (True) or not (False)
    """
    from requests.exceptions import ReadTimeout

    # Most likely case is Google API transient error.
    if retry.if_transient_error(ex):
        return True
    # Timeouts should be considered for retry as well.
    if isinstance(ex, ReadTimeout):
        return True
    # Could also be checksum mismatch of download.
    if isinstance(ex, CheckSumMismatchException):
        return True
    return False


@retry.Retry(predicate=google_cloud_retry_predicate)
def download_blob(blob: storage.Blob, filename: Path) -> Path:
    """
    Download and validate storage Blob to a blob_fil.

    Arguments:
      blob (storage.Blob) : the Google storage blob object
      blob_file (str)     : the file path to download to
    Returns: boolean to indicate doing retry (True) or not (False)
    """

    # create parent directories if necessary
    filename.parent.mkdir(parents=True, exist_ok=True)

    # ideally we could calculate hash while streaming to file with provided function
    # https://github.com/googleapis/python-storage/issues/29
    with open(filename, "wb") as blob_file:
        parser = Crc32cCalculator(blob_file)
        blob.download_to_file(parser)
    os.sync()

    # **Important** hash can be incorrect or missing if not refreshed
    blob.reload()

    # Compute local hash and verify correct
    if parser.hexdigest() != blob.crc32c:
        os.remove(filename)
        raise CheckSumMismatchException("The checksum of %s does not match." % filename)
    return filename
