import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics

from matplotlib.ticker import FuncFormatter
from pandas import DataFrame
from sklearn import linear_model

from src.config import REG_COLOR



def filter_data(df: DataFrame):
    # Convert relevant columns to numeric
    for key in ['Value', 'Wage']:
        df[key] = df[key].str[1:]
        df[key] = np.where(df[key].str.contains('.', regex=False),
                               df[key].str.replace('K', '00').str.replace('M', '00000'),
                               df[key].str.replace('K', '000').str.replace('M', '000000'))
        df[key] = df[key].str.replace('.', '', regex=False)
        df[key] = pd.to_numeric(df[key])

    # create a new dataframe with only the age and value columns
    wage_value_df = df[["Wage", "Value"]]
    wage_value_df = wage_value_df[(wage_value_df["Wage"] != 0) & (wage_value_df["Value"] != 0)]

    return wage_value_df


def wage_against_value(wage_value_df):
    # reshape the dataframe from (n,) to array of (n, 1)
    valueList = wage_value_df["Value"].values.reshape(-1, 1)
    wageList = wage_value_df["Wage"].values.reshape(-1, 1)

    linReg = linear_model.LinearRegression()
    linReg.fit(valueList, wageList)

    fig, ax = plt.subplots(figsize=(8,6))
    ax.scatter(valueList, wageList, alpha=0.5)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: '{0:g}'.format(x / 1_000)))
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: '{0:g}'.format(x / 1_000_000)))
    plt.plot(valueList, linReg.predict(valueList), color=REG_COLOR, label="Linear Regression")
    ax.axhline(y=statistics.median(wageList.flatten()), color="red", linestyle="dashed", linewidth=1, label="Median")
    ax.axhline(y=statistics.mean(wageList.flatten()), color="green", linestyle="dashed", linewidth=1,
               label="Mean Value")
    ax.set_xlabel("Player's value [Mio. €]")
    ax.set_ylabel("Wage [K. € per week]")
    ax.set_title("Korrelation between wage and value of the players")
    ax.legend()
    plt.show()


if __name__ == '__main__':
    df = pd.read_csv("../data/fifa19.csv")
    df = filter_data(df)
    wage_against_value(df)
