"""
A script to train FSM players against sets of the Fortran players
"""
import csv
import multiprocessing
import sys
import imp

from main import train

run_full_tournament = imp.load_source('full_tournament',
                                      '../../run_full_tournament.py')
from full_tournament import players as full_players

if __name__ == "__main__":
    cpu_count = multiprocessing.cpu_count()
    opponents = full_players
    weights = [1 for _ in opponents]
    assert len(opponents) == 257

    output_file = "training_data_original_tournament_full_players_with_axl.csv"

    train(opponents=opponents,
          weights=weights,
          filename=output_file,
          processes=cpu_count)
