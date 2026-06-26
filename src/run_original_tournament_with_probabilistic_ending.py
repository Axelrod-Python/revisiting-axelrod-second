import sys

import axelrod_fortran as axlf

import main

players = [axlf.Player(name) for name in axlf.second_tournament_strategies]
assert len(players) == 63

match_attributes = {"length": float("inf")}
prob_end = 1 / 151

if __name__ == "__main__":

    seed = int(sys.argv[1])
    repetitions = int(sys.argv[2])

    main.main(
        players=players,
        repetitions=repetitions,
        seed=seed,
        outdir="./data/original_tournament_with_probabilistic_end",
        prefix="original_{}_prob_end_{}_repetitions".format(prob_end, repetitions),
        prob_end=prob_end,
        match_attributes=match_attributes,
    )
