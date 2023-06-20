"""

    Module to call the distribution functions

    author:     Alexander Mueller
    date:       29.03.2023
    version:    0.0.1

    Every function that is "[VERIFIED]" is checked
    to give the same results as b.staehle considers
    correct in her script!

"""

#===== IMPORTS =======================================
import math
from scipy.stats import poisson

#===== FUNCTIONS =====================================
def poisson_self(rate, k):
    return ((rate**k) * math.e**-rate) / math.factorial(k)
