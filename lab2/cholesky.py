import numpy as np


def choleskyMethod(A, b):
    c = np.linalg.cholesky(A)
    n = c.shape[0]
    print('Apatine choleskio matrica')
    print(c)
    x = np.zeros((n), float)
    y = np.zeros((n), float)
    print('Vykdomi skaiciavimai')
    # forward substitution
    for i in range(0, n):
        s = b[i]
        k = 0
        for j in range(0, i):
            s = (s - c[i, j] * y[j])
            k = k + 1
        y[i] = s / c[i, k]
        print(y)
    print('Baigtas pirmas forward substitution')
    # backwards substitution
    # needs to be transposed back
    c = c.transpose()
    print('Virsutine choleskio funkcija:')
    print(c)
    print('Vykdomi skaiciavimai')
    for i in range(n - 1, -1, -1):
        s = y[i]
        for j in range(i + 1, n):
            s = s - c[i, j] * x[j]
        x[i] = s / c[i, i]
        print(x)
    print('Baigtas antras pertvarkymas su backwards substitution')
    print('Galutinis rezultatas:')
    print(x)



A = np.matrix([[4, 3, -1, 1],
             [3, 9, -2, -2],
             [-1, -2, 11, -1],
             [1, -2, -1, 5]]).astype(np.float)
b = np.matrix([[15], [32], [53], [-5]]).astype(np.float)

choleskyMethod(A,b)