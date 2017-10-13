import sys

import axelrod as axl
import axelrod_fortran as axlf

import main
assert axl.__version__ == "3.8.1"
assert axlf.__version__ == "0.3.2"

players = [axlf.Player(name) for name in axlf.second_tournament_strategies]
implemented_strategies = [axlf.characteristics[name]['axelrod-python_class']
                          for name in axlf.second_tournament_strategies]
players += [s() for s in axl.strategies
            if s not in implemented_strategies and
            s not in [axl.Alexei, axl.ContriteTitForTat]]  # Correspond to TfT

assert len(players) == 257

turns = [63, 77, 151, 308, 157]
match_attributes={"length": float('inf')}

if __name__ == "__main__":

    seed = int(sys.argv[1])
    repetitions = int(sys.argv[2])

    for turn in turns:
        main.main(players=players,
                  repetitions=repetitions,
                  seed=seed,
                  outdir="./data/full_tournament",
                  prefix="full_{}_turns_{}_repetitions".format(
                      turn,
                      repetitions),
                  turns=turn,
                  match_attributes=match_attributes)
