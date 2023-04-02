"""
    Moudle to search for correlations in
    the origin of a player and his stats/etc.

    author:     Alexander Mueller
    date:       01.04.2023
    version:    0.0.1

"""

#===== MODULES =======================================
from src.helpers import parse_money

#===== LIBRARIES =====================================
from matplotlib import pyplot as plt

#===== BUILD-INS =====================================
import json


#===== FUNCTIONS =====================================
def get_origin_stats(data : list, ident: list):
    """
    Compute a dict with all the stats of the players from one country
    """

    data_dict = {}

    # Get index of origin
    origin = ident.index("Nationality")
    value = ident.index("Value")
    strong_foot = ident.index("Preferred Foot")
    speed = ident.index("SprintSpeed")

    # Build list according to origin
    for player in data:

        # Add country to dict
        if player[origin] not in data_dict.keys():
            data_dict[player[origin]] = {
                "value" : [],
                "strong_foot" : [],
                "speed" : []
            }
        
        # Append the value
        try:
            data_dict[player[origin]]["value"].append(parse_money(player[value]))
            data_dict[player[origin]]["strong_foot"].append(player[strong_foot])
            data_dict[player[origin]]["speed"].append(int(player[speed]))
        except ValueError:
            print("[WARN]\tSkipped one entry because of missing data")
            continue

    return data_dict


def visualize_origin_data(data : dict):
    """
    Visualize the prepared data from
    get_origin_stats()
    """

    # Try to show box plot for every country of value

    # Init sublists
    data_ident = []
    data_list = []

    countries_of_interest = ["Germany", "England"]

    # Build list for every country
    for country in data:

        if country in countries_of_interest:

            data_ident.append(country)
            data_list.append(data[country]["value"])


    print(data_list)


    # Define the figure
    fig = plt.figure(figsize =(10, 7))
    ax = fig.add_subplot(111)


    out_plot = ax.boxplot(data_list, notch="True")

    ax.set_xticklabels(data_ident)

    plt.show()

