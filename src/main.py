import axelrod as axl
import axelrod_fortran as axlf
import numpy as np

assert axl.__version__ == "3.8.1"
assert np.__version__ == "1.13.1"

copy_of_shared_library = "libstrategies_copy.so"

def main(players,
         repetitions=1000,
         outdir="data/",
         prefix=None,
         seed=0,
         processes=0,
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
        processes: the number of cores
        tournament_kwargs, a dictionary:
            - turns
            - prob_end
            - match_attributes

    """
    fortran_players = [player for player in players
                       if type(player) is axlf.Player]
    player_copies = []
    for player in fortran_players:
        original_name = player.original_name
        player_copies.append(axlf.Player(
            original_name,
            shared_library_name=copy_of_shared_library))

    number_of_players = len(players)
    # Normal interactions
    edges = [(i, j) for i in range(number_of_players)
             for j in range(number_of_players) if i < j]
    # Self interactions
    edges += [(i, i) for i, player in enumerate(players)
              if player not in fortran_players]
    # Self interactions for fortran players
    edges += [(i, i + number_of_players)
              for i, player in enumerate(players)
              if player in fortran_players]

    axl.seed(seed)
    tournament = axl.Tournament(players + player_copies,
                                edges=edges, repetitions=repetitions,
                                **tournament_kwargs)
    interaction_filename = "{}/{}_{}_interactions.csv".format(outdir,
                                                              prefix,
                                                              seed)
    results = tournament.play(filename=interaction_filename,
                              processes=processes,
                              progress_bar=False)

    results.write_summary("{}/{}_{}_seed_summary.csv".format(outdir,
                                                             prefix,
                                                             seed))

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
