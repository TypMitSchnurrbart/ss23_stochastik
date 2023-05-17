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
from bokeh.plotting import figure, output_file, save
from bokeh.io import export_png
from bokeh.models import Range1d, Text
from bokeh.layouts import grid


# ===== FUNCTIONS =====================================


# ===== MAIN ==========================================
if __name__ == "__main__":
    filename_korreliert = "output.txt"
    stats_korreliert = [[], [], []]

    # Kovarianzmatrix für nicht korrelliert
    print("Start generating stats_normal...")
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
    print("Finished generating stats_normal...")

    # Read results from file
    with open(filename_korreliert, "r") as file:
        for line in file:
            entry, value1, value2 = line.strip().split(", ")
            stats_korreliert[0].append(float(entry))
            stats_korreliert[1].append(float(value1))
            stats_korreliert[2].append(float(value2))

    # Plot Größe gegen Intelligenz
    G_I_plot = figure(title="Größe gegen Intelligenz (Korreliert)",
                      # width=1200,
                      # height=800,
                      match_aspect=True,
                      x_axis_label='Größe',
                      y_axis_label='Intelligenz')
    G_I_plot.scatter(stats_korreliert[0], stats_korreliert[1], color='blue')
    G_I_plot_2 = figure(title="Größe gegen Intelligenz (Normalverteilt)",
                        # width=1200,
                        # height=800,
                        match_aspect=True,
                        x_axis_label='Größe',
                        y_axis_label='Intelligenz')
    G_I_plot_2.scatter(stats_normal[0], stats_normal[1], color='green')

    # Plot Größe gegen Stärke
    G_S_plot = figure(title="Größe gegen Stärke (Korreliert)",
                      # width=1200,
                      # height=800,
                      match_aspect=True,
                      x_axis_label='Größe',
                      y_axis_label='Stärke')
    G_S_plot.scatter(stats_korreliert[0], stats_korreliert[2], color='blue')
    G_S_plot_2 = figure(title="Größe gegen Stärke (Normalverteilt)",
                        # width=1200,
                        # height=800,
                        match_aspect=True,
                        x_axis_label='Größe',
                        y_axis_label='Stärke')
    G_S_plot_2.scatter(stats_normal[0], stats_normal[2], color='green')

    G_I_plot.y_range = Range1d(30, 160)
    G_I_plot.x_range = Range1d(90, 250)
    G_I_plot_2.y_range = Range1d(30, 160)
    G_I_plot_2.x_range = Range1d(90, 250)

    G_S_plot.y_range = Range1d(-20, 105)
    G_S_plot.x_range = Range1d(90, 250)
    G_S_plot_2.y_range = Range1d(-20, 105)
    G_S_plot_2.x_range = Range1d(90, 250)

    # Create layout / grid and save to html file
    combined_plot = grid([
        [G_I_plot, G_I_plot_2],
        [G_S_plot, G_S_plot_2]
    ])

    # Save all plots as png
    export_png(combined_plot, filename="plots/combined_plot.png")
    export_png(G_I_plot, filename="plots/G_I_plot.png")
    export_png(G_S_plot, filename="plots/G_S_plot.png")
    export_png(G_I_plot_2, filename="plots/G_I_plot_2.png")
    export_png(G_S_plot_2, filename="plots/G_S_plot_2.png")

    print(f"Sample Covariance:\n{np.cov(stats_normal)}\n")
