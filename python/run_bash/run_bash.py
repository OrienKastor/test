#!/usr/bin/python3
import os
import sh


def __main__():
	os.system('echo "Hello"')
	
	os.popen('echo "Hello"')
	
	os.Popen('echo "Hello World!"')
	
	sh.cd ('') # execute shell commands as native python functions

__main__()

