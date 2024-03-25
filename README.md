# pypsa-nz

Investigating New Zealands energy system with PyPSA

This repository contains the entire scientific project, including code and report. The philosophy behind this repository is that no intermediary results are included, but all results are computed from raw data and code.

## Getting ready

You need [mamba](https://mamba.readthedocs.io/en/latest/) to run the analysis. Using mamba, you can create an environment from within you can run it:

    mamba env create -f environment.yaml

## Run the analysis

    snakemake -call

This will run all analysis steps to reproduce results and eventually build the report.

To generate a PDF of the dependency graph of all steps `build/dag.pdf` run:

    snakemake -c1 --use-conda -f dag

## Repo structure

* `config`: configurations used in the study
* `data`: place for raw data
* `report`: contains all files necessary to build the report; plots and result files are generated automatically
* `workflow`: contains the Snakemake workflow
* `build`: will contain all results (does not exist initially)

## License

The code in this repo is MIT licensed, see `./LICENSE.md`.
