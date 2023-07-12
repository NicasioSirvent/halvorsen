# 3 dw/dt + ( w / (1 + t^2) ) = cos(t) .. reordeno
#  dw/dt = (cos(t) - (w/(1+t^2))) / 3

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

tstart = 0
tstop = 5
increment = 0.1
w0 = 1

t = np.arange(tstart, tstop, increment)

#funcion que retorna dx/dt
def mydiff(w, t):
    dwdt = ( np.cos(t) - (w / (1 + t**2)) ) / 3
    return dwdt

#solve ode
W = odeint( mydiff, w0, t )
print(W)

plt.plot( t, W, label='W' )
plt.title( 'Plotting Differential Equation Solutions' )
plt.xlabel( 't' )
plt.ylabel( 'W(t)' ) 
plt.grid()
plt.legend()
plt.show()