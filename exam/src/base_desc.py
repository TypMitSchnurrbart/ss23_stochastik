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
