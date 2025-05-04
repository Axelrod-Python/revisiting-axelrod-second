This directory contains a number of different scripts to run experiments and
write the data to the `./data/` directory.

They take 2 command line arguments. For example:

    python run_original_tournament.py 0 1000

Will run the original tournament with a seed of 0 and 1000 repetitions.

Note that 1000 repetitions in facts corresponds to a total of 5000 repetitions
as each tournament run for the specific number of turns.

The file `jobs.txt` contains all jobs run. This can be used with gnu `parallel`
to parallelise the running of the jobs:

    parallel --jobs 10 < jobs.txt

Would run 10 jobs at a time.
