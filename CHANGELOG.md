# Changelog

## [0.1.0](https://github.com/jjjermiah/snakemake-storage-plugin-gcs/compare/v1.0.0...v0.1.0) (2024-04-26)


### ⚠ BREAKING CHANGES

* expect correct google cloud storage abbreviation in query scheme (gcs://) ([#39](https://github.com/jjjermiah/snakemake-storage-plugin-gcs/issues/39))

### Features

* add logging capabilities for future WMS work ([f51f586](https://github.com/jjjermiah/snakemake-storage-plugin-gcs/commit/f51f58685ba2f1ad7e8c88d3d2237aeae50a87f1))


### Bug Fixes

* directory() issue arising from uploading into the wrong gcs path. ([a21a4f5](https://github.com/jjjermiah/snakemake-storage-plugin-gcs/commit/a21a4f57f3c1acd8c14c5e4388c77038f6fd9c09))
* expect correct google cloud storage abbreviation in query scheme (gcs://) ([#39](https://github.com/jjjermiah/snakemake-storage-plugin-gcs/issues/39)) ([0ebf52c](https://github.com/jjjermiah/snakemake-storage-plugin-gcs/commit/0ebf52cc6131fe092f638306f104e4c37a88aac4))
* fix directory support ([#38](https://github.com/jjjermiah/snakemake-storage-plugin-gcs/issues/38)) ([ce3d165](https://github.com/jjjermiah/snakemake-storage-plugin-gcs/commit/ce3d165f94e2d9d8f9469434d88edc0fe1b7f2a1))
* refactor remove method for directories ([3300cf4](https://github.com/jjjermiah/snakemake-storage-plugin-gcs/commit/3300cf4a1c3fbfef77d765efe5a44d6f62c829ca))
* relax towards older crc32c ([#7](https://github.com/jjjermiah/snakemake-storage-plugin-gcs/issues/7)) ([b99dfa0](https://github.com/jjjermiah/snakemake-storage-plugin-gcs/commit/b99dfa07cc4b9bebbc2126d8f725bcd544c91dcf))
* repair GCS query string ([#26](https://github.com/jjjermiah/snakemake-storage-plugin-gcs/issues/26)) ([f61e8d0](https://github.com/jjjermiah/snakemake-storage-plugin-gcs/commit/f61e8d0e3b83d3b03ad2eb41ceb0c5902345ef48))


### Documentation

* add intro, fix link ([6ec568a](https://github.com/jjjermiah/snakemake-storage-plugin-gcs/commit/6ec568a092aa6b636549a48fc09f0f1ba07b6f00))
* update metadata ([cceaad1](https://github.com/jjjermiah/snakemake-storage-plugin-gcs/commit/cceaad1c9795cc95c4d420b2ee2ebe0c7fdd5b0d))
* update readme ([7d23319](https://github.com/jjjermiah/snakemake-storage-plugin-gcs/commit/7d233198eb911f7fb3f73176f2304681272dd080))


### Miscellaneous Chores

* release 0.1.0 ([6709181](https://github.com/jjjermiah/snakemake-storage-plugin-gcs/commit/67091814a0b44107809162b6eb6d9178745d8afa))

## [1.0.0](https://github.com/snakemake/snakemake-storage-plugin-gcs/compare/v0.1.4...v1.0.0) (2024-04-26)


### ⚠ BREAKING CHANGES

* expect correct google cloud storage abbreviation in query scheme (gcs://) ([#39](https://github.com/snakemake/snakemake-storage-plugin-gcs/issues/39))

### Bug Fixes

* expect correct google cloud storage abbreviation in query scheme (gcs://) ([#39](https://github.com/snakemake/snakemake-storage-plugin-gcs/issues/39)) ([0ebf52c](https://github.com/snakemake/snakemake-storage-plugin-gcs/commit/0ebf52cc6131fe092f638306f104e4c37a88aac4))
* fix directory support ([#38](https://github.com/snakemake/snakemake-storage-plugin-gcs/issues/38)) ([ce3d165](https://github.com/snakemake/snakemake-storage-plugin-gcs/commit/ce3d165f94e2d9d8f9469434d88edc0fe1b7f2a1))


### Documentation

* add intro, fix link ([6ec568a](https://github.com/snakemake/snakemake-storage-plugin-gcs/commit/6ec568a092aa6b636549a48fc09f0f1ba07b6f00))

## [0.1.4](https://github.com/snakemake/snakemake-storage-plugin-gcs/compare/v0.1.3...v0.1.4) (2024-03-08)


### Bug Fixes

* repair GCS query string ([#26](https://github.com/snakemake/snakemake-storage-plugin-gcs/issues/26)) ([f61e8d0](https://github.com/snakemake/snakemake-storage-plugin-gcs/commit/f61e8d0e3b83d3b03ad2eb41ceb0c5902345ef48))

## [0.1.3](https://github.com/snakemake/snakemake-storage-plugin-gcs/compare/v0.1.2...v0.1.3) (2023-12-20)


### Documentation

* update readme ([7d23319](https://github.com/snakemake/snakemake-storage-plugin-gcs/commit/7d233198eb911f7fb3f73176f2304681272dd080))

## [0.1.2](https://github.com/snakemake/snakemake-storage-plugin-gcs/compare/v0.1.1...v0.1.2) (2023-12-20)


### Bug Fixes

* relax towards older crc32c ([#7](https://github.com/snakemake/snakemake-storage-plugin-gcs/issues/7)) ([b99dfa0](https://github.com/snakemake/snakemake-storage-plugin-gcs/commit/b99dfa07cc4b9bebbc2126d8f725bcd544c91dcf))

## [0.1.1](https://github.com/snakemake/snakemake-storage-plugin-gcs/compare/v0.1.0...v0.1.1) (2023-12-08)


### Documentation

* update metadata ([cceaad1](https://github.com/snakemake/snakemake-storage-plugin-gcs/commit/cceaad1c9795cc95c4d420b2ee2ebe0c7fdd5b0d))

## 0.1.0 (2023-12-07)


### Miscellaneous Chores

* release 0.1.0 ([6709181](https://github.com/snakemake/snakemake-storage-plugin-gcs/commit/67091814a0b44107809162b6eb6d9178745d8afa))
