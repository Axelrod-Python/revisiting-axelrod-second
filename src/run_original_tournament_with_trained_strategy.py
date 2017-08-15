import sys
import pathlib

import pandas as pd

import axelrod_fortran as axlf
import axelrod_dojo as dojo

import main
assert pd.__version__ == '0.20.3'
assert dojo.__version__ == "0.0.4"
assert axlf.__version__ == "0.3.1"

fortran_players = [axlf.Player(name)
                   for name in axlf.second_tournament_strategies]
assert len(fortran_players) == 63

turns = [63, 77, 151, 308, 157]
match_attributes={"length": float('inf')}

if __name__ == "__main__":

    seed = int(sys.argv[1])
    repetitions = int(sys.argv[2])
    extra_player_training_data_file = sys.argv[3]
    path = pathlib.Path(extra_player_training_data_file)
    filename = path.stem

    df = pd.read_csv(extra_player_training_data_file,
                     header=None,
                     names=["index", "Mean", "Std", "Max", "Best"],
                     index_col="index")
    best_player_repr = df.groupby("Best")["Max"].max().argmax()

    for turn in turns:

        extra_player = dojo.FSMParams.parse_repr(best_player_repr).player()
        players = fortran_players + [extra_player]

        main.main(players=players,
                  repetitions=repetitions,
                  seed=seed,
                  outdir="./data/training_strategies",
                  prefix="original_{}_turns_{}_repetitions_with_{}".format(
                      turn,
                      repetitions,
                      filename,
                      ),
                  turns=turn,
                  match_attributes=match_attributes)
