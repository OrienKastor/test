#!/usr/bin/python3


# GENERATE OpenGL 2D STRUCTURES AND DISPLAY IT IN A pygame WINDOW

import OpenGL

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *



def init2D(r=0.0,g=0.0,b=0.0,alpha=0.0):
	glClearColor(r,g,b,alpha)
	glMatrixMode(GL_PROJECTION)
	gluOrtho2D(0.0,200.0,0.0,150.)



def display():
	#glClear(GL_COLOR_BUFFER_BIT)
	
	#glColor3f(1.0,0.0,0.0)
	
	# draw 2 points
	points([[10,110],[15,110],[20,110]])
	#point([1,-1])
#	glBegin(GL_POINTS)
#	for i in range(0,10):
#		glVertex2i(10+5*i,110)
#	glEnd()
#
	# draw line
	lines([[10,10],[100,100]])
	#glBegin(GL_LINES)
	#glVertex2i(10,10)
	#glVertex2i(100,100)
	#glEnd()
	
	glFlush()



def points(pts,rgb=[1.0,0,0]):
	# can either be given [pt1,pt2,pt3,...] or pt1

	#glClear(GL_COLOR_BUFFER_BIT)

	glColor3f(rgb[0],rgb[1],rgb[2])

	glBegin(GL_POINTS)

	try: 
		pts[0][0]
		for pt in pts:
			glVertex2i(int(pt[0]),int(pt[1]))
	except:
		glVertex2i(int(pts[0]),int(pts[1]))

	glEnd()

	#glFlush()



def lines(ls,rgb=[1.0,0,0]):
	# can either be [[pt1,pt2],[pt3,pt4],[pt5,pt6],...] or [pt1,pt2]
	# where: pt1 = [x1,y1], pt2 = [x2,y2]

	#glClear(GL_COLOR_BUFFER_BIT)
	
	glColor3f(rgb[0],rgb[1],rgb[2])

	glBegin(GL_LINES)

	try:
		ls[0][0][0]
		for l in ls:
			glVertex2i(int(l[0][0]),int(l[0][0]))
			glVertex2i(int(l[1][0]),int(l[1][1]))
	except:
		glVertex2i(int(ls[0][0]),int(ls[0][1]))
		glVertex2i(int(ls[1][0]),int(ls[1][1]))
	
	glEnd()

	#glFlush()



def __main__():
	glutInit(sys.argv)
	glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize (500, 500)
	glutInitWindowPosition (100, 100)
	glutCreateWindow ('points and lines')
	init2D(0.0,0.0,0.0)
	glutDisplayFunc(display)
	glutMainLoop()

__main__()
