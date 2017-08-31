"""
A script to train FSM players against sets of the Fortran players
"""
import csv
import multiprocessing
import sys

from main import train

if __name__ == "__main__":
    cpu_count = multiprocessing.cpu_count()
    opponents = [axlf.Player(name)
                 for name in axlf.second_tournament_strategies]
    weights = [1 for _ in opponents]
    assert len(opponents) == 63

    output_file = "training_data_original_tournament_full_players.csv"

    train(opponents=opponents,
          weights=weights,
          filename=output_file,
          processes=cpu_count)
