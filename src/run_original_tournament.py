import sys

import axelrod as axl
import axelrod_fortran as axlf

import main

players = [axlf.Player(name) for name in axlf.second_tournament_strategies]
assert len(players) == 63

turns = [63, 77, 151, 308, 156]
match_attributes={"length": float('inf')}

if __name__ == "__main__":

    seed = int(sys.argv[1])
    repetitions = int(sys.argv[2])

    for turn in turns:
        main.main(players=players,
                  repetitions=repetitions,
                  seed=seed,
                  outdir="./data/original_tournament",
                  prefix="original_{}_turns_{}_repetitions".format(
                      turn,
                      repetitions),
                  turns=turn,
                  match_attributes=match_attributes)
