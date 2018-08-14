#!/usr/bin/python3

import sys, pyautogui, time
import numpy as np
import math


def draw_circle2(center=[1080/2.,960/2.],r=100,step=5):
    # x**2 + y**2 = r**2
    
    # Draw bottom hemisphere
    pyautogui.moveTo(center[0]-r,0)
    for x in range(-r,r+step,step):
        y = (r**2.-x**2.)**0.5
        pyautogui.dragTo(center[0]+x,center[1]+y,duration=0.001)
    
    # Draw upper hemisphere
    pyautogui.moveTo(center[0]-r,0)
    for x in range(-r,r+step,step):
        y = -(r**2.-x**2.)**0.5
        pyautogui.dragTo(center[0]+x,center[1]+y,duration=0.001)


def draw_circle(center=[1080/2.,960/2.],r=100,step=5):
    # x**2 + y**2 = r**2
    
    # Start at angle of 0
    
    pyautogui.moveTo(center[0],center[1]+r)
    for theta in range(0,360+step,step):
        x = center[0]+r*math.sin(theta*math.pi/180.)
        y = center[1]+r*math.cos(theta*math.pi/180.)
        pyautogui.dragTo(x,y,duration=0.001)

        
def draw_rect(pos,height=100,width=100,angle=0):
    # position of top left corner, height, width, angle in deg

    angle = angle*math.pi/180.
    
    pos1 = pos
    pos2 = [pos1[0]+width*math.cos(angle),pos1[1]+width*math.sin(angle)]
    pos3 = [pos2[0]+height*math.sin(angle),pos2[1]-height*math.cos(angle)]
    pos4 = [pos1[0]+height*math.sin(angle),pos1[1]-height*math.cos(angle)]
    
    pyautogui.moveTo(pos1)
    pyautogui.dragTo(pos2)
    pyautogui.dragTo(pos3)
    pyautogui.dragTo(pos4)
    pyautogui.dragTo(pos1)


def press(input_):
    for in_ in input_:
        pyautogui.press(in_)


def press_(input_):
    pyautogui.press(input_)


def hotkey(input_):
    print(input_)
    if len(input_)==3.:
        pyautogui.hotkey(input_[0],input_[1],input_[2])
    elif len(input_)==2.:
        pyautogui.hotkey(input_[0],input_[1])


def open_pinta():
    pyautogui.press('winleft')
    press('pinta')
    pyautogui.press('tab')
    pyautogui.press('return')
    
    
def delay(time_):
    # delay this many seconds
    init = time.time()
    while(time.time()-init<time_):
        None


def __main__():
    window_center = [pyautogui.size()[0]/2.,pyautogui.size()[1]/2.]
    
    open_pinta()
#    hotkey(['alt','tab'])
    
    # draw circle
    r = 100
    inc = 4
    delay(2.)
    draw_circle(window_center,r,inc)
    
#    # draw rectangle
#    pos = [700,600]
#    h = 100
#    w = 100
#    angle = 0
#    draw_rect(pos,h,w,angle)
#    
#    # draw rectangle
#    pos = [800,600]
#    h = 100
#    w = 100
#    angle = 0
#    draw_rect(pos,h,w,angle)

    # draw rectangle
    pos = [700,700]
    h = 100
    w = 100
    angle = 0
    draw_rect(pos,h,w,angle)
    
    # draw rectangle
    pos = [700,700]
    h = 100
    w = 100
    angle = 30
    draw_rect(pos,h,w,angle)
    
    # draw rectangle
    pos = [700,700]
    h = 100
    w = 100
    angle = 60
    draw_rect(pos,h,w,angle)
    
    # draw rectangle
    pos = [700,700]
    h = 100
    w = 100
    angle = 90
    draw_rect(pos,h,w,angle)
    
    # draw rectangle
    pos = [700,700]
    h = 100
    w = 100
    angle = 120
    draw_rect(pos,h,w,angle)
    
    # draw rectangle
    pos = [700,700]
    h = 100
    w = 100
    angle = 150
    draw_rect(pos,h,w,angle)
    
    # draw rectangle
    pos = [700,700]
    h = 100
    w = 100
    angle = 180
    draw_rect(pos,h,w,angle)
    
    # draw rectangle
    pos = [700,700]
    h = 100
    w = 100
    angle = 210
    draw_rect(pos,h,w,angle)
    
    # draw rectangle
    pos = [700,700]
    h = 100
    w = 100
    angle = 240
    draw_rect(pos,h,w,angle)
    
    # draw rectangle
    pos = [700,700]
    h = 100
    w = 100
    angle = 270
    draw_rect(pos,h,w,angle)
    
    # draw rectangle
    pos = [700,700]
    h = 100
    w = 100
    angle = 300
    draw_rect(pos,h,w,angle)
    
    # draw rectangle
    pos = [700,700]
    h = 100
    w = 100
    angle = 330
    draw_rect(pos,h,w,angle)


def __main__2():
    
    delay(4.)
    
    window_center = [pyautogui.size()[0]/2.,pyautogui.size()[1]/2.]
    
    pyautogui.hotkey('alt','tab')

    delay(0.5)
    
    pyautogui.moveTo(window_center[0]-100,window_center[1]+100)
    pyautogui.moveTo(window_center[0]+100,window_center[1]+100)
    pyautogui.moveTo(window_center[0]+100,window_center[1]-100)
    pyautogui.moveTo(window_center[0]-100,window_center[1]-100)


__main__()