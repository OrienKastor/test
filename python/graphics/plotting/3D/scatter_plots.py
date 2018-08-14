#!/usr/bin/python3

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

X = [1,2,3,4,5,6,7]
Y = np.array(X)/2.
Z = np.array(X)*2.

ax.scatter(X,Y,Z,c='r',marker='o')

ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')

plt.show()


