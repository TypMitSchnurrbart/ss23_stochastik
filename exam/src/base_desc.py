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
import math
import numpy as np
import pandas as pd
from collections import Counter
from tabulate import tabulate
import matplotlib.pyplot as plt
from scipy.stats import mode

#===== FUNCTIONS =====================================
def median(stats : list):
    """Quick Median [VERIFIED]"""

    # Get input length
    len_stats = len(stats)

    # Get simple case
    if len_stats == 0:
        return None

    # Compute Median
    stats = sorted(stats)
    middle_index = int((len_stats-1)/2)
    return stats[middle_index] if len_stats % 2 == 1 else (stats[middle_index] + stats[middle_index+1]) / 2


def average(input_set : list):
    """Average of a given list of int / floats"""
    return sum(input_set) / len(input_set)


def variance(data : list):
    """ Quick Variance [VERIFIED]"""

    avg = average(data)
    sum_variance = 0
    for point in data:
        sum_variance += (point - avg)**2

    return 1 / (len(data)-1) * sum_variance


def deviation(data : list):
    """Quick STD Deviation [VERIFIED]"""

    return math.sqrt(variance(data))

def quantil(data: list, quantil: float):
    """Quick Quantil [VERIFIED]"""

    data.sort()
    index = int(quantil * (len(data) - 1))
    if (quantil * len(data)) % 1 == 0.0:
        return (data[index] + data[index + 1]) / 2
    else:
        return data[int(np.ceil(quantil * (len(data)))-1)]

def haeufigkeit(data: list):
    """Quick Haeufigkeit [VERIFIED]"""
    
    kategorien = set(data)
    anzahl = len(data)

    abs_haeufigkeit = Counter(data)
    rel_haeufigkeit = {k: v / anzahl for k, v in abs_haeufigkeit.items()}
    
    # tabelle = pd.DataFrame({'Kategorie': ['Absolute Häufigkeit', 'Relative Häufigkeit'],
    #     **{k: [abs_haeufigkeit[k], rel_haeufigkeit[k]] for k in kategorien}})
    
    # pd.set_option('display.max_colwidth', None)
    # return tabelle.to_string(index=False, justify='center')

    data = [['Absolute Häufigkeit'] + [abs_haeufigkeit[k] for k in kategorien],
        ['Relative Häufigkeit'] + [rel_haeufigkeit[k] for k in kategorien]]

    headers = ['Kategorie'] + list(kategorien)

    table = tabulate(data, headers, tablefmt='pipe')
    return table

def getHistogram(data: list):

    abs_haeufigkeit = Counter(data)

    categories = list(abs_haeufigkeit.keys())
    frequencies = list(abs_haeufigkeit.values())

    plt.bar(categories, frequencies)
    plt.xlabel('Kategorie')
    plt.ylabel('Absolute Häufigkeit')
    plt.title('Histogramm der absoluten Häufigkeiten')
    plt.show()

def getEmpirisch(data: list):
    abs_haeufigkeit = Counter(data)

    categories = sorted(abs_haeufigkeit.keys())
    frequencies = np.cumsum(list(abs_haeufigkeit.values())) / len(data)

    plt.plot(categories, frequencies, drawstyle='steps-post')
    plt.xlabel('Kategorie')
    plt.ylabel('Empirische Verteilungsfunktion')
    plt.title('Empirische Verteilungsfunktion')
    plt.ylim([0, 1])
    plt.show()