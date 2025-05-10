import pathlib
import pandas as pd
import itertools
import numpy as np
import json
import re

def get_turns(filename):
    """
    Read the number of turns if included in the file name
    """
    match = re.search("[0-9]+(?=(_turns))", str(filename))
    return int(match.group(0))

def get_repetitions(filename):
    """
    Read the number of repetitions if included in the file name
    """
    match = re.search("[0-9]+(?=(_repetitions))", str(filename))
    return int(match.group(0))

def read_payoff_matrix(files, number_of_fortran_strategies=None):
    arrays = []
    turns = []
    repetitions = 0
    for gz_path in files:
        repetitions += get_repetitions(gz_path)
        arrays.append(np.array(pd.read_csv(str(gz_path), header=None)))  # Read through pd to deal with float conversion
        turns.append(get_turns(str(gz_path)))
    payoff_matrix = sum(array * turn for turn, array in zip(turns, arrays)) / sum(turns)

    return payoff_matrix, repetitions

def get_indices_of_players(player_names, player_index):
    """
    Returns the indices of the players in `player_names` from `player_index`
    """
    indices = []
    for player in player_names:
        indices.append(list(player_index).index(player))
    return indices

def get_results_of_sub_tournament(
    player_names, 
    payoff_matrix, 
    player_index, 
    characteristics,
):
    player_indices = get_indices_of_players(player_names, player_index)
    player_index_mesh = np.ix_(player_indices, player_indices)
    payoff_sub_matrix = payoff_matrix[player_index_mesh]
    mean_payoffs = np.mean(payoff_sub_matrix, axis=1)
    median_payoffs = np.median(payoff_sub_matrix, axis=1)
    df = pd.DataFrame(
        {
            "Name": player_names,
            "Mean payoff": mean_payoffs,
            "Median payoff": median_payoffs,
        }
    )
    df["Rank"] = df["Mean payoff"].rank(ascending=False)
    original_ranks = []
    for name in df["Name"]:
        try:
            original_rank = characteristics[name]['original_rank']
        except KeyError:
            original_rank = None
        original_ranks.append(original_rank)
    df["Original Rank"] = original_ranks
    return df.sort_values("Rank")

if __name__ == "__main__":

    original_tournament_data_path = pathlib.Path("./data/original_tournament/")
    full_tournament_path = pathlib.Path("./data/full_tournament/")

    full_tournament_player_index = pd.read_csv(
        f"{full_tournament_path}/players.index",
        names=("Name",),
    )

    fortran_player_index = pd.read_csv(
        f"{original_tournament_data_path}/players.index",
        names=("Name",),
    )
    full_tournament_payoff_matrix, _ = read_payoff_matrix(
        full_tournament_path.glob("*payoff_matrix.gz")
    )


    with open(original_tournament_data_path/"fortran_characteristics.json", "r") as f:
        characteristics = json.load(f)

    tournament_id = 0
    fortran_player_set = set(fortran_player_index["Name"])
    #for number_of_new_strategies in [0, 1, 2, 3, 4]:
    for number_of_new_strategies in [4]:
        for names in itertools.combinations(full_tournament_player_index["Name"], number_of_new_strategies):
            if all(name not in fortran_player_set for name in names):
                player_names = list(fortran_player_index["Name"]) + list(names)
                df = get_results_of_sub_tournament(
                    player_names=player_names, 
                    payoff_matrix=full_tournament_payoff_matrix, 
                    player_index=full_tournament_player_index["Name"],
                    characteristics=characteristics,
                )
                df["number of new strategies"] = number_of_new_strategies
                df["tournament id"] = tournament_id
                df = df.sort_values("Rank")
                winner = df.iloc[0]["Name"]
                df["Winner"] = winner
                df = df[df["Name"].isin(names)]
                if tournament_id == 0:
                    df.to_csv("./data/extra_player/main.csv", mode='w', header=True, index=False)
                else:
                    df.to_csv("./data/extra_player/main.csv", mode='a', header=False, index=False)
                tournament_id += 1
