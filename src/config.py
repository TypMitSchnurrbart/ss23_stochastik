"""
    Module to store const / config parameters

"""

# Base Color Theme
BASE_COLOR = "#104E8B"
SEC_COLOR = '#FF7D40'
REG_COLOR = "#d20404"

# Countires to evaluate
COUNTRIES_OF_INTEREST = ["Germany", "England", "Brazil", "Argentina", "France", "Italy"]

# Stats for the Regression as list in list! [[], [], ...]
# Please only use Player stats from [0, 100] that are already in the corr_matrix
CORR_STATS = [["Positioning", "SlidingTackle"], ["Acceleration", "Curve"]]