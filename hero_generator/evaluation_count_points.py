"""
    Module to display the generated stats for heros!

    authors:    Marco Mollo
                Nick Nowak
                Manuel Guenter
                Alexander Mueller
                Daniel Alf

    date:       17.05.2023
    version:    0.0.1
"""

# ===== IMPORTS =======================================
from math import log
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


# ===== FUNCTIONS =====================================


# ===== MAIN ==========================================
if __name__ == "__main__":
    filename_korreliert = "output.txt"

    # Read results from file
    stats_korreliert = [[], [], []]
    with open(filename_korreliert, "r") as file:
        for line in file:
            entry, value1, value2 = line.strip().split(", ")
            stats_korreliert[0].append(float(entry))
            stats_korreliert[1].append(float(value1))
            stats_korreliert[2].append(float(value2))

    # Zähle die Häufigkeit der Punkte
    target_lists = [[160, 180, 200],            # Größe
                    [80, 90, 100, 110, 120],    # Intelligenz
                    [20, 30, 40, 50, 60]]       # Stärke

    # Zähle Punkte Größe und Intelligenz
    # Kombiniere die Elemente von x und y paarweise
    kombinationen_G_I = zip(stats_korreliert[0], stats_korreliert[1])
    kombinationen_G_S = zip(stats_korreliert[0], stats_korreliert[2])

    # Verwende die Counter-Klasse, um die Anzahl jeder Kombination zu zählen
    anzahl_kombinationen_G_I = Counter(kombinationen_G_I)
    anzahl_kombinationen_G_S = Counter(kombinationen_G_S)

    # Diagramm Größe gegen Intelligenz
    kombinationen = list(anzahl_kombinationen_G_I.keys())
    x = [item[0] for item in list(anzahl_kombinationen_G_I.keys())]
    y = [item[1] for item in list(anzahl_kombinationen_G_I.keys())]

    häufigkeiten = list(anzahl_kombinationen_G_I.values())
    sizes = [item/300 for item in häufigkeiten]

    fig1, ax1 = plt.subplots()
    ax1.grid(True)
    ax1.set_axisbelow(True)
    ax1.scatter(x, y, s=sizes)
    ax1.set_title("Größe gegen Intelligenz")
    ax1.set_xlabel("Größe")
    ax1.set_ylabel("Intelligenz")
    for i in range(len(x)):
        ax1.text(x[i]+2, y[i], str(häufigkeiten[i]) + 'x',
                 bbox={'facecolor': 'white', 'pad': 2})
    fig1.savefig("plots/G_I_plot_Werte.png")

    # # Plot Größe gegen Stärke
    kombinationen = list(anzahl_kombinationen_G_S.keys())
    x = [item[0] for item in list(anzahl_kombinationen_G_S.keys())]
    y = [item[1] for item in list(anzahl_kombinationen_G_S.keys())]

    häufigkeiten = list(anzahl_kombinationen_G_S.values())
    sizes = [item/300 for item in häufigkeiten]

    fig2, ax2 = plt.subplots()
    ax2.grid(True)
    ax2.set_axisbelow(True)
    ax2.scatter(x, y, s=sizes)
    ax2.set_title("Größe gegen Stärke")
    ax2.set_xlabel("Größe")
    ax2.set_ylabel("Stärke")
    for i in range(len(x)):
        ax2.text(x[i]+2, y[i], str(häufigkeiten[i]) + 'x',
                 bbox={'facecolor': 'white', 'pad': 2})
    fig2.savefig("plots/G_S_plot_Werte.png")

    print(f"Sample Covariance:\n{np.cov(stats_korreliert)}\n")
