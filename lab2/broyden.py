# 1.
# 10sin(x1) cos(x2/2) = 0
# x1**2/4 + x2**2/2 - 4 = 0


from __future__ import division
import numpy as np

from numpy.linalg import inv


PREC = 1e-10
MAX_ITERATIONS = 50
x0 = -3
y0 = -2


def broyden(x, y, f_equations, J_equations):
    steps_taken = 0

    f = f_equations(x, y)

    J = inv(J_equations(x, y))

    while np.linalg.norm(f) > PREC and steps_taken < MAX_ITERATIONS:

        s = J.dot(f_equations(x, y))

        x = x - s[0]
        y = y - s[1]

        newf = f_equations(x, y)
        z = newf - f

        u = J.dot(z)
        d = - 1 * s

        J = J + np.dot(((d - u).dot(d)), J) / np.dot(d, u)

        f = newf
        steps_taken += 1
        p = np.linalg.norm(f)
    print(f"Prec: {p}")
    return steps_taken, x, y


def fs(x, y):
    return np.array([10 * np.sin(x) * np.cos(y/2), (x**2)/4 + (y**2)/2 - 4])


def Js(x, y):
    return np.array([[20 * np.cos(x) * np.cos(y/2), 10 * np.sin(x) * (-0.5 * np.sin(y/2))],
                     [0.5 * x, y]])


points = [[-2, 2], [0, 2], [3, 2], [-2, -2], [0, -2], [3, -2]]
for xy in points:
    n, x, y = broyden(xy[0], xy[1], fs, Js)
    print(f"Artinys: {xy}")
    print("iterations: ", n)
    print("x and y: ", x, y)

