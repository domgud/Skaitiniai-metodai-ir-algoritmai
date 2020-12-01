from funkcijos import *

point = 100
print("Pasirinktu tasku skaicius: {}".format(point))

# Tasku atrinkimas
n = arr.shape[0]
step = n/point

x = []
y = []

for i in range(0, point):
    index = int(step * i)
    x.append(arr[index, 0])
    y.append(arr[index, 1])

sg = np.zeros(n)
sg[:] = 1

n = len(x)

ff = get_F_values_itemptas(x, y, sg)

# atstumai tarp gretimų taškų
d = getDistance(x)
# its = 100
xx = []
yy = []


its = 100

x1 = x[0]
for i in range(1, point):
    x2 = x1
    for j in range(its):
        step = (x2 - x[i-1]) / (point-1)
        # print("x2: {}\nx[i-1]: {}\ns: {}\n".format(x[i],x[i-1],step))
        value = get_new_y_itemptas(ff[i - 1], ff[i], step, d[i - 1], y[i - 1], y[i], 1)
        # print(x2, value)
        yy.append(value)
        xx.append(x2)
        if step < 0:
            x2 += 1 / its
        else:
            x2 -= 1 / its
    # print()

    x1 = x[i]

# for j in range(0, len(xx)):
#     print(xx[i], yy[j])

plt.plot(xx, yy, label="Funkcija f(x)")

# print(xx)
# print(yy)

for i in range(0, len(x)):
    plt.plot(x[i],y[i], markersize='5',marker='o', color="black")

plt.grid()
plt.show()