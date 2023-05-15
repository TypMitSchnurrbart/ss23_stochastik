"""
    Module to generate stats for heros,
    that are correlating!

    authors:     Marco Mollo
                Nick Nowak
                Manuel Guenter
                Alexander Mueller
                Daniel Alf

    date:       15.05.2023
    version:    0.0.1

    TODO
        - Understand the task
        - Find a conecept of hero versions
        - Implement a generator based on the chosen concept

"""

# ===== IMPORTS =======================================
import numpy as np
from scipy.stats import multivariate_normal

# ===== FUNCTIONS =====================================


def joint_cdf(x):
    r = mvn.cdf(x)
    print(r)
    return r


def correlated_random_variables(n_samples):
    # Speichern der generierten Zufallsvariablen
    samples = np.zeros((n_samples, 3))
    # Schleife über alle Zufallsstichproben
    for i in range(n_samples):
        accepted = False
        # Schleife zum Abweisen von nicht akzeptierten Zufallsvariablen
        while not accepted:
            # Generierung von Zufallsvariablen
            x = np.random.normal(size=3)
            # Überprüfung der Akzeptanzbedingung
            print(x)
            if np.random.uniform(0, 1) < joint_cdf(x):
                samples[i] = x
                accepted = True
    return samples


# ===== MAIN ==========================================
if __name__ == "__main__":
    # Größe - Intelligenz - Stärke

    # Mittelwerte und Standardabweichungen der Variablen
    mean = [180, 100, 40]
    std = [0.141, 13.691, 14.141]

    # TODO: Kovarianzmatrix der Variablen
    cov = np.array([[0.019881, -1.35, 0.59],
                    [-1.35, 187.443, 0.5],
                    [0.59, 0.5, 199.964]])

    # Erzeugung der multivariaten normalverteilten Zufallsvariablen
    mvn = multivariate_normal(mean=mean, cov=cov)

    # Erzeugen von 10000 korrelierten Zufallsvariablen
    samples = correlated_random_variables(10)

    # Ausgabe von Mittelwert und Standardabweichung jeder Variablen
    print("Mittelwerte:")
    print(np.mean(samples, axis=0))
    print("Standardabweichungen:")
    print(np.std(samples, axis=0))
