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

#===== FUNCTIONS =====================================
if __name__ == "__main__":

    data = [0.0, 1.0, 2.0, 5.0, 12.0]

    print(f"""
    Average:\t{average(data)}
    Median:\t{median(data)}
    Varianz:\t{variance(data)}
    STD:\t{deviation(data)}
    
    """)