import copy
import random
import numpy as np
import matplotlib.pyplot as plt

# const
a = 10
# step
alpha = 0.1
# h value from formula
h = 1e-6
# number of points
n = 4
# min/max range
range_min = -10
range_max = 10
# seed for generating points
seed = 1000101
# precision
eps = 1e-6



def generate_points(_n):
    points = [[0.0, 0.0]]
    random.seed(seed)
    for i in range(_n):
        x = random.uniform(range_min, range_max)
        y = random.uniform(range_min, range_max)
        points.append([x, y])
    return points


def distance(point1, point2):

    return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2


def distance_sum(points):

    _sum = 0
    for i, p1 in enumerate(points):
        for p2 in points[i + 1:]:
            _sum += (distance(p1, p2) - a) ** 2

    return _sum


def optimize_points(points):

    global alpha
    points = copy.deepcopy(points)
    targetValues = []
    iterations = []
    max_iterations = 10000
    current_sum = distance_sum(points)
    primary_sum = current_sum
    counter = 0
    not_improving_counter = 0
    while counter < max_iterations and alpha >= eps:
        targetValues.append(current_sum)
        iterations.append(counter)
        counter += 1
        points_gradient = points_gradient_vector(points, current_sum)
        gradient_norm = [item / np.linalg.norm(points_gradient) for item in points_gradient]
        moved_points = move_by_gradient(gradient_norm, points)
        next_sum = distance_sum(moved_points)
        if next_sum < current_sum:
            points = moved_points
            current_sum = next_sum
        else:
            alpha /= 2
    #plot the iterations-sums
    plt.plot(iterations, targetValues, 'b-')
    plt.title("Tikslo f-jos priklausomybe nuo iteraciju")
    plt.xlabel('Iteracijos')
    plt.ylabel('Tikslo f-ja')
    plt.show()
    return points, current_sum, counter + 1, primary_sum


def move_by_gradient(gradient_vector, points):
    moved_points = copy.deepcopy(points)

    for i, point in enumerate(moved_points):
        point[0] -= alpha * gradient_vector[i * 2]
        point[1] -= alpha * gradient_vector[i * 2 + 1]

    return moved_points


def points_gradient_vector(points, current_sum):

    gradients = [0.0, 0.0]
    for i in range (1, len(points)):
        # X
        changed_points_x = copy.deepcopy(points)
        changed_points_x[i][0] += h

        # Y
        changed_points_y = copy.deepcopy(points)
        changed_points_y[i][1] += h

        gradients.append((distance_sum(changed_points_x) - current_sum) / h)
        gradients.append((distance_sum(changed_points_y) - current_sum) / h)
    return gradients

def connect_each_point(points):

    connected = []
    for i, p1 in enumerate(points):
        for p2 in points[i + 1:]:
            connected.append(p1)
            connected.append(p2)

    return connected

generated_points = generate_points(n)

optimized_points, sum_value, iterations_count, primary_sum = optimize_points(generated_points)

print(
    f"Prad kaina: {primary_sum}\n Optimizuota kaina : {sum_value}\n Iteracijos: {iterations_count}\n Taskai: {optimized_points}")
connected_points = connect_each_point(optimized_points)
print('Pasiektas tikslumas:',alpha)

plt.scatter([x[0] for x in generated_points], [x[1] for x in generated_points], color='b', label='Starting points')
plt.scatter([x[0] for x in optimized_points], [x[1] for x in optimized_points], color='r', label='Optimized points')
plt.plot([x[0] for x in connected_points], [x[1] for x in connected_points], color='g',
         label='Optimized points lines')

plt.legend()
plt.show()
