from funkcijos import *
from matplotlib import pyplot as plt
import numpy as np





if __name__ == "__main__":

    # x taškai
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    y = np.array([
        0.63296,
        1.28477,
        4.43475,
        7.49224,
        9.22946,
        14.4113,
        14.6247,
        13.1831,
        12.4297,
        9.71576,
        5.02944,
        0.68251

    ])

    # interpoliavimo taškų skaičius
    n = len(y)

    a = 1
    b = 12

    A = np.zeros((n, n))

    # randa funkcijos x reikšmes
    for i in range(n):

        for j in range(n):
            A[i, j] = x[i]**j

    # randa koeficientus
    coefficients = np.linalg.solve(A, y)
    print("Koeficientai:\n", coefficients)


    # randa interpoliuotos funkcijos taškus
    x_interpolated, y_interpolated = get_interpolated_points(1, 12, 0.01, coefficients)

    # piešia grafiką
    plt.plot(x, y, label='Funkcija f(x)')
    plt.plot(x_interpolated, y_interpolated, label='Interpoliuota funkcija f(x)', color="red", linestyle='dashed')
    plt.scatter(x, y, label='Funkcijos f(x) taškai')
    plt.title("Switzerland 2014 monthly temperatures\nPolynomial interpolation")
    plt.xlabel('Month')
    plt.ylabel('Average month temperature in C')
    plt.xticks(x, range(1, 13))
    plt.legend()
    plt.grid(0.5)
    plt.show()
