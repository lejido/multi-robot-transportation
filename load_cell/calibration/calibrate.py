# find slope, offset

import numpy as np 
import matplotlib.pyplot as plt
from numpy import linalg as LA

a = np.array([[0.000052, 1.0],
              [0.000236, 1.0],
              [0.000043, 1.0],
              [0.000102, 1.0],
              [0.000047, 1.0],
              [0.000038, 1.0],
              [0.000056, 1.0],
              [0.000047, 1.0],
              [0.000082, 1.0],
              [0.000050, 1.0],
              [0.000034, 1.0]])

b = np.array([[17.4],
              [200.6],
              [9.1],
              [67.7],
              [13.2],
              [4.5],
              [21.6],
              [13.6],
              [48.1],
              [16.0],
              [0.0]])

plt.scatter(a[:, 0], b)
plt.show()

i = a.transpose()@a
result = LA.inv(i) @ a.transpose() @ b
print(result)
