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
import numpy as np
import matplotlib.pyplot as plt


# ===== FUNCTIONS =====================================


# ===== MAIN ==========================================
if __name__ == "__main__":
    # false -> erstellt nicht, true -> erstellt

    plot_keine_korrelation_erstellen = True
    filename_korreliert = "output.txt"

    # Read results from file
    stats_korreliert = [[], [], []]
    with open(filename_korreliert, "r") as file:
        for line in file:
            entry, value1, value2 = line.strip().split(", ")
            stats_korreliert[0].append(float(entry))
            stats_korreliert[1].append(float(value1))
            stats_korreliert[2].append(float(value2))

    # Plot Größe gegen Intelligenz
    fig1, ax1 = plt.subplots()
    ax1.grid(True)
    ax1.set_axisbelow(True)
    ax1.scatter(stats_korreliert[0], stats_korreliert[1], s=1)
    ax1.set_title("Größe gegen Intelligenz")
    ax1.set_xlabel("Größe")
    ax1.set_ylabel("Intelligenz")
    fig1.savefig("plots/G_I_plot.png")

    # Plot Größe gegen Stärke
    fig2, ax2 = plt.subplots()
    ax2.grid(True)
    ax2.set_axisbelow(True)
    ax2.scatter(stats_korreliert[0], stats_korreliert[2], s=1)
    ax2.set_title("Größe gegen Stärke")
    ax2.set_xlabel("Größe")
    ax2.set_ylabel("Stärke")
    fig2.savefig("plots/G_S_plot.png")

    print(f"Sample Covariance:\n{np.cov(stats_korreliert)}\n")

    # Kovarianzmatrix für nicht korrelliert
    if plot_keine_korrelation_erstellen:
        mean = [180, 100, 40]
        stats = np.array([[266.667, 0.0, 0.0],
                          [0.0, 200.0, 0.0],
                          [0.0, 0.0, 200.0]])

        n = 200000
        stats_normal = [[], [], []]
        for _ in range(n):
            abilities = np.random.multivariate_normal(mean, stats)
            stats_normal[0].append(abilities[0])
            stats_normal[1].append(abilities[1])
            stats_normal[2].append(abilities[2])

        # Plot Größe gegen Intelligenz
        fig3, ax3 = plt.subplots()
        ax3.grid(True)
        ax3.set_axisbelow(True)
        ax3.scatter(stats_normal[0], stats_normal[1], s=1)
        ax3.set_title("Größe gegen Intelligenz (Keine Korrelation)")
        ax3.set_xlabel("Größe")
        ax3.set_ylabel("Intelligenz")
        fig3.savefig("plots/G_I_plot_2.png")

        # Plot Größe gegen Stärke
        fig4, ax4 = plt.subplots()
        ax4.grid(True)
        ax4.set_axisbelow(True)
        ax4.scatter(stats_normal[0], stats_normal[2], s=1)
        ax4.set_title("Größe gegen Stärke (Keine Korrelation)")
        ax4.set_xlabel("Größe")
        ax4.set_ylabel("Stärke")
        fig4.savefig("plots/G_S_plot_2.png")

        # Print Cov-matrix
        print(f"Keine Korrelation Covariance:\n{np.cov(stats_normal)}\n")
