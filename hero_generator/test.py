"""
    Module to generate stats for heros,
    that are correlating!

    authors:    Marco Mollo
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

# ===== FUNCTIONS =====================================
def generate_random_numbers(mean, covariance_matrix, num_samples):

    # three random variables searched
    num_variables = 3

    # Compute L from cholesy
    L = np.linalg.cholesky(covariance_matrix)
    
    # Generate uncorrelated random numbers
    uncorrelated_numbers = np.random.normal(size=(num_variables, num_samples))
    
    # Apply Cholesky decomposition to introduce correlation
    correlated_numbers = np.dot(L, uncorrelated_numbers)
    
    # Add the means to the correlated random numbers
    random_numbers = correlated_numbers + np.array(mean).reshape((num_variables, 1))
    
    return random_numbers


#===== MAIN ==========================================
if __name__ == "__main__":
    
    # Define the correlation
    mean = [180, 100, 40]

    # Correlationmatrix
    cov = np.array([[0.019881, -1.35, 0.59],
                    [-1.35, 187.443, 0.5],
                    [0.59, 0.5, 199.964]])

    # How many samples we want to produce
    num_samples = 100

    # Generate our random sets of numbers
    random_numbers = generate_random_numbers(mean, cov, num_samples)

    # Round for better visual presentation
    rounded_result = np.around(random_numbers, decimals=3)

    # print every single option given
    for index, entry in enumerate(rounded_result[0]):

        print(f"{index+1}:\t[{entry}, {rounded_result[1][index]}, {rounded_result[2][index]}]")

    # Compute means and correlation matrix
    # of our random numbers to prove the correlation is as wished
    print(f"\nMittelwerte:\n{np.mean(random_numbers, axis=1)}\n")

    print(f"Kovarianzmatrix:\n{np.cov(random_numbers)}\n")
