"""
    Moudle to search for correlations in
    the origin of a player and his stats/etc.

    author:     Alexander Mueller
    date:       01.04.2023
    version:    0.0.1

"""

#===== MODULES =======================================
from src.helpers import parse_money

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
            continue

    return data_dict


def visualize_origin_data(data : dict):
    """
    Visualize the prepared data from
    get_origin_stats()
    """

    pass
