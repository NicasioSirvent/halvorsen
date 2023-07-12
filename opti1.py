#pruebas con optimizacion: encontrar minimo de funcion.
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

xstart = -5
xstop = 5
N = 100
dx = (xstart - xstop)/N

x = np.linspace(xstart, xstop, N+1)
#x = np.arange(x_min, x_max+dx, dx)  ##equivalente

y = x**2 + 2*x + 1
def f(x):
    return x**2 + 2*x + 1

min = optimize.fminbound(f,xstart,xstop)
print(min)
plt.plot(min,f(min),'or')

#mi propia funcion
mimin = xstart #cojo el primero
for i in x:
    if f(i) < f(mimin):
        mimin = i

print("mimin:", mimin)

#comparo con otras funciones:
fmin_min = optimize.fmin(f, 1) #1: initial valor
print("fmin:", fmin_min)

minimize_min = optimize.minimize(f, 1)
print("minimze_min:", minimize_min.x) 

plt.plot(x,y)
plt.xlim([xstart,xstop])
plt.show()