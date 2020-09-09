import sys

import axelrod_fortran as axlf

import main

players = []
python_players = []
for name in axlf.second_tournament_strategies:
    characteristics = axlf.characteristics[name]
    axelrod_class = characteristics["axelrod-python_class"]
    if axelrod_class is not None:
        python_players.append(axelrod_class())
    else:
        players.append(axlf.Player(name))

players = players + python_players

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
                  outdir="./data/original_tournament_with_python_implementations",
                  prefix="original_with_py_implementations_{}_turns_{}_repetitions".format(
                      turn,
                      repetitions),
                  turns=turn,
                  match_attributes=match_attributes)
