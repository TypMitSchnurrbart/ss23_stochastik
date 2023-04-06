"""
    Module to compute the correlation between multiple
    stats as matrix

    Also visualize the given matric

    author:     Alexander Mueller
    date:       05.04.2023
    version:    0.0.1

"""

#====== MODULES ======================================
from src.config import (
    CORR_STATS,
    REG_COLOR
)

#===== LIBRARIES =====================================
from sklearn import linear_model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json

#===== FUNCTIONS =====================================
def get_correlation_data(data : dict, ident : list):
    """
    Extract all the interest points
    """

    # Compute the Idents that are intersting for us
    start_index = ident.index("Finishing")
    end_index = ident.index("SlidingTackle")

    # Build the data dict
    data_dict = {}
    for stat in ident[start_index : end_index+1]:
        data_dict[stat] = []


    # Get data per player
    for player in data:

        for stat_index in range(start_index, end_index+1):

            try:
                data_dict[ident[stat_index]].append(int(player[stat_index]))
            except ValueError:
                continue
                

    return data_dict, ident[start_index:end_index+1]


def compute_correlation_matrix(data: dict, ident : list):
    """
    Function to transform the data_dict to a correlation matrix
    """

    df = pd.DataFrame(data, columns=ident)

    method = "pearson"
    corr = df.corr(method=method).round(3)

    f = plt.figure(figsize=(19, 15))
    plt.matshow(corr, fignum=f.number)
    plt.xticks(range(df.select_dtypes(['number']).shape[1]), df.select_dtypes(['number']).columns, fontsize=11, rotation=55, ha="left")
    plt.yticks(range(df.select_dtypes(['number']).shape[1]), df.select_dtypes(['number']).columns, fontsize=11)
    cb = plt.colorbar()
    cb.ax.tick_params(labelsize=11)
    plt.title(f'Correlation Matrix - Method: {method}', fontsize=16)
    plt.show()


def regression_analysis(data : dict, ident: list):
    """
    Display scatter plots of stats with high correlation
    found in the correlation matrix
    """

    for stat_pair in CORR_STATS:

        # Correlation
        pearson = round(np.corrcoef(data[stat_pair[0]], data[stat_pair[1]])[0][1], 3)

        # Make the scatter plot with the points of interest
        plt.scatter(data[stat_pair[0]], data[stat_pair[1]], alpha=0.4)


        # Perform the linear Regression
        regr = linear_model.LinearRegression()

        df = pd.DataFrame(data, columns=ident)

        x = df[stat_pair[0]].values
        y = df[stat_pair[1]].values

        x = x.reshape(len(data[stat_pair[0]]), 1)
        y = y.reshape(len(data[stat_pair[1]]), 1)
        
        regr.fit(x, y)

        plt.plot(x, regr.predict(x), color=REG_COLOR, linewidth=2)


        # Format the plot
        plt.title(f"Regression of {stat_pair[0]} to {stat_pair[1]} | Pearson: {pearson}")

        plt.xlabel(f"{stat_pair[0]} [0, 100]")
        plt.ylabel(f"{stat_pair[1]} [0, 100]")

        plt.xlim(0, 100)
        plt.ylim(0, 100)

        plt.show()
