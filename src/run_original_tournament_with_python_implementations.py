import sys

import axelrod as axl
import axelrod_fortran as axlf

import main
assert axl.__version__ == "3.8.1"
assert axlf.__version__ == "0.4.0"

players = []
for name in axlf.second_tournament_strategies:
    characteristics = axlf.characteristics[name]
    axelrod_class = characteristics["axelrod-python_class"]
    if axelrod_class is not None:
        players.append(axelrod_class())
    else:
        players.append(axlf.Player(name))

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
                  outdir="./data/original_tournament_with_python_implementations",
                  prefix="original_with_py_implementations_{}_turns_{}_repetitions".format(
                      turn,
                      repetitions),
                  turns=turn,
                  match_attributes=match_attributes)
