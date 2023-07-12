import numpy as np
import matplotlib.pyplot as plt
x = [1, 2, 3]
y = [3, 2, 0]

x_new = 2.5
y_new = np.interp(x_new, x, y)

print("Valor interpolado en", x_new, "es", y_new)