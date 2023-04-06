"""
    Python module to play around with data
    and statistics

    author:     Alexander Mueller
    date:       29.03.2023
    version:    0.0.1

    Following the stochastics course B. Staehle

"""

#===== LIBRARIES =====================================
import numpy as np

#===== MODULES =======================================
from src.age_worth_analysis import (
    ageWorth,
    age_hist
)

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


#===== MAIN ==========================================
if __name__ == "__main__":

    # Data import
    data_ident, np_data = data_import(path="./data/fifa19.csv")

    # Quick histogramm of the age of players
    age_hist(data=np_data, ident=data_ident)
    ageWorth()

    exit()