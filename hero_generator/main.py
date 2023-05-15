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


def joint_cdf(x, mvn):
    r = mvn.cdf(x)
    # print(r)
    return r


def correlated_random_variables(n_samples, mvn):
    # Speichern der generierten Zufallsvariablen
    samples = np.zeros((n_samples, 3))
    # Schleife über alle Zufallsstichproben
    for i in range(n_samples):
        if i % 10_000 == 0:
            print(i)
        accepted = False
        # Schleife zum Abweisen von nicht akzeptierten Zufallsvariablen
        while not accepted:
            # Generierung von Zufallsvariablen
            x = np.random.choice([160.0, 180.0, 200.0])
            y = np.random.choice([80.0, 90.0, 100.0, 110.0, 120.0])
            z = np.random.choice([20.0, 30.0, 40.0, 50.0, 60.0])
            X = [x, y, z]
            # Überprüfung der Akzeptanzbedingung
            # print(X)
            if np.random.uniform(0, 1) < joint_cdf(X, mvn):
                samples[i] = X
                accepted = True
    return samples


# ===== MAIN ==========================================
if __name__ == "__main__":
    # Größe - Intelligenz - Stärke

    # Mittelwerte und Standardabweichungen der Variablen
    mean = [180.0, 100.25, 40.0]
    std = [14.142, 13.691, 14.142]

    # TODO: Kovarianzmatrix der Variablen
    cov = np.array([[200.0, -135.0, 60.0],
                    [-135.0, 187.4375, 50.0],
                    [60.0, 50.0, 200.0]])

    # Erzeugung der multivariaten normalverteilten Zufallsvariablen
    mvn = multivariate_normal(mean=mean, cov=cov)

    # Erzeugen von 10000 korrelierten Zufallsvariablen
    samples = correlated_random_variables(10_000, mvn)

    # Ausgabe von Mittelwert und Standardabweichung jeder Variablen
    print("Mittelwerte:")
    print(np.mean(samples, axis=0))
    print("Standardabweichungen:")
    print(np.std(samples, axis=0))
