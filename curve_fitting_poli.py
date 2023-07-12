# polinomio a*x^2 + b*x + c

from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

x = [0,1,2,3,4,5]
y = [15,10,9,6,2,0]

def poli_model( x, a, b, c ):
    return a * x**2 + b * x + c

popt, pcov = curve_fit( poli_model, x, y )
print( popt )

plt.plot(x, y, 'or')

xstart = -1
xstop = 6
xstep = 0.1
xmodel = np.arange(xstart, xstop, xstep)

a = popt[0]
b = popt[1]
c = popt[2]
ymodel = a * xmodel**2 + b * xmodel + c

plt.plot(xmodel, ymodel, 'b')
plt.show()