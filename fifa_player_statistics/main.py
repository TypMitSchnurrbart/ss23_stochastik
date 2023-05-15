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
from src.origin_analysis import (
    get_origin_stats,
    visualize_origin_data,
    analyze_strong_foot,
    origin_to_speed
)

from src.correlation_analysis import (
    get_correlation_data,
    compute_correlation_matrix,
    regression_analysis
)

from src.age_worth_analysis import (
    ageWorth,
    age_hist
)

#===== FUNCTIONS =====================================
def data_import(path):
    
    data = []

    if ".csv" in path:
        
        # Read the first line for the identation
        with open(path, "r", encoding="utf-8") as data_file:
            data_ident = data_file.readline()
            data_ident = data_ident.split(",")

            for line in data_file:
                data.append(line.split(","))

    return data_ident, data


def np_data_import(path):
    
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
    np_data_ident, np_data = np_data_import(path="./data/fifa19.csv")
    data_ident, data_dict = data_import(path="./data/fifa19.csv")

    # Quick histogramm of the age of players
    age_hist(data=np_data, ident=np_data_ident)
    ageWorth()

    # Origin Analysis
    origin_data = get_origin_stats(data=data_dict, ident=data_ident)

    visualize_origin_data(data=origin_data)
    analyze_strong_foot(data=origin_data)
    origin_to_speed(data=origin_data)

    # Correlation Analysis
    correlation_data, ident = get_correlation_data(data=data_dict, ident=data_ident)
    compute_correlation_matrix(data=correlation_data, ident=ident)

    # Make regression with interesting factors
    regression_analysis(data=correlation_data, ident=ident)
