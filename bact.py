#bacterias en un jar
# al principio: 100
# nacimiento: dx/dt = bx ; b = 1/hora
# muerte: dx/dt = px^2 ; p = 0.5/hora
# total: dx/dt = bx - px^2

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

tstart = 0
tstop = 3600 #una hora
increment = 10 #cada 10 seg.

x0 = 100  #poblacion inicial
b = 1.0/3600  #por segundo
p = 0.5/3600 
t = np.arange(tstart, tstop+1, increment)

#funcion que retorna dx/dt
def mydiff(x, t):
    dxdt =  b*x - p*(x**2)
    return dxdt

#solve ode
x = odeint( mydiff, x0, t )
print(x)

plt.plot(t, x, label='Nº Bact.')
plt.title('Bacterias in a Jar')
plt.xlabel('t(s)')
plt.ylabel('N')
plt.grid()
plt.legend()
plt.show()