import numpy as np
import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4, 5]
y = [15, 10, 9, 6, 2, 0]

x_new = 3.5
y_new = np.interp(x_new, x, y)

print("Valor interpolado en", x_new, "es", y_new)

plt.plot(x, y, '--', x_new, y_new, 'o')
plt.show()