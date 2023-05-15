"""
    Module to provide
    general helper functions to handle
    the given data

    author:     Alexander Mueller
    date:       01.04.2023
    version:    0.0.1

"""

#===== FUNCTIONS =====================================
def parse_money(money_string: str):
    """
    Delete the euro sign and the return an actual intereger

    param - {str} - money_string

    return - {int} - money_value
    """

    # Get rid of first sign
    multiplicator = money_string[-1]
    money_string = money_string[1:-1]

    if multiplicator == "M":
        result = int(float(money_string) * 10**6)

    elif multiplicator == "K":
        result = int(float(money_string) * 10**3)

    elif multiplicator == "0":
        result = 0

    else:
        print(f"[ERROR] Got unknown money multiplicator: {multiplicator}! Please add!")
        exit()

    return result