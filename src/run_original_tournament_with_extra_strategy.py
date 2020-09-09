import sys

import axelrod as axl
import axelrod_fortran as axlf

import main

fortran_players = [axlf.Player(name)
                   for name in axlf.second_tournament_strategies]
assert len(fortran_players) == 63

turns = [63, 77, 151, 308, 156]
match_attributes={"length": float('inf')}

if __name__ == "__main__":

    seed = int(sys.argv[1])
    repetitions = int(sys.argv[2])
    extra_player_index = int(sys.argv[3])

    for turn in turns:

        extra_player = axl.strategies[extra_player_index]()
        players = fortran_players + [extra_player]

        main.main(players=players,
                  repetitions=repetitions,
                  seed=seed,
                  outdir="./data/original_tournament_with_extra_strategy",
                  prefix="original_{}_turns_{}_repetitions_with_axl_player_{}-{}".format(
                      turn,
                      repetitions,
                      extra_player_index,
                      extra_player.name,
                      ),
                  turns=turn,
                  match_attributes=match_attributes)
