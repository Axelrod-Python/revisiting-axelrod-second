import sys

import axelrod as axl
import axelrod_fortran as axlf

import main
assert axl.__version__ == "3.3.0"
assert axlf.__version__ == "0.3.1"

players = [axlf.Player(name) for name in axlf.second_tournament_strategies]
implemented_strategies = [axlf.characteristics[name]['axelrod-python_class']
                          for name in axlf.second_tournament_strategies]
stewart_and_plotkin_players = [axl.Cooperator(),
                               axl.Defector(),
                               axl.ZDExtort2(),
                               axl.HardGoByMajority(),
                               axl.Joss(),
                               axl.HardTitForTat(),
                               axl.HardTitFor2Tats(),
                               axl.TitForTat(),
                               axl.Grudger(),
                               axl.GTFT(),
                               axl.TitFor2Tats(),
                               axl.WinStayLoseShift(),
                               axl.Random(),
                               axl.ZDGTFT2()]
stewart_and_plotkin_players = [p for p in stewart_and_plotkin_players if
                               type(p) not in implemented_strategies]
players += stewart_and_plotkin_players

assert len(players) == 74

turns = [63, 77, 151, 308, 157]
match_attributes={"length": float('inf')}

if __name__ == "__main__":

    seed = int(sys.argv[1])
    repetitions = int(sys.argv[2])

    for turn in turns:
        main.main(players=players,
                  repetitions=repetitions,
                  seed=seed,
                  outdir="./data/sp_tournament",
                  prefix="pd_{}_turns_{}_repetitions".format(
                      turn,
                      repetitions),
                  turns=turn,
                  match_attributes=match_attributes)
