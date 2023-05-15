import numpy as np
import pandas as pd
import statistics

from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter
from pandas import DataFrame


def filter_data(df: DataFrame):
    df['Wage'] = df['Wage'].str[1:]
    df['Wage'] = np.where(df['Wage'].str.contains('.', regex=False),
                           df['Wage'].str.replace('K', '00').str.replace('M', '00000'),
                           df['Wage'].str.replace('K', '000').str.replace('M', '000000'))
    df['Wage'] = df['Wage'].str.replace('.', '', regex=False)
    df['Wage'] = pd.to_numeric(df['Wage'])
    return df


def wage_per_club(df: DataFrame):

    # groub by Club and take wage into lists
    df2 = df.groupby(['Club'])['Wage'].apply(list)

    # search 6 max paying Clubs
    df3 = df.groupby(['Club'])['Wage'].sum()
    df3 = df3.sort_values(ascending=False).nlargest(6)

    # build data
    data = []
    for key in df3.keys():
        data.append(df2[key])

    # boxplot
    fig, ax = plt.subplots(figsize=(12,7))
    ax.boxplot(data, notch="True", patch_artist=True)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: '{0:g}'.format(x / 1_000)))
    ax.set_xticklabels(df3.keys())
    ax.set_ylabel("Wage [K. € per week]")
    plt.title("Boxplot: Wage per Club")
    plt.show()

    # histogram
    fig, ax = plt.subplots(figsize=(12,7))
    plt.bar(df3.keys(), df3 * 4 * 12)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, pos: '{0:g}'.format(x / 1_000_000)))
    plt.xlabel("Club")
    plt.ylabel("Wage [Mio. € per year]")
    plt.title("Histogram: Wage sum per Club")
    plt.show()


if __name__ == '__main__':
    data_frame = pd.read_csv("../data/fifa19.csv")
    data_frame = filter_data(data_frame)
    wage_per_club(data_frame)
