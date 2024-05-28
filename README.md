# pypsa-nz

![Size](https://img.shields.io/github/repo-size/energyLS/pypsa-nz)

PyPSA-NZ is an open-source energy system model in high spatial and temporal resolution, based on 
[PyPSA-Earth](https://github.com/pypsa-meets-earth/pypsa-earth) and [PyPSA-Earth-Sec](https://github.com/pypsa-meets-earth/pypsa-earth-sec).
This repository contains analysis of solved model runs from PyPSA-Earth-Sec in the context of New Zealand, as well as data preparation, validation, etc.

It is currently under development.

## Clone the repository

```bash
    git clone https://github.com/energyLS/pypsa-nz.git
```



## Repo structure

* `config`: configurations used in the study
* `data`: place for raw data
* `report`: contains all files necessary to build the report; plots and result files are generated automatically
* `workflow`: contains the Snakemake workflow

## License

The code in this repo is MIT licensed, see `./LICENSE.md`.

## Brownfield capacities
The brownfield capacities are a result of the PyPSA-Earth workflow and the visualization is based on 
the [transmission system visualisation](https://github.com/pypsa-meets-earth/documentation/blob/main/notebooks/viz/regional_transm_system_viz.ipynb).


![Brownfield capacities](readme/brownfield_capacities_.png?raw=true "Brownfield capacities")
