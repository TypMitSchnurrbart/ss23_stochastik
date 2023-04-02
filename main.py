"""
    Python module to play around with data
    and statistics

    author:     Alexander Mueller
    date:       29.03.2023
    version:    0.0.1

    Following the stochastics course B. Staehle

"""

#===== LIBRARIES =====================================
from matplotlib import pyplot as plt

#===== MODULES =======================================
from src.origin_analysis import (
    get_origin_stats,
    visualize_origin_data
)


#===== FUNCTIONS =====================================
def data_import(path):
    
    data = []

    if ".csv" in path:
        
        # Read the first line for the identation
        with open(path, "r") as data_file:
            data_ident = data_file.readline()
            data_ident = data_ident.split(",")

            for line in data_file:
                data.append(line.split(","))

    return data_ident, data


def age_hist(data : list, ident : list):
    """
        Process the data to allow displayment
    """

    # Build a list of all the age datapoints to create a hist from
    age_list = []
    age_index = ident.index("Age")
    
    for index, wine in enumerate(data):
        age_list.append(wine[age_index])

    # Get Histogramm of the Qualities
    # [TODO] Make it prettier
    # [TODO] Hist seems to make some classes form the ages. Maybe as barchart
    plt.hist(age_list)
    plt.xlim(14, 50)
    plt.show()

#===== MAIN ==========================================
if __name__ == "__main__":

    # Data import
    data_ident, np_data = data_import(path="./data/fifa19.csv")

    # Quick histogramm of the age of players
    #age_hist(data=np_data, ident=data_ident)

    origin_data = get_origin_stats(data=np_data, ident=data_ident)
    visualize_origin_data(data=origin_data)
