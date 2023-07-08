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
from scipy.stats import pearsonr, mode
from collections import Counter
import os

#===== FUNCTIONS =====================================
if __name__ == "__main__":

    data = [1, 1, 2, 2, 3, 3]
    data_cov = [1, 1, 2, 2, 3, 3]

    modalwerte = [k for k, v in Counter(data).items() if v == max(Counter(data).values())]
    # Quantil berechnen
    q = 0.1

    if len(data_cov) > 0:
        print(f"""
        Cov:\t{np.cov(data, data_cov)[0, 1]}
        Pearson:\t{pearsonr(data, data_cov)}
        """)

    data.sort()

    print(f"""
    {data}
    Average:\t{average(data)}
    Median:\t{median(data)}
    Modalwert:\t{sorted(modalwerte)}
    Varianz:\t{variance(data)}
    STD:\t{deviation(data)}
    Q_{q}:\t{quantil(data, q)}
    IQA:\t{quantil(data, 0.75) - quantil(data, 0.25)}
    Spannweite:\t{data[-1] - data[0]}
    """)

    print(f""" Alle Quartile:          
    Q_{0.25}:\t{quantil(data, 0.25)}
    Q_{0.5}:\t{quantil(data, 0.5)}
    Q_{0.75}:\t{quantil(data, 0.75)}
    """)

    print(haeufigkeit(data))
    #getHistogram(data)
    #getEmpirisch(data)