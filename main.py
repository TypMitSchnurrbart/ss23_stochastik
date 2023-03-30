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
        data = np.genfromtxt(path, delimiter=",", skip_header=True)

    return data_ident, data


def data_processing(data):
    """
        Process the data to allow displayment
    """

    quality_list = []
    for index, wine in enumerate(data):
        quality_list.append(wine[-1])

    # Get Histogramm of the Qualities
    plt.hist(quality_list)
    plt.xlim(0, 10)
    plt.show()


#===== MAIN ==========================================
if __name__ == "__main__":

    # Data import
    data_indent, np_data = data_import(path="./data/winequality-red.csv")

    data_processing(data=np_data)


    exit()