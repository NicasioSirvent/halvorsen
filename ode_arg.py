import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

tstart = 0
tstop = 25
increment = 1

x0 = 1
T = 5
a = -1/T
t = np.arange(tstart, tstop+1, increment)

#funcion que retorna dx/dt
def mydiff(x, t, a):
    dxdt = a * x
    return dxdt

#solve ode
x = odeint( mydiff, x0, t, args=(a,))
print(x)
a = -0.1
z = odeint( mydiff, x0, t, args=(a,))

plt.plot(t, x, label='a= -0.2')
plt.plot(t, z, label='a= -0.1')
plt.title('Plotting Differential Equation Solutions')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid()
plt.legend()
plt.show()