#!/usr/bin/python3

# -*- coding: utf-8 -*-
"""
Created on Thu May 10 10:01:39 2018

@author: razor
"""

from matplotlib import pyplot as plt # or import matplotlib.pyplot as plt
import numpy as np

def one():

	plt.close('all')
	
	fig = plt.figure(1) # can just use 1 in the case of just making a new figure you don't want to reference later
	
	plt.subplot(211)
	plt.plot(np.sin(range(0,100)))
	plt.title('title')
	plt.xlabel('x')
	plt.ylabel('y')

	
	plt.subplot(212)
	plt.plot(1,2,'x')
	
	plt.plot(2,3,'x')

	fig.subplots_adjust(hspace=0.3)
	
	plt.show()


def two():

	x = np.linspace(0,2*np.pi,400)
	y = np.sin(x**2.)

	plt.close('all')

	f, ax = plt.subplots(4)	
	ax[0].plot(x,y)
	ax[0].set_title('Simple plot')
	ax[1].scatter(x,y)
	ax[2].plot(x,y,color='r')
	ax[3].scatter(x,y)

	f, axarr = plt.subplots(2,sharex=True)
	axarr[0].plot(x,y)
	axarr[0].set_title('sharing x-axis')
	axarr[1].scatter(x,y)
	
	f, (ax1,ax2) = plt.subplots(1,2,sharey=True)
	ax1.plot(x,y)
	ax1.set_title('Sharing Y axis')
	ax2.scatter(x,y)
	
	f, (ax1, ax2, ax3) = plt.subplots(3,sharex=True,sharey=True)
	ax1.plot(x,y)
	ax1.set_title('Sharing X and Y')
	ax2.scatter(x,y)
	ax3.scatter(x,2*y**2.-1,color='r')
	# alter the subplots layout
	f.subplots_adjust(hspace=0)
	plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
	
	f, ((ax1, ax2),(ax3, ax4)) = plt.subplots(2,2,sharex='col',sharey='row')
	ax1.plot(x,y)
	ax1.set_title('Sharing x on column and y on row')
	ax2.scatter(x,y)
	ax3.scatter(x,2*y**2.-1,color='r') 
	ax4.scatter(x,2*y**2.-1,color='r') 

	plt.show()


one()
two()

"""
Traceback (most recent call last):
  File "plotting_multiple.py", line 69, in <module>
    two()
  File "plotting_multiple.py", line 36, in two
    ax.plot(x,y)
AttributeError: 'numpy.ndarray' object has no attribute 'plot'
"""








