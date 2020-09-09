import sys

import axelrod as axl
import axelrod_fortran as axlf

import main

strategies = axlf.second_tournament_strategies
strategies[strategies.index("k74r")] = "k74rxx"

players = [axlf.Player(name) for name in strategies]
assert len(players) == 63

turns = [63, 77, 151, 308, 156]
match_attributes={"length": float('inf')}

if __name__ == "__main__":

    seed = int(sys.argv[1])
    repetitions = int(sys.argv[2])
    processes = int(sys.argv[3])

    for turn in turns:
        main.main(players=players,
                  repetitions=repetitions,
                  seed=seed,
                  processes=processes,
                  outdir="./data/original_with_alt_k74r_tournament",
                  prefix="original_with_alt_k74r_{}_turns_{}_repetitions".format(
                      turn,
                      repetitions),
                  turns=turn,
                  match_attributes=match_attributes)
