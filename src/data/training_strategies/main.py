"""
A script to train FSM players against sets of the Fortran players
"""
import csv
import multiprocessing
import sys
import pathlib

import axelrod as axl
import axelrod_dojo as dojo
import axelrod_fortran as axlf

assert axl.__version__ == "3.3.0"
assert axlf.__version__ == "0.3.1"
assert dojo.__version__ == "0.0.5"

def train(opponents, weights, filename, processes,
          turns=200, repetitions=100, mutation_rate=0.1, size=16,
          num_states=10, name="score",
          match_attributes={"length": float("inf")}):

    # Code to read in any pre training and adjust output file
    current_dir = pathlib.Path(".")

    try:
        initial_params = dojo.load_params(dojo.FSMParams,
                                          filename,
                                          num=16)
        initial_population = initial_params

        for params in initial_params:
            params.mutation_rate = 0.1

    except AttributeError:
        initial_population = None

    objective = dojo.prepare_objective(name=name,
                                       turns=turns,
                                       match_attributes=match_attributes,
                                       repetitions=repetitions)

    population = dojo.Population(params_class=dojo.FSMParams,
                                 params_args=(num_states,
                                              mutation_rate),
                                 size=size,
                                 objective=objective,
                                 output_filename=filename,
                                 opponents=opponents,
                                 weights=weights,
                                 bottleneck=5,
                                 processes=processes,
                                 population=initial_population)

    generations = 10 ** 7
    axl.seed(0)
    population.run(generations)

if __name__ == "__main__":
    input_file = sys.argv[1]
    cpu_count = multiprocessing.cpu_count()

    opponents, weights = [], []
    with open(input_file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            player_name, weight = row
            opponents.append(axlf.Player(player_name))
            weights.append(float(weight))

    output_file = "training_data_" + input_file
    train(opponents=opponents,
          weights=weights,
          filename=output_file,
          processes=cpu_count)
