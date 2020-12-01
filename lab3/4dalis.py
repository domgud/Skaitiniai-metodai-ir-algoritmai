from funkcijos import *

#data
#     0.63296,
#     1.28477,
#     4.43475,
#     7.49224,
#     9.22946,
#     14.4113,
#     14.6247,
#     13.1831,
#     12.4297,
#     9.71576,
#     5.02944,
#     0.68251

deg = np.array([#x, y
       [1.0,  0.63296],
       [2.0, 1.28477],
       [3.0, 4.43475],
       [4.0, 7.49224],
       [5.0, 9.22946],
       [6.0, 14.4113],
       [7.0, 14.6247],
       [8.0, 13.1831],
       [9.0, 12.4297],
       [10.0, 9.71576],
       [11.0, 5.02944],
       [12.0, 0.68251]])

# Creates a polynomial function according to the number of coefficients
def polynomial(x, c):
  deg = len(c)
  result = 0

  for i in range(0,deg):
    result += c[i]*x**i

  return result;


# 2nd degree polynomial
#def f2(x, c0, c1, c2):
#  return c0+c1*x+c2*x*x;

#Creates a G matrix from x points and accordingly from a polynomial degree.
def G_matrix(x_points, degree):
  n = len(x_points)
  G = np.zeros((n,degree), dtype="float")

  for i in range(0, n):
    for j in range(0, degree):
      G[i][j] = x_points[i]**j;

  return G;



#polynomial degree plus 1, e.g.: m = 2(2nd) + 1 = 2

x_points = deg[:,0]

#Select the degree of polynomial
polynomialDegree = 5
G = G_matrix(x_points, polynomialDegree)
G_transposed = np.transpose(G)

y = deg[:,1]

#calculating coefficient's matrix c.
A = np.matmul(G_transposed, G);
b = np.matmul(G_transposed, y);
c = np.linalg.solve(A, b);

#drawing graph
x = np.linspace(1, 12, 200)
y = polynomial(x,c)

plt.plot(x,y)
plt.grid()

n = len(deg)
for i in range(0,n):
  plt.plot(deg[i][0],deg[i][1], markersize=5, marker='o',color='red',)
plt.show()
