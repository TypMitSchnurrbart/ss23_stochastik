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
        - Think about changing the height variance
        - Cov of I and S not granted!

        - IS THIS EVEN CORRECT? Bc our results leave the
          given result spaces! But would be weird to stick to those smh

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


def adjust_values(random_list : list, target_list : list):

    adjusted_list = []

    for value in random_list:

        closest_value = min(target_list, key=lambda x: abs(x - value))

        adjusted_list.append(closest_value)

    return adjusted_list


#===== MAIN ==========================================
if __name__ == "__main__":
    
    # Define the correlation
    mean = [180, 102.5, 40]

    # Correlationmatrix
    cov = np.array([[200.0, -135.0, 60.0],
                    [-135.0, 187.4375, -50.0],
                    [60.0, -50.0, 200.0]])

    # How many samples we want to produce
    num_samples = 2000000

    # Generate our random sets of numbers
    random_numbers = generate_random_numbers(mean, cov, num_samples)

    # Round for better visual presentation
    rounded_result = np.around(random_numbers, decimals=3)


    # Adjust the value to the target lists
    target_lists = [[160, 180, 200],
                    [80, 90, 100, 110, 120],
                    [20, 30, 40, 50, 60]]
    for index, entry in enumerate(rounded_result):
        rounded_result[index] = adjust_values(entry, target_lists[index])


    # print every single option given
    for index, entry in enumerate(rounded_result[0]):

        print(f"{index+1}:\t[{entry}, {rounded_result[1][index]}, {rounded_result[2][index]}]")

    # Compute means and correlation matrix
    # of our random numbers to prove the correlation is as wished
    print(f"\nMittelwerte:\n{np.mean(random_numbers, axis=1)}\n")

    print(f"Kovarianzmatrix:\n{np.cov(random_numbers)}\n")

    print(f"Abweichungen der Kovarianzmatrix:\n{np.cov(random_numbers)-cov}\n")
