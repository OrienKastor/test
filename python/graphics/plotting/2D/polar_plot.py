#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,2*np.pi,400)
y = np.sin(x)*0.1

f, ax = plt.subplots(2,2, subplot_kw=dict(projection='polar'))
ax[0,0].plot(x,y)
ax[0,0].set_title('Axis[0,0]')
ax[0,1].scatter(x,y)
ax[1,0].scatter(x,y**2.)
ax[1,1].plot(x,y**2.)
f.subplots_adjust(hspace=0.3)

plt.show()
