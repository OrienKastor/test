#!/usr/bin/python3

import pyautogui

pyautogui.size()

pyautogui.position()

pyautogui.moveTo(pyautogui.size()[0]/2.,pyautogui.size()[1]/2.,duration=0.0)
pyautogui.moveRel(100,100,duration=.3)
pyautogui.dragRel(100,100,duration=.3)
