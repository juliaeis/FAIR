# FaIRv2.0.0
This repo contains model code and supporting notebooks to accompany the paper describing version 2.0.0 of the FaIR simple climate model (https://gmd.copernicus.org/preprints/gmd-2020-390/). The repo structure is outlined below.

## Code

| /path/to/file.py  | description |
| ------------- | ------------- |
| /FaIRv2_0_0_alpha.py  | All functions required to run FaIRv2.0.0-alpha, the development version of FaIRv2.0.0  |
| /scripts/data_retrieval.py  | Functions that retrieve RCMIP protocol datasets, and transform them into FaIRv2.0.0-alpha compatible inputs.  |
| /scripts/EBM_to_FaIR.py  | Functions that convert Energy Balance Model parameters into FaIRv2.0.0-alpha climate response parameters  |
| /scripts/FaIR_tuning_scripts.py  | A function that is used to tune the gas cycles by inverting a concentration timeseries to emissions under a prescribed temperature series.  |
| /scripts/stats.py  | A function for calculating ordinary least squares estimators rapidly.  |

## Notebooks
These notebooks are listed in the approximate order they should be run in to generate all the data files and parameter sets required to fully carry out all the analyses within the paper. Figures and tables as they appear in the paper are listed after each description.

| /path/to/notebook.ipynb  | description |
| ------------- | ------------- |
| /notebooks/example-nb.ipynb  | Demonstration of FaIRv2.0.0-alpha I/O formats, plus some examples of how to run experiments.  |
| /notebooks/parameter-tuning/CMIP6-aerosol.ipynb  | Tuning FaIRv2.0.0 parameters to CMIP6 aerosol forcing from RFMIP. *Fig5, Tab4*  |
| /notebooks/parameter-tuning/CMIP6-cc.ipynb  | Tuning FaIRv2.0.0 parameters to CMIP6 ESMs from C4MIP. *Fig4, Tab3*  |
| /notebooks/parameter-tuning/CMIP6-climresp_Cummins.ipynb  | Tuning FaIRv2.0.0 parameters to CMIP6 climate respose using [Cummins et al., 2020 MLE methodology](http://journals.ametsoc.org/doi/10.1175/JCLI-D-19-0589.1). R language notebook.  |
| /notebooks/parameter-tuning/CMIP6-climresp-results.ipynb  | Examining tuned climate response parameters from `CMIP6-climresp_Cummins`. *Fig3, Tab2, TabS5*  |
| /notebooks/parameter-tuning/default-parameters.ipynb  | Tunes or sets the default model parameter set.  |
| /notebooks/parameter-tuning/default-experiment-metrics.ipynb  | Carries out a suite of experiments for the default parameter set, and computes associated metrics. *Fig2, FigS2, FigS3, TabS2, TabS3* |
| /notebooks/perturbed-parameter-ensemble/FULL-compute.ipynb  | Creates a large parameter ensemble (FULL) & generates key metrics for each member over the SSPs.  |
| /notebooks/perturbed-parameter-ensemble/global-warming-index.ipynb  | Generate an estimate of the present-day Global Warming Index, and associated FULL ensemble selection probabilities. |
| /notebooks/perturbed-parameter-ensemble/FULL-constrain.ipynb  | Constrains the FULL ensemble using the GWI-based selection probabilities, and explores the implications. *Fig6, Fig7, Tab7, Tab8, Tab9, Tab10, TabS6* |
| /notebooks/perturbed-parameter-ensemble/DECK-simulations.ipynb  | Carries out some basic CMIP6 experiments (abrupt-4xCO2 & 1pctCO2) for the FULL and CONSTRAINED ensembles. *Fig8* |
| /notebooks/perturbed-parameter-ensemble/SSP-simulations.ipynb  | Carries out simulations of the SSPs for the CONSTRAINED ensemble. *Fig9, Fig10, TabS4* |
| /notebooks/RCMIP/RCMIP-experiments.ipynb  | Carries out simulations submitted to [RCMIP phase II](http://www.essoar.org/doi/10.1002/essoar.10504793.1). |

## Auxiliary data files
There are also a number of auxiliary data files and directories within this repo. Some are excluded from the repo due to limitations on file sizes, but all are described below.

| /path/to/file/or/directory  | description |
| ------------- | ------------- |
| /aux/FaIRv2.0.0-alpha_RCMIP_forcmap.csv  | Maps between RCMIP forcing categories (pyam convention) & FaIRv2.0.0-alpha categories (AR5 convention).  |
| /aux/FaIRv2.0.0-alpha_RCMIP_inputmap.csv  | Maps between RCMIP input variables (emissions + concentrations) & FaIRv2.0.0-alpha inputs. |
| /aux/FaIRv2.0.0-alpha_RF_categories.csv  | Maps each FaIRv2.0.0-alpha output forcing (default parameters) to an aggregated forcing category. |
| /aux/parameter-sets/CMIP6_cc_full.csv  | Carbon cycle parameters tuned to C4MIP models with $r_a$ included in the fit. |
| /aux/parameter-sets/CMIP6_cc_reduced.csv  | Carbon cycle parameters tuned to C4MIP models with $r_a$ not included in the fit. |
| /aux/parameter-sets/CMIP6_climresp.csv  | Climate response parameters tuned to CMIP6 models. |
| /aux/parameter-sets/CMIP6_ERFaci.csv  | Aerosol-cloud interaction parameters tuned to RFMIP. |
| /aux/parameter-sets/CMIP6_ERFari.csv  | Aerosol-radiation interaction parameters tuned to RFMIP. |
| /aux/parameter-sets/CMIP6_f_params.csv  | CO2 forcing parameters tuned to CMIP6 models. |
| /aux/parameter-sets/Complete_gas_cycle_params.csv  | Full default gas cycle and forcing parameter set. |
| /aux/parameter-sets/CMIP6-climresp_Cummins/  | Tuned EBM parameters to CMIP6 models following Cummins et al., 2020. |
| /aux/parameter-sets/perturbed-parameters/climresp_params/  | FULL ensemble of climate response parameters in batches of 10,000 members. |
| /aux/parameter-sets/perturbed-parameters/extforc_sfs/  | FULL ensemble of external forcing scaling factors in batches of 10,000 members. |
| /aux/parameter-sets/perturbed-parameters/gas_params/  | FULL ensemble of gas cycle & forcing parameters in batches of 10,000 members. |
| /aux/parameter-sets/perturbed-parameters/gas_params/{FULL,ALT}\_{ALL,ANT}.h5  | Key output metrics for FULL (ALTERNATIVE) ensemble under all-forcing (anthropogenic-only) SSP2-45 simulation. |
| /aux/parameter-sets/perturbed-parameters/gas_params/ssp*.h5  | Key output metrics for FULL ensemble under all-forcing SSP simulations. |
| /aux/parameter-sets/perturbed-parameters/gas_params/{FULL,ALT}\_selection\_probability*.h5  | FULL (ALTERNATIVE) ensemble member selection probabilities based on anthropogenic-warming-index level/rate likelihood from various observational data products. |
| ------------- | ------------- |
| /aux/output-data/global-warming-index/  | Outputs from the `global-warming-index` notebook. |
| /aux/output-data/RCMIP/  | Model output submitted to [RCMIP phase II](http://www.essoar.org/doi/10.1002/essoar.10504793.1). |
| ------------- | ------------- |
| /aux/input-data/Temperature-observations/  | Global temperature data products used in `global-warming-index` notebook. Raw data as downloaded from corresponding sources. |
| /aux/input-data/RCMIP/  | MAGICC7.1.0-beta and FaIRv1.5 data from [RCMIP phase I](https://doi.org/10.5194/gmd-13-5175-2020) used in several figures.  |
| /aux/input-data/CMIP6/  | CMIP6 data used throughout the paper. Downloaded from https://cmip6.science.unimelb.edu.au/. See [Nicholls et al., 2021](https://onlinelibrary.wiley.com/doi/10.1002/gdj3.113).  |

# Zenodo DOI
TODO<!-- [![DOI](https://zenodo.org/badge/231077183.svg)](https://zenodo.org/badge/latestdoi/231077183) -->

# License
[CC4.0](https://creativecommons.org/licenses/by/4.0/)