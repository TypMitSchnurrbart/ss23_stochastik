"""
    Python module to play around with data
    and statistics

    author:     Alexander Mueller
    date:       29.03.2023
    version:    0.0.1

    Following the stochastics course B. Staehle

    What factors make a good red wine?

"""

#===== LIBRARIES =====================================
import numpy as np
from matplotlib import pyplot as plt


#===== FUNCTIONS =====================================
def data_import(path):
    
    if ".csv" in path:
        
        # Read the first line for the identation
        with open(path, "r") as data_file:
            data_ident = data_file.readline()
            data_ident = data_ident.split(",")

        # Read the data
        data = np.genfromtxt(path, delimiter=",", skip_header=True, usecols=np.arange(0, len(data_ident)))

    return data_ident, data


def age_hist(data : list, ident : list):
    """
        Process the data to allow displayment
    """

    # Create a simple histogramm of 
    age_list = []
    age_index = ident.index("Age")
    for index, wine in enumerate(data):
        age_list.append(wine[age_index])

    # Get Histogramm of the Qualities
    plt.hist(age_list)
    plt.xlim(14, 50)
    plt.show()


#===== MAIN ==========================================
if __name__ == "__main__":

    # Data import
    data_ident, np_data = data_import(path="./data/fifa19.csv")

    # Quick histogramm of the age of players
    age_hist(data=np_data, ident=data_ident)


    exit()