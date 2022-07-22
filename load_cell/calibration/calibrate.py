# find slope, offset

import numpy as np 
import matplotlib.pyplot as plt
from numpy import linalg as LA

a = np.array([[-0.000097, -1.0],
              [0.000101, -1.0],
              [0.000000, -1.0],
              [-0.000081, -1.0],
              [-0.000079, -1.0],
              [-0.000091, -1.0],
              [-0.000067, -1.0],
              [-0.000030, -1.0],
              [-0.000016, -1.0],
              [0.000064, -1.0]])

b = np.array([[0.0],
              [200.0],
              [98.2],
              [15.4],
              [17.4],
              [5.4],
              [29.9],
              [67.5],
              [81.9],
              [162.4]])

plt.scatter(a[:, 0], b)
plt.show()

i = a.transpose()@a
result = LA.inv(i) @ a.transpose() @ b
print(result)
