#optimizacion con 2 variables independientes...
# busco en google:
# b = [0.1 + i / 100 for i in range(0, 510)] .. vaya vaya...
# 
# A meshgrid can take 2 1D arrays, and return 2 2D arrays such that every index 
# in the arrays corresponds to a unique pair of elements from the original 1D arrays.
# osease: x(0,1,2) e y(0,1,2) .. en plano son 9 puntos
# el meshgrid devuelve 2 arrays, uno con las coordenadas x de los 9 puntos, otro con las y.
# ahora, ya aplicable z = x * y

from matplotlib import projections
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from zmq import proxy_steerable

#meshgrid?
xstart = -5
xstop = 5
N = 10
dx = (xstop - xstart) / N

x = np.linspace(xstart, xstop, N+1)
y = np.linspace(xstart, xstop, N+1)

X, Y = np.meshgrid(x, y)
#print(X)
#print(Y)
#z = X * Y
#print(z) -> array tal....

Z = 2 * (X - 1)**2 + X - 2 + (Y - 2)**2 + Y
def f(params):
    x,y = params
    return 2 * (x - 1)**2 + x - 2 + (y - 2)**2 + y

#minimo?
initial_guess = [1,1]
min = optimize.minimize(f, initial_guess)
print(min.x)

#figura
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
#ax = Axes3D(fig)
ax.plot_surface(X, Y, Z)
ax.scatter(min.x[0], min.x[1], f([min.x[0],min.x[1]]))
plt.xlabel('X')
plt.ylabel('Y')
plt.show()