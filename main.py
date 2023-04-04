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
    visualize_origin_data,
    analyze_strong_foot,
    origin_to_speed
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


#===== MAIN ==========================================
if __name__ == "__main__":

    # Data import
    data_ident, np_data = data_import(path="./data/fifa19.csv")

    # Origin Analysis
    origin_data = get_origin_stats(data=np_data, ident=data_ident)

    visualize_origin_data(data=origin_data)
    analyze_strong_foot(data=origin_data)
    origin_to_speed(data=origin_data)

