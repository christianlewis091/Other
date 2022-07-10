import numpy as np
a = np.arange(10)
b = np.where(a > 5, a, 10*a)
print(b)

