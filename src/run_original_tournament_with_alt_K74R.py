import sys

import axelrod as axl
import axelrod_fortran as axlf

import main
assert axl.__version__ == "3.3.0"
assert axlf.__version__ == "0.2.0"

strategies = axlf.second_tournament_strategies
strategies[strategies.index("k74r")] = "k74rxx"

players = [axlf.Player(name) for name in strategies]
assert len(players) == 63

turns = [63, 77, 151, 308, 157]
match_attributes={"length": float('inf')}

if __name__ == "__main__":

    seed = int(sys.argv[1])
    repetitions = int(sys.argv[2])

    for turn in turns:
        main.main(players=players,
                  repetitions=repetitions,
                  seed=seed,
                  outdir="./data/original_with_alt_k74r_tournament",
                  prefix="original_with_alt_k74r_{}_turns_{}_repetitions".format(
                      turn,
                      repetitions),
                  turns=turn,
                  match_attributes=match_attributes)
