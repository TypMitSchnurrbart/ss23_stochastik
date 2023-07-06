"""

    Quick easy and OWN stat functions to compute the basics
    and therefore know what is happening in the exam

    author:     Alexander Mueller
    date:       29.03.2023
    version:    0.0.1

    Every function that is "[VERIFIED]" is checked
    to give the same results as b.staehle considers
    correct in her script!

"""

#===== IMPORTS =======================================
from src.base_desc import *
import statistics
import numpy as np
from scipy.stats import pearsonr

#===== FUNCTIONS =====================================
if __name__ == "__main__":

    data = [125, 100, 130, 150, 150, 250, 250, 250]

    data_cov = []


    if len(data_cov) > 0:
        print(f"""
        Cov:\t{np.cov(data, data_cov)[0, 1]}
        Pearson:\t{pearsonr(data, data_cov)[1]}
        """)


    data.sort()

    print(f"""
    {data}
    Mode:\t{statistics.mode(data)}
    Average:\t{average(data)}
    Median:\t{median(data)}
    Varianz:\t{variance(data)}
    STD:\t{deviation(data)}
    
    """)