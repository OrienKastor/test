#!/usr/bin/python3

# GENERATE OpenGL 3D STRUCTURES AND DISPLAY IT IN A pygame WINDOW


import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import numpy as np

from math import sin, cos, pi


# Lines:

# Cubes:

# Sphere:

# 




# make a line:
def line(pos1,pos2):
	# glBegin(GL_LINES)
	# glVertex3fv(pt1)
	# glVertex3fv(pt2)
	# glVertex3fv(pt...)
	# ...
	# glEnd()
	glBegin(GL_LINES)
	glVertex3fv(pos1)
	glVertex3fv(pos2)
#	glVertex3fv(line2_start)
#	glVertex3fv(line2_end)
#	glVertex3fv(line3_start)
#	glVertex3fv(line3_end)
	glEnd()

# make a cube:
def rect_prism(center=[0,0,0],x=1.,y=1.,z=1.,alpha=0.,theta=0.):
	# theta is the angle in the x-z plane -> first angle done
	# alpha is the angle in the x-y plane -> second angle done
	theta = theta*pi/180.
	alpha = alpha*pi/180.
	center = np.array(center)
	center_bottom = center + z/2.*np.array([sin(theta)*cos(alpha),sin(alpha),cos(theta)])
	center_top = center - z/2.*np.array([sin(theta)*cos(alpha),sin(alpha),cos(theta)])

	pt1 = center_bottom + ((x/2.)**2.+(y/2.)**2.)**0.5 * np.array([cos(theta)*cos(alpha-pi/4.),cos(theta)*sin(alpha-pi/4.),sin(theta)*cos(alpha-pi/4.)])
	pt2 = center_bottom + ((x/2.)**2.+(y/2.)**2.)**0.5 * np.array([cos(theta)*cos(alpha-pi/4.+pi/2.),cos(theta)*sin(alpha-pi/4.+pi/2.),sin(theta)*cos(alpha-pi/4.+pi/2.)])
	pt3 = center_bottom + ((x/2.)**2.+(y/2.)**2.)**0.5 * np.array([cos(theta)*cos(alpha-pi/4.+pi/2.+pi/2.),cos(theta)*sin(alpha-pi/4.+pi/2.+pi/2.),sin(theta)*cos(alpha-pi/4.+pi/2.+pi/2.)])
	pt4 = center_bottom + ((x/2.)**2.+(y/2.)**2.)**0.5 * np.array([cos(theta)*cos(alpha-pi/4.+pi/2.+pi/2.+pi/2.),cos(theta)*sin(alpha-pi/4.+pi/2.+pi/2.+pi/2.),sin(theta)*cos(alpha-pi/4.+pi/2.+pi/2.+pi/2.)])


	pt1_2 = center_top + ((x/2.)**2.+(y/2.)**2.)**0.5 * np.array([cos(theta)*cos(alpha-pi/4.),cos(theta)*sin(alpha-pi/4.),sin(theta)*cos(alpha-pi/4.)])
	pt2_2 = center_top + ((x/2.)**2.+(y/2.)**2.)**0.5 * np.array([cos(theta)*cos(alpha-pi/4.+pi/2.),cos(theta)*sin(alpha-pi/4.+pi/2.),sin(theta)*cos(alpha-pi/4.+pi/2.)])
	pt3_2 = center_top + ((x/2.)**2.+(y/2.)**2.)**0.5 * np.array([cos(theta)*cos(alpha-pi/4.+pi/2.+pi/2.),cos(theta)*sin(alpha-pi/4.+pi/2.+pi/2.),sin(theta)*cos(alpha-pi/4.+pi/2.+pi/2.)])
	pt4_2 = center_top + ((x/2.)**2.+(y/2.)**2.)**0.5 * np.array([cos(theta)*cos(alpha-pi/4.+pi/2.+pi/2.+pi/2.),cos(theta)*sin(alpha-pi/4.+pi/2.+pi/2.+pi/2.),sin(theta)*cos(alpha-pi/4.+pi/2.+pi/2.+pi/2.)])



	
	glBegin(GL_LINES)

	glVertex3fv(center)
	glVertex3fv(center_top)
	glVertex3fv(center)
	glVertex3fv(center_bottom)

	glVertex3fv(pt1)
	glVertex3fv(pt2)
	glVertex3fv(pt2)
	glVertex3fv(pt3)
	glVertex3fv(pt3)
	glVertex3fv(pt4)
	glVertex3fv(pt4)
	glVertex3fv(pt1)

	glVertex3fv(pt1_2)
	glVertex3fv(pt2_2)
	glVertex3fv(pt2_2)
	glVertex3fv(pt3_2)
	glVertex3fv(pt3_2)
	glVertex3fv(pt4_2)
	glVertex3fv(pt4_2)
	glVertex3fv(pt1_2)
	
	glVertex3fv(pt1)
	glVertex3fv(pt1_2)
	glVertex3fv(pt2)
	glVertex3fv(pt2_2)
	glVertex3fv(pt3)
	glVertex3fv(pt3_2)
	glVertex3fv(pt4)
	glVertex3fv(pt4_2)

#	print("center"+str(center))
#	print("center_bottom"+str(center_bottom))
	glEnd()


def tri_c(color,triangle):
	# color: [r,g,b] (i think, check if it's this or bgr)
	# triangle: [[x1,y1,z1],[x2,y2,z2],[x3,y3,z3]]
	
	glBegin(GL_TRIANGLES)
	glColor3fv(color)
	glVertex3fv(triangle[0])
	glVertex3fv(triangle[1])
	glVertex3fv(triangle[2])
	glEnd()


def __main__():
	pygame.init()
	display = (800,600)
	pygame.display.set_mode(display,DOUBLEBUF|OPENGL)
	
	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0) # sets up an orientation  the following: 
	#           ||
	#           ||
	#           \/ +y
	#
	#           (x) z (z goes into the window)
	#           
	#           <===== +x

	
	glTranslatef(0.0,0.0,-5) # translates the position of the window by (x,y,z)
	
	theta = 0
	alpha = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		
		#line([-1,-1,-1],[1,1,1])
		theta=theta+.1
		rect_prism([0,0,0],1.4,1.4,3.4,theta,0.)
		#tri_c([1.0,0.,1.],[[1,1,-1],[1,1,1],[1,-1,1]])
		
		try:
			pygame.display.flip()
		except:
			print("Exiting now. Thank you!")
			return None
		
		pygame.time.wait(10) # wait this many milliseconds
		
		
		# rotate the image
		#glRotatef(1,1,1,0)


__main__()





