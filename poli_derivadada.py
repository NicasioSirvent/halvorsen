import numpy as np

# 3x^3 + 4x^2 - 5x + 1
pol = [3,4,5,1]


dpdx = np.polyder(pol)
print(dpdx) # -> [9,8,5] -> 9x^2 + 8x + 5