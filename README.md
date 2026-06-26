# Reviving, Reproducing, and Revisiting Axelrod's Second Tournament

This repository contains the code and manuscript source files for the project
***Reviving, Reproducing, and Revisiting Axelrod's Second Tournament***.

The project reproduces Robert Axelrod’s second Iterated Prisoner’s Dilemma
tournament, originally run in the early 1980s, using the original Fortran
implementations of the submitted strategies. It uses
[**Axelrod-Python**](https://github.com/Axelrod-Python/Axelrod) and
[**TourExec**](https://github.com/Axelrod-Python/TourExec) to run the computer
tournament simulations.

A preprint of this work is available at: https://arxiv.org/abs/2510.15438.


## Requirements

* Install [TourExec](https://github.com/Axelrod-Python/TourExec) (see
  installation instructions in that repository).
* You will also need Python.


## Setting up the Environment

To install all necessary Python dependencies, we recommend creating a **conda
environment** using the provided configuration file `src/environment.yml`. From
the root of this repository run:

```bash
conda env create -f src/environment.yml
conda activate axelrod_tournament
```


## Source Code

* The code for generating and reproducing the original tournaments is located in
  the `src/` directory.
* It includes:

  * **Tournament execution scripts** to reproduce Axelrod’s results.
  * **Analysis scripts and Jupyter notebooks** for generating all figures used
    in the manuscript.

To rerun the original tournaments, refer to the
[documentation](https://github.com/Axelrod-Python/revisiting-axelrod-second/tree/main/src)
in `src/`.


## Data

Running the simulations will generate the tournament data.

If you prefer **not to rerun** the entire simulation, you can download the
archived data from Zenodo:

1. Download the dataset archive from https://doi.org/10.5281/zenodo.20811704.
2. Unzip it into the `data/` folder.

This will allow you to reproduce the analysis and figures directly.


## Analysis and Figures

All data analysis and manuscript figures were generated using **Python** and
**Jupyter notebooks**, available under `src/`.

If you have downloaded the archived data, you can simply open and run the
notebooks to reproduce all figures without rerunning the full simulations.