from funkcijos import *
from matplotlib import pyplot as plt
import numpy as np



if __name__ == "__main__":

    # duotas intervalas
    a = -3
    b = 2

    # laisvai pasirenkamas taškų skaičius
    n = 16

    x = []
    y = []

    # true = tolygūs, false = čiobyševo
    first = False



    #x taškų sudarymas
    if first:
        x = np.linspace(a, b, n, endpoint=True)
    else:
        for i in range(n):
            tempX = ((b - a) / 2) * np.cos((np.pi * (2 * i + 1)) / (2 * n)) + (b + a) / 2
            x.append(tempX)



    #y taškų sudarymas
    for i in range(n):
        y.append(f(x[i]))


    # randa funkcijos x reikšmes
    A = np.zeros((n, n))


    for i in range(n):

        for j in range(n):
            A[i, j] = x[i]**j

    # randa koeficientus
    coefficients = np.linalg.solve(A, y)
    print("Koeficientai:\n", coefficients)

    # randa funkcijos taškus
    x_fx, y_fx = get_fx_points(a, b, 0.01)

    # randa interpoliuotos funkcijos taškus
    x_interpolated, y_interpolated = get_interpolated_points(a, b, 0.01, coefficients)

    # piešia grafiką
    plt.title('e^(-x^2)*sin(x^2)*(x-3)')
    plt.plot(x_fx, y_fx, label='Funkcija f(x)')
    plt.plot(x_interpolated, y_interpolated, label='Interpoliuota funkcija f(x)', color="red", linestyle='dashed')
    plt.fill_between(x_fx, y_fx, y_interpolated, color="orange", label="Netiktis")
    plt.scatter(x, y, label='Funkcijos f(x) taškai')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(0.5)
    plt.show()
