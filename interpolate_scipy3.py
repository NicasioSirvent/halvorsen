import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x = [100, 150, 200, 250, 300, 400, 500]
y = [2506.7, 2582.8, 2658.1, 2733.7, 2810.4, 2967.9, 3131.6]

f = interp1d(x, y) #kind linear es el default.
f2 = interp1d(x, y, kind='cubic')

ynew = 2680.78 #
f3 = interp1d(y, x) #al reves, para pedir por y
print("El valor de temp que corresponde a Energia", ynew, "es", f3(ynew))

xnew = np.linspace(100, 500, num=20, endpoint=True)

plt.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--' )
plt.legend(['data', 'linear', 'cubic'])
plt.show()