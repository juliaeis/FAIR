# FaIRv2.0.0
This repo contains model code and supporting notebooks to accompany the paper describing version 2.0.0 of the FaIR simple climate model (https://gmd.copernicus.org/preprints/gmd-2020-390/). The repo structure is outlined below.

## Code
| path/to/file.py  | description |
| ------------- | ------------- |
| fair/fair_runner.py  | All functions required to run FaIRv2.0.0-alpha, the development version of FaIRv2.0.0  |
| fair/scripts/data_retrieval.py  | Functions that retrieve RCMIP protocol datasets, and transform them into FaIRv2.0.0-alpha compatible inputs.  |
| fair/scripts/EBM_to_FaIR.py  | Functions that convert Energy Balance Model parameters into FaIRv2.0.0-alpha climate response parameters  |
| fair/scripts/FaIR_tuning_scripts.py  | A function that is used to tune the gas cycles by inverting a concentration timeseries to emissions under a prescribed temperature series.  |
| fair/scripts/stats.py  | A function for calculating ordinary least squares estimators rapidly.  |

# Zenodo DOI
TODO<!-- [![DOI](https://zenodo.org/badge/231077183.svg)](https://zenodo.org/badge/latestdoi/231077183) -->

# License
[CC4.0](https://creativecommons.org/licenses/by/4.0/)
