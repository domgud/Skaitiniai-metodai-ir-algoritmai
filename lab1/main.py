from sympy import *
import numpy as np
import matplotlib.pyplot as plt
# x = symbols('x')
# t = ((x-2)**2)/4 + 5*sin(x)
# tp = t.diff(x)
# print(tp)
def funcX(x):
    return 1.20*(x**4)-11.84*(x**3)+36.35*(x**2)-34.77*x+7.23

def dFuncX(x):
    return 4.8*x**3 - 35.52*x**2 + 72.7*x - 34.77

def gFunc(x):
    return ((x-2)**2)/4 + 5*np.sin(x)

def dgFunc(x):
    return x/2 + 5*np.cos(x) - 1

def manoFunc(x):
    return np.pi*(x**2)*(6-x)-6
#Metodai

def skenavimas(x1, x2, step, func):
    xprad = x1
    xkitas = xprad + step
    reiksmes = []
    while xkitas < x2:
        if np.sign(func(xprad)) != np.sign(func(xkitas)):
            reiksmes.append([xprad, xkitas])
            print([xprad, xkitas])
        xprad = xkitas
        xkitas = xkitas + step
    return reiksmes

def paprastosIteracijos(func, x, a):
    i = 1
    xmid = x + (np.abs(func(x))/a)
    while(np.abs(func(xmid)) > 1e-10):
        print("{}. x: {} f(x): {}".format(i,xmid, func(xmid)/a))
        xmid = xmid + np.abs(func(xmid))/a
        i += 1
    return xmid

def skenuotiMazejanciu(x1, x2, zingsnis, func):
    counter = 0
    while np.abs(func(x1)) > 1e-10 and x1 + zingsnis <= x2:
        if np.sign(func(x1)) != np.sign(func(x1 + zingsnis)):
            counter += 1
            print("{} x:{:.12f} f(x):{}".format(counter, x1, func(x1)))
            zingsnis /= 2
            continue
        x1 += zingsnis
        counter += 1
        print("{} x:{:.12f} f(x):{:.12f}".format(counter, x1, func(x1)))
    return x1
#funkcija, nuo a iki b, N norimas iteraciju skaicius po kurio nustot dirbti
def secant(f,a,b,N):
    if f(a)*f(b) >= 0:
        print("Secant method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        f_m_n = f(m_n)
        print("{} x:{:.20f} f(x):{}".format(n, m_n, f(m_n)))
        if np.abs(f_m_n) < 1e-10:
            return m_n
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Secant method fails.")
            return None
    return a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))

#reziu skaiciavimas
grubus = 1 + 36.35/1.20
print("{:.2f} {:.2f}".format(-grubus, grubus))

k = 4 - 3
B = 34.77
Rteig = 1 + np.power(B/1.20, 1/k)
print(Rteig)
k = 4 - 0
B = 0
Rneig = (1 + np.power(B/1.20, 1/k))*-1
print (Rneig)

#F(x)

# xx = []
# rez = skenavimas(Rneig, Rteig, 0.05, funcX)
# print(rez)
# for i,j in rez:
#     xx.append(paprastosIteracijos(funcX, i, 20))

# for arr in rez:
#     z = paprastosIteracijos(funcX, arr[0], 100)
#     print (z)
#     print (funcX(z))
#
# for arr in rez:
#     z = skenuotiMazejanciu(arr[0], arr[1], 0.005, funcX)
#     print(z)
#     print (funcX(z))
#
# for arr in rez:
#     z = secant(funcX, arr[0], arr[1], 5)
#     print(z)
#     print(funcX(z))

# x = np.linspace(-grubus, grubus, 100)
# y = funcX(x)
# for a in xx:
#     plt.plot(a, funcX(a), markersize=10, marker='o', label="šaknys")
# plt.plot(x, y, label = "f(x)")
# plt.axvline(-grubus, color = (1,0,0), label = "Grubus")
# plt.axvline(grubus, color = (1,0,0))
# plt.axvline(Rneig, color = (0,1,0), label = "Tikslesnis")
# plt.axvline(Rteig, color = (0,1,0))
# plt.legend()
# plt.grid()
# plt.title("f(x) funkcijos grafikas")
# plt.show()

#G(x)

# x = np.linspace(-5, 15, 100)
# y = gFunc(x)
# plt.plot(x, y, label = "g(x)")
# plt.axvline(-5, color = (1,0,0), label = "Ribos")
# plt.axvline(15, color = (1,0,0))
# plt.legend()
# plt.grid()
# plt.title("g(x) funkcijos grafikas")
# plt.show()
# rez = skenavimas(-5, 15, 0.05, gFunc)
# print(rez)
# for arr in rez:
#     z = paprastosIteracijos(gFunc, arr[0], 10)
#     print (z)
#     print (gFunc(z))
#
# for arr in rez:
#     z = skenuotiMazejanciu(arr[0], arr[1], 0.005, gFunc)
#     print(z)
#     print (gFunc(z))
#
# for arr in rez:
#     z = secant(gFunc, arr[0], arr[1], 5)
#     print("Found root:",z)

# Mano

x = np.linspace(-1, 7, 100)
y = manoFunc(x)
plt.plot(x, y, label = "funkcija")
plt.axvline(0, color = (1,0,0), label = "Ribos")
plt.axvline(6, color = (1,0,0))
plt.legend()
plt.grid()
plt.title("F(h)")
plt.show()
rez = skenavimas(0, 6, 0.005, manoFunc)
print(rez)

for arr in rez:
    z = secant(manoFunc, arr[0], arr[1], 10)
    print("Rezultatas:",z)
    print ("Tikslumas:",manoFunc(z))