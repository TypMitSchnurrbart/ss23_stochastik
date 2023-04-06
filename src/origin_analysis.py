"""
    Moudle to search for correlations in
    the origin of a player and his stats/etc.

    author:     Alexander Mueller
    date:       01.04.2023
    version:    0.0.1

"""

#===== MODULES =======================================
from src.helpers import parse_money
from src.config import (
    BASE_COLOR,
    SEC_COLOR,
    COUNTRIES_OF_INTEREST
)

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
    wage = ident.index("Wage")

    # Build list according to origin
    for player in data:

        # Add country to dict
        if player[origin] not in data_dict.keys():
            data_dict[player[origin]] = {
                "value" : [],
                "strong_foot" : [],
                "speed" : [],
                "wage" : []
            }
        
        if parse_money(player[wage]) <= 10000:
            continue

        # Append the value
        try:
            data_dict[player[origin]]["value"].append(parse_money(player[value]))
            data_dict[player[origin]]["strong_foot"].append(player[strong_foot])
            data_dict[player[origin]]["speed"].append(int(player[speed]))
            data_dict[player[origin]]["wage"].append(parse_money(player[wage]))
        except ValueError:
            print("[WARN]\tSkipped one entry because of missing data")
            continue

    return data_dict

# ====================================================
def visualize_origin_data(data : dict):
    """
    Visualize the prepared data from
    get_origin_stats()
    """

    # Try to show box plot for every country of value

    # Init sublists
    data_ident = []
    data_list = []

    # Build list for every country
    for country in data:

        if country in COUNTRIES_OF_INTEREST:

            data_ident.append(country)
            data_list.append(data[country]["wage"])

    # Define the figure
    fig = plt.figure(figsize =(10, 7))
    ax = fig.add_subplot(111)

    bp = ax.boxplot(data_list, notch="True", patch_artist=True)

    # Set color theme
    for patch in bp['boxes']:
        patch.set_facecolor(BASE_COLOR)
 
    # changing color and linewidth of
    # whiskers
    for whisker in bp['whiskers']:
        whisker.set(color =SEC_COLOR,
                    linewidth = 1.5,
                    linestyle =":")
    
    # changing color and linewidth of
    # caps
    for cap in bp['caps']:
        cap.set(color =SEC_COLOR,
                linewidth = 2)
    
    # changing color and linewidth of
    # medians
    for median in bp['medians']:
        median.set(color ='#FF5349',
                linewidth = 3)


    ax.set_xticklabels(data_ident)
    ax.set_ylabel("Wage [€]")

    plt.ylim([3000, 100000])
    plt.tight_layout()


    # Set overall parameters
    plt.title("Boxplot Wage / Nationality")
    plt.show()


# ====================================================
def analyze_strong_foot(data: dict):
    """
    Analyze the averages of strong foots per country
    """

    # Compute the averages of left / right foots per country
    foot_data = {}
    for country in data:

        # Get number of dataset per country
        players = len(data[country]["strong_foot"])

        # Only look at stats that actually are representable
        # 
        if players < 50:
            continue

        # Get number of right strong players and compute average
        right_strong = data[country]["strong_foot"].count("Right")
        foot_data[country] = (right_strong / players)
    
    
    foot_data = sorted(foot_data.items(), key=lambda x:x[1])

    
    # plot a Stacked Bar Chart using matplotlib
    bar_pos = []
    values = []
    neg_values = []
    country_list = []
    for index, country in enumerate(foot_data):
        
        bar_pos.append(index)
        country_list.append(country[0])
        values.append(country[1])
        neg_values.append(1 - country[1])

    # Visualize
    barWidth = 0.5
    # Create green Bars
    test = plt.bar(bar_pos, values, color=BASE_COLOR, edgecolor='white', width=barWidth)
    # Create orange Bars
    testo = plt.bar(bar_pos, neg_values, bottom=values, color=SEC_COLOR, edgecolor='white', width=barWidth)

    plt.title("Relative frequency of preferred foot per nationality")
    plt.ylabel("Relative frequency")
    plt.xlabel("Nationality")
    plt.xticks(bar_pos, country_list)

    plt.legend([test, testo], ["Right Foot", "Left Foot"])

    plt.show()


#=====================================================
def origin_to_speed(data : dict):
    """
    Mopdule to show the different speed of different countries
    """

    # Init sublists
    data_ident = []
    data_list = []

    # Build list for every country
    for country in data:

        if country in COUNTRIES_OF_INTEREST:

            data_ident.append(country)
            data_list.append(data[country]["speed"])

    # Define the figure
    fig = plt.figure(figsize =(10, 7))
    ax = fig.add_subplot(111)

    bp = ax.boxplot(data_list, notch="True", patch_artist=True)

    # Set color theme
    for patch in bp['boxes']:
        patch.set_facecolor(BASE_COLOR)
 
    # changing color and linewidth of
    # whiskers
    for whisker in bp['whiskers']:
        whisker.set(color =SEC_COLOR,
                    linewidth = 1.5,
                    linestyle =":")
    
    # changing color and linewidth of
    # caps
    for cap in bp['caps']:
        cap.set(color =SEC_COLOR,
                linewidth = 2)
    
    # changing color and linewidth of
    # medians
    for median in bp['medians']:
        median.set(color ='#FF5349',
                linewidth = 3)


    ax.set_xticklabels(data_ident)
    ax.set_ylabel("Speed Value [0,100]")

    # Formating
    plt.ylim([20, 105])
    plt.tight_layout()

    # Set overall parameters
    plt.title("Boxplot Speed / Nationality")
    plt.show()




