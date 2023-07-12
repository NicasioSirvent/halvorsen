#Ejercicio Final del capitulo

from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

x = [100, 150, 200, 250, 300, 400, 500]
y = [2506.7, 2582.8, 2658.1, 2733.7, 2810.4, 2967.9, 3131.6]

plt.plot(x, y, 'or') #lo dibujamos...

def linear_model( x, a, b ):
    return a * x + b

popt, pcov = curve_fit( linear_model, x, y )
print( popt )

xstart = 50
xstop = 550
xstep = 50
xmodel = np.arange(xstart, xstop, xstep)

a = popt[0]
b = popt[1]

ymodel = a * xmodel + b

plt.plot(xmodel, ymodel)
plt.show()