This directory contains a number of different scripts to run experiments and
write the data to the `./data/` directory.

## `run_*.py`

These scripts run the various tournaments described in the manuscript.

They take 2 command line arguments. For example:

    python run_original_tournament.py 0 1000

Will run the original tournament with a seed of 0 and 1000 repetitions.

Note that 1000 repetitions in facts corresponds to a total of 5000 repetitions
as each tournament run for the specific number of turns.

The file `jobs.txt` contains all jobs run. This can be used with gnu `parallel`
to parallelise the running of the jobs:

    parallel --jobs 10 < jobs.txt

Would run 10 jobs at a time.

## `summarise_extra_strategy_tournaments.py`

This uses the original tournament and the full tournament data to find the
results of the tournaments with extra invitations.

Usage:

    python summarise_extra_strategy_tournaments.py

## `*.ipynb`

The three jupyter notebooks include the analysis code for the
creation of the figures and supplementary information.

## `environment.yml`

This contains the conda environment information specifying the
versions of the software used for all data generation and analysis.
