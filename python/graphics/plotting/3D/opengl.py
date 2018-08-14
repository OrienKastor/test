#!/usr/bin/python3

### 3D GLUT display
##
###import OpenGL
##from OpenGL.GL import *
##from OpenGL.GLU import *
##from OpenGL.GLUT import *
##import sys
##
##
##def init3D(Width=620,Height=480,r=0.0,g=0.0,b=0.0,alpha=0.0):
##	glClearColor(0.0, 0.0, 0.0, 0.0)  
##	glClearDepth(1.0)
##	glDepthFunc(GL_LESS)			  
##	glEnable(GL_DEPTH_TEST)		   
##	glShadeModel(GL_SMOOTH)		   
##	glMatrixMode(GL_PROJECTION)
##	glLoadIdentity()				  
##	gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
##	
##	glMatrixMode(GL_MODELVIEW)
##
##
##
##def display():
##		
##	rect([[2,-2,0],[2,2,0],[-2,2,0],[-2,-2,0]])
##
##
##	
##def rect(pts):
##	
##	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
##
##	glBegin(GL_QUADS)
##	glColor3f(1.0,0.0,0.0)
##	
##	for pt in pts:
##		glVertex3f(pt[0],pt[1],pt[2])
##	glEnd()
##
##
##
##def __main__():
##	global window
##	glutInit(sys.argv)
##
##	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
##	glutInitWindowSize(640,480)
##	glutInitWindowPosition(0,0)
##	window = glutCreateWindow("Hello World :'D")
##	
##	glutDisplayFunc(display)
##	glutIdleFunc(display)
##
##	init3D()
##
##	glutMainLoop()
##
##
##
##__main__()


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

ESCAPE = '\033'

window = 0
rtri = 0.0

def InitGL(Width, Height):			 
	glClearColor(0.0, 0.0, 0.0, 0.0)  
	glClearDepth(1.0)				 
	glDepthFunc(GL_LESS)			  
	#glEnable(GL_DEPTH_TEST)		   
	glShadeModel(GL_SMOOTH)		   
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()				  
	gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

	glMatrixMode(GL_MODELVIEW)

def ReSizeGLScene(Width, Height):
	if Height == 0:	   
		Height = 1

	glViewport(0, 0, Width, Height)	 
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
	glMatrixMode(GL_MODELVIEW)

def DrawGLScene():
	global rtri, rquad

	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)   
	glLoadIdentity()				   

	glTranslatef(0.0,0.0,-6.0)			

	#glPushMatrix();
	glBegin(GL_TRIANGLES)				 
	glColor3f(1.0,0.0,0.0)		   
	glVertex3f(0.0, 1.0, 0.0)		
	glColor3f(0.0,0.0,1.0)		   
	glVertex3f(-1.0,-1.0,0.0)		
	glColor3f(0.0,1.0,0.0)		   
	glVertex3f(1.0,-1.0, 1.0)		
	glEnd()
	#glPopMatrix();

	glutSwapBuffers()

def keyPressed(*args):
	if args[0] == ESCAPE:
		sys.exit()

def main():
	#global window
	glutInit(sys.argv)

	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
	glutInitWindowSize(640, 480)
	glutInitWindowPosition(0, 0)
	#window = glutCreateWindow("Python OpenGL Triangle")
	glutCreateWindow("Python OpenGL Triangle")

	# Altering the DrawGLScene, or the things between glutInit and glutMainLoop; that's what happens with glut and that's how an animation can occur
	glutDisplayFunc(DrawGLScene)
	glutIdleFunc(DrawGLScene)

	glutReshapeFunc(ReSizeGLScene)
	glutKeyboardFunc(keyPressed)
	InitGL(640, 480)
	glutMainLoop()

print("Hit ESC key to quit.")
main()


