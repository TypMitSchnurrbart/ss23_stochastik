"""
    Module to store const / config parameters

"""

# Base Color Theme
BASE_COLOR = "#b5ffb9"
SEC_COLOR = '#f9bc86'
REG_COLOR = "#d20404"

# Countires to evaluate
COUNTRIES_OF_INTEREST = ["Germany", "England", "Brazil", "Argentina", "Japan", "Italy"]

# Stats for the Regression as list in list! [[], [], ...]
# Please only use Player stats from [0, 100] that are already in the corr_matrix
CORR_STATS = [["Positioning", "SlidingTackle"], ["Acceleration", "Curve"]]