import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

x = np.arange(0, 10)
y = np.exp(-x/3.0)
f = interpolate.interp1d(x, y)

print("El valor interpolado en x=", 5, "es", f(5))

#interpolamos muchos puntos!
xnew = np.arange(0, 9, 0.1)
ynew = f(xnew)
plt.plot(x, y, 'o', xnew, ynew, '--')
plt.show()