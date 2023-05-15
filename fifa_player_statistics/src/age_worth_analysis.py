"""
    Module to perform the Age to Value
    evaluation

    author:     Marco Mollo
    date:       03.04.2023
    version:    0.0.1

"""

#===== LIBRARIES =====================================
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import statistics

#===== FUNCTIONS =====================================
def age_hist(data : list, ident : list):
    """
        Process the data to allow displayment
    """

    # Build a list of all the age datapoints to create a hist from
    age_list = []
    age_index = ident.index("Age")
    
    for index, element in enumerate(data):
        age_list.append(element[age_index])

    # Get Histogramm of the Qualities
    # [TODO] Make it prettier
    # [TODO] Hist seems to make some classes form the ages. Maybe as barchart
    sns.distplot(age_list, hist=True, kde=True, bins=30, color="blue",
                 hist_kws={"alpha": 0.5, "histtype": "bar", "ec": "black"},
                 kde_kws={"shade": True})
    plt.axvline(statistics.median(age_list), color="red", linestyle="solid", linewidth=1, label="Median Age")
    plt.xlabel("Age")
    plt.ylabel("Density")
    plt.title("Age Distribution of the Players")
    plt.legend()
    plt.show()

def ageWorth():
    """
        Plot the age of the players against their worth
    """
    df = pd.read_csv("./data/fifa19.csv")
    
    # Convert Value column to numeric
    #df['Value'] = df['Value'].str[1:].str.replace('.', '').str.replace('K', '000').str.replace('M', '000000')
    df['Value'] = df['Value'].str[1:]
    df['Value'] = np.where(df['Value'].str.contains('.'), 
                       df['Value'].str.replace('K', '00').str.replace('M', '00000'), 
                       df['Value'].str.replace('K', '000').str.replace('M', '000000'))
    df['Value'] = df['Value'].str.replace('.', '', regex=False)
    df['Value'] = pd.to_numeric(df['Value'])

    # Create a new dataframe with only the age and value columns
    age_value_df = df[["Age", "Value"]]
    age_value_df = age_value_df[(age_value_df["Age"] != 0) & (age_value_df["Value"] != 0)]
    # Convert the dataframe to a list
    valueList = age_value_df["Value"].tolist()
    ageList = age_value_df["Age"].tolist()


    # Print out Information
    print("|=============================================|")
    print("|Further Information:                         |")
    print("|=============================================|")
    print("|Value Information:                           |")
    print(f"|Mean Value: {statistics.mean(valueList)}               |")
    print(f"|Median Value: {statistics.median(valueList)}                          |") 
    print(f"|Standard Deviation Value: {statistics.stdev(valueList)} |")
    print(f"|Variance Value: {statistics.variance(valueList)}           |")
    print(f"|Min Value: {min(valueList)}                              |")
    print(f"|Max Value: {max(valueList)}                         |")
    print("|=============================================|")
    print("|Age Information:                             |")
    print(f"|Mean Value: {statistics.mean(ageList)}               |")
    print(f"|Median Value: {statistics.median(ageList)}                             |") 
    print(f"|Standard Deviation Value: {statistics.stdev(ageList)}  |")
    print(f"|Variance Value: {statistics.variance(ageList)}            |")
    print(f"|Min Value: {min(ageList)}                                |")
    print(f"|Max Value: {max(ageList)}                                |")
    print("|=============================================|")

    # Plot the data
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.scatter(ageList, valueList, alpha=0.5)
    ax.axhline(y=statistics.mean(valueList), color="red", linestyle="dashed", linewidth=1, label="Mean Value")
    ax.set_xlabel("Age")
    ax.set_ylabel("Value of the Player in €")
    ax.set_title("Age of the Players against their Value")
    ax.legend()
    plt.show()