#!/usr/bin/python3

from PIL import Image

from matplotlib import pyplot as plt

import numpy as np


def create_img_size(width=100,height=100):
	img = Image.new('RGB',(width,height))
	
	
	
def create_img_from_pixels(rgb=[[[0,0,0],[0,0,0],[0,0,0],[1,1,1],[1,1,1],[1,1,1]],[[0,0,0],[0,0,0],[0,0,0],[1,1,1],[1,1,1],[1,1,1]]]):
	# input rgb: [[r1,g1,b1],[r2,g2,b2],...]
	
	rgb = np.array(rgb)
	
	new_image = Image.fromarray(rgb)
	return new_image

def create_img_rand(width,height):

	array = np.random.random_integers(0,255,(width,height,3))
	
	return Image.fromarray(np.array(array,dtype=np.uint8))
	

def read_img(file_):
	return Image.open(file_)




def matplotlib_make_img():

	image = [[[0,0,0],[0,255,0],[0,0,0]],[[255,0,0],[0,0,0],[0,0,255]],[[0,0,0],[255,0,255],[0,0,0]]]

	plt.imshow(image)

	plt.show()

def matplotlib_show_img():

	image = plt.imread('Screenshot from 2018-05-19 16-57-11.png')
	
	plt.imshow(image)

	plt.show()



def __main__():
	
	matplotlib_make_img()

	matplotlib_show_img()


__main__()

