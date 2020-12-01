import numpy as np
from funkcijos import *
from matplotlib import pyplot as plt



n = 12
aa = 1
x = np.arange(aa, aa+n)
# temperatures
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
ff = get_F_values(x, y)

# 41 skaidrė
ff[0] = 0
ff[n - 1] = 0

# atstumai tarp gretimų taškų
d = getDistance(x)
its = 100
xx = []
yy = []
# pradedame nuo sausio mėnesio
x1 = 1

# pradedame ciklą nuo antro taško
for i in range(1, n):
    # x2 šiuo atveju bus pradžios taškas (kairysis taškas)
    x2 = x1
    for j in range(its):
        # s yra ilgis, kuris nurodo per kiek esamas taškas yra nutolęs nuo kairiojo (pradinio) taško
        s = x2 - i
        xx.append(x2)
        value = splinify(ff[i - 1], ff[i], s, d[i - 1], y[i - 1], y[i])
        yy.append(value)
        # didiname x kas 0.01
        x2 += 1 / its
    x1 += 1

plt.plot(xx, yy, label="Funkcija f(x)")
plt.scatter(x, y, label="Funkcijos f(x) taškai")
plt.xlabel("Month")
plt.ylabel("Average month temperature in C")
plt.legend()
plt.grid()
plt.xticks(x, range(1, 13))
plt.title("Switzerland 2014 monthly temperatures\nGlobal spline")
plt.grid(0.5)
plt.show()
