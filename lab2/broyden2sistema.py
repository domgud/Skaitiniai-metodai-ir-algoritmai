import numpy as np
import matplotlib.pyplot as plt

# X = np.arange(-10, 10, 0.01)
# Y = np.arange(-10, 10, 0.01)
# X1, X2 = np.meshgrid(X, Y)

# 2.
# 2x1 + 2x2 − 2x3 + 2x4 − 2 = 0
# −2x1**3 + 4x2*x3 + 128 = 0
# −3x2**2 + 2x3*x2 + 3x4**3 + 15 = 0
# x1 − 6x2 + 2x3 − x4 − 17 = 0

# Lygties sprendimas
def F(x): # x = [x1, x2, x3, x4]
    s = np.array([2*x[0] + 2*x[1] - 2*x[2] + 2*x[3]-2,
                  -2*x[0]**3 + 4*x[1]*x[2] + 128,
                  -3*x[1]**2 + 2*x[2]*x[1] + 3*x[3]**3 + 15,
                  x[0] - 6*x[1] + 2*x[2] - x[3] - 17])
    s.shape = (4, 1)
    s = np.matrix(s)
    return s

def tikslumas(x1,x2,f1,f2,eps):
    if np.isscalar(x1):
            if np.abs(x1+x2) > eps:
                   s =  np.abs(x1-x2)/(np.abs(x1+x2)+np.abs(f1)+np.abs(f2))
            else:  s =  np.abs(x1-x2)+abs(f1)+abs(f2);
    else:
        if (sum(np.abs(x1+x2)) > eps):
               s =  sum(np.abs(x1-x2))/sum(np.abs(x1+x2)+np.abs(f1)+np.abs(f2))
        else:  s =  sum(np.abs(x1-x2)+abs(f1)+abs(f2))
    return s
# I lygciu sistemos sprendimas
n = 4  # lygciu skaicius
# Pradinis artinys
x = np.matrix(np.zeros(shape=(n, 1)))
x[0] = 5
x[1] = -1
x[2] = 0
x[3] = -2

maxiter = 50  # didziausias leistinas iteraciju skaicius
eps = 1e-10  # reikalaujamas tikslumas

# Jakobo matricos sukurimas
A = np.matrix(np.zeros(shape=(n, n)))
x1 = np.zeros(shape=(n, 1))
x1 = np.matrix(x)

A[0,0] = 2
A[0,1] = 2
A[0,2] = -2
A[0,3] = 2

A[1,0] = -6*x[0]**2
A[1,1] = 4*x[2]
A[1,2] = 4*x[1]
A[1,3] = 0

A[2,0] = 0
A[2,1] = -6*x[1]+2*x[2]
A[2,2] = 2*x[1]
A[2,3] = 9*x[3]**2

A[3,0] = 1
A[3,1] = -6
A[3,2] = 2
A[3,3] = -1

ff = F(x) # pradinis f(x(i-1))
x1sprend = 0
x2sprend = 20

for i in range(1, maxiter):
    deltax = -np.linalg.solve(A, ff)
    x1 = np.matrix(x + deltax)
    ff1 = F(x1) # f(x(i))
    A += (ff1 - ff - A * deltax) * deltax.transpose() / (deltax.transpose() * deltax)
    tiksl = tikslumas(x, x1, ff, ff1, eps)
    x1sprend = x
    ff = ff1 # f(x(i-1))
    x = x1
    if tiksl[0] < eps:
        print("Iteracija {} tikslumas = {}".format(i, tiksl))
        break
    else:
        print("Iteracija {} tikslumas = {}".format(i, tiksl))
print("sprendinys: x: {} {} {} {}".format(x1sprend[0],x1sprend[1], x1sprend[2], x1sprend[3]))
#https://www.wolframalpha.com/input/?i=systems+of+equations+calculator&assumption=%22FSelect%22+-%3E+%7B%7B%22SolveSystemOf4EquationsCalculator%22%7D%7D&assumption=%7B%22F%22%2C+%22SolveSystemOf4EquationsCalculator%22%2C+%22equation1%22%7D+-%3E%222*a%2B2*b-2*c%2B2*d-2%3D0%22&assumption=%7B%22F%22%2C+%22SolveSystemOf4EquationsCalculator%22%2C+%22equation2%22%7D+-%3E%22-2*a%5E3%2B4*b*c%2B128%3D0%22&assumption=%7B%22F%22%2C+%22SolveSystemOf4EquationsCalculator%22%2C+%22equation3%22%7D+-%3E%22-3*b%5E2%2B2*c*b%2B3*d%5E3%2B15%3D0%22&assumption=%7B%22F%22%2C+%22SolveSystemOf4EquationsCalculator%22%2C+%22equation4%22%7D+-%3E%22a-6*b%2B2*c-d-17%3D0%22
