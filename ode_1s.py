# Ahora varias ecuaciones de primer grado
# dx/dt = -y, x0 = 1
# dy/dt = x, y0 = 1

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

tstart = -5
tstop = 5
increment = 0.1

z0 = [1,1]

t = np.arange(tstart, tstop, increment)

#funcion que retorna dx/dt
def mydiff(z, t):
    dxdt = -z[1]
    dydt = z[0]
    dzdt = [dxdt, dydt]
    return dzdt

#solve ode
z = odeint( mydiff, z0, t)
print(z)

#z es ahora una lista de listas(soluciones de x e y para cada t)
#creamos nuevas listas seleccionando primeros(x) y segundos(y) terminos de esas listas
x = z[:,0]
y = z[:,1]

plt.plot(t, x, label='x')
plt.plot(t, y, label='y')
plt.title('dx/dt=-y; dy/dt=x')
plt.xlabel('t')
plt.ylabel('z(t)')
plt.grid()
plt.legend()
plt.show()