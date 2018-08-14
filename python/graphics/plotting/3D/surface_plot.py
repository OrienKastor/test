#!/usr/bin/python3

###from matplotlib import pyplot as plt
###
#### [ (x1, y1, z1), (x2, y2, z2), ... (xN, yN, zN) ]
####all_vals = ...
#### (x1, x2, ... xN) , (y1, y2, ... yN) , (z1, z2, ... zN)
###all_xvals, all_yvals, all_zvals = [ [0,0,0,1,1,1,2,2,2], [0,1,2,0,1,2,0,1,2], [0,0,0,0,0,0,0,0,0]  ]
###fig = plt.figure()
###ax = Axes3D(fig)
###X, Y = np.meshgrid(xvals, yvals)
#### This is the part you want:
###Z1 = np.zeros(X.shape, float)
###for (x, y, z) in all_vals:
###    x = find_in_sorted_list(x, xvals)
###    y = find_in_sorted_list(y, yvals)
###    Z1[y,x] = z    
###surf = ax.plot_surface(X, Y, Z1, rstride=1, cstride=1, cmap=cm.jet,
###        linewidth=0, antialiased=False)
###plt.xlabel('Blur standard deviation')  
###plt.ylabel('JPEG quality')
###ax.w_zaxis.set_major_locator(LinearLocator(10))
###ax.w_zaxis.set_major_formatter(FormatStrFormatter('%.03f'))    
###fig.c'olorbar(surf, shrink=0.5, aspect=5)    
###plt.show()


# for more on this: https://jakevdp.github.io/PythonDataScienceHandbook/04.04-density-and-contour-plots.html
# 		    https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

def arrange(a,b,step):
	array = []
	val=a
	while(val<b):
		array.append(val)
		val = val+step
	array.append(b)
	return np.array(array)

# Make data
x = arrange(-5,5,0.25)
y = arrange(-5,5,0.25)
x,y = np.meshgrid(x,y)

z = np.sin( np.sqrt(x**2+y**2) )

surf = ax.plot_surface(x,y,z,cmap=cm.coolwarm,linewidth=0,antialiased=False)

ax.set_zlim(-1.01,1.01)

fig.colorbar(surf,shrink=0.5,aspect=5)

plt.show()


