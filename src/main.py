import axelrod as axl
import axelrod_fortran as axlf
import numpy as np
import os.path
import json

assert axl.__version__ == "4.10.0"
assert axlf.__version__ == "0.4.8"

def main(players,
         repetitions=1000,
         outdir="data/",
         prefix=None,
         seed=0,
         **tournament_kwargs):
    """
    A function to run a tournament.

    To ensure self interactions are recorded correctly, this is done using a
    spatial tournament and using a copied version of the shared library.

    This output data to be analysed at a later date which allows for large
    number of repetitions to be computed independently.

    Parameters
    ----------
        players: the list of players to be used (combination of axelrod and
                 axelrod_fortran players)
        repetitions: the repetitions
        outdir: where the output data will be written
        prefix: what the output data will be called
        seed: the random seed to use
        tournament_kwargs, a dictionary:
            - turns
            - prob_end
            - match_attributes

    """
    player_index_file = f"{outdir}/players.index"
    print(f"Writing tournament index file to {player_index_file}")
    with open(player_index_file, 'w') as f:
        for i, player in enumerate(players):
            f.write(f"{i}, {str(player)}\n")

    fortran_characteristics_dictionary_file = f"{outdir}/fortran_characteristics.json"}
    print(f"Writing characteristics file to {fortran_characteristics_dictionary_file}")
    with open(fortran_characteristics_dictionary_file, "w") as f:
        json.dump(axlf.characteristics, f)

    print(f"Running tournament with seed={seed} and {len(players)} players and with tournament_kwargs={tournament_kwargs}")
    tournament = axl.Tournament(players,
                                repetitions=repetitions,
                                seed=seed,
                                **tournament_kwargs)
    interaction_filename = "{}/{}_{}_interactions.csv".format(outdir,
                                                              prefix,
                                                              seed)
    summary_filename = "{}/{}_{}_seed_summary.csv".format(outdir,
                                                         prefix,
                                                         seed)
    if not os.path.isfile(summary_filename):
        results = tournament.play(filename=interaction_filename,
                                  progress_bar=False)


        scores_per_tournament = np.array(results.scores).transpose()
        np.savetxt(fname="{}/{}_{}_seed_scores.gz".format(outdir, prefix, seed),
                   X=scores_per_tournament, delimiter=",")

        wins_per_tournament = np.array(results.wins).transpose()
        np.savetxt(fname="{}/{}_{}_seed_wins.gz".format(outdir, prefix, seed),
                   X=wins_per_tournament, delimiter=",")

        match_lengths_per_tournament = np.mean(results.match_lengths, axis=2)
        np.savetxt(fname="{}/{}_{}_seed_match_lengths_per_tournament.gz".format(outdir, prefix, seed),
                   X=match_lengths_per_tournament, delimiter=",")

        cooperation_rates = np.array(results.normalised_cooperation).transpose()
        np.savetxt(fname="{}/{}_{}_seed_cooperation_rates.gz".format(outdir, prefix, seed),
                   X=cooperation_rates, delimiter=",")

        payoff_matrix = np.array(results.payoff_matrix)
        np.savetxt(fname="{}/{}_{}_seed_payoff_matrix.gz".format(outdir, prefix, seed),
                   X=payoff_matrix, delimiter=",")
        results.write_summary(summary_filename)
    print("Tournament complete")
