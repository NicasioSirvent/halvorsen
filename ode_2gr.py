# Ahora ecuacion de 2º grado: d2x/dt2 = (2 - 2t*dx/dt -3x)/(1 + t^2)
# Cambio de variable:
# x = x1, x1(0) = 0
# dx/dt = x2, x2(0) = 1
#-> dx1/dt = x2
#-> dx2/dt = (2 - 2t*x2 -3x1)/(1 + t**2)


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

tstart = 0
tstop = 5
increment = 0.1

# lista: [x1,x2]
x_init = [0,1]

t = np.arange(tstart, tstop, increment)

#funcion que retorna dx/dt
def mydiff(x, t):
    dx1dt = x[1]  #dx1/dt = x2
    dx2dt = (2 - t*x[1] - 3*x[0])/(1 + t**2)
    dxdt = [dx1dt, dx2dt]
    return dxdt

#solve ode
x = odeint( mydiff, x_init, t)
print(x)

#x es ahora una lista de listas(soluciones de x1 y x2 para cada t)
#creamos nuevas listas seleccionando primeros(x1) y segundos(x2) terminos de esas listas
x1 = x[:,0]
x2 = x[:,1]

plt.plot(t, x1, label='x')
plt.plot(t, x2, label='dx/dt')
plt.title('d2x/dt2 = (2 - t*dx/dt -3x)/(1 + t²)')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid()
plt.legend()
plt.show()