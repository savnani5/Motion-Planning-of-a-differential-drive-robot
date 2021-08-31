# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 12:00:49 2020
@author: Paras
Pygame simulation

"""
import cv2
import numpy as np
import pygame
import sys
import math
import time
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


def robot(robot_image,x, y,angle):
    orig_rect = robot_image.get_rect()
    rot_image = pygame.transform.rotate(robot_image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    
    # To update pos of the robot
    screen.blit(rot_image, (x, y))

def get_angle(sp, i):
   s = math.atan2(sp[i+1][1]-sp[i][1], sp[i+1][0]-sp[i][0])
   angle = -s*180/math.pi
   # angle = round(angle,2)
   return angle 
        
def drive(sp, i):
    global angle_change 
    global x_change
    global y_change
    angle_change = 1
    x_change = (sp[i+1][0]-sp[i][0])/5
    y_change = (sp[i+1][1]-sp[i][1])/5
    x_distance = sp[i+1][0]-sp[i][0]
    y_distance = sp[i+1][1]-sp[i][1]
    return angle_change, x_change, y_change, x_distance, y_distance        

def spline_fit(sp):
    x = []
    y = []
    nsp = []
    for i in range(len(sp)):
        x.append(sp[i][0])
        y.append(sp[i][1])

    f1 = interp1d(x, y, kind ='linear')
    f2 = interp1d(x, y, kind='quadratic')
    
    xnew = np.linspace(sp[0][0], sp[-1][0], num=100, endpoint=True)
    
    for (i,j) in zip(xnew, f2(xnew)):
        i = round(i, 3)
        j = round(j, 3)
        nsp.append((i,j))
    
    return nsp
#__________________________________________________________
    
pygame.init()
img = 'obstacle course3.png'
image = cv2.imread(img)
rows, cols, _ = image.shape

sp =  [(81, 350), (118, 350), (317, 224), (526, 100), (601, 85), (765, 49)] #[(76, 397), (233, 382), (508, 228), (630, 78), (639, 42)]

sp = spline_fit(sp)

screen = pygame.display.set_mode((cols, rows))
screen.fill((0,0,0))
# pixarr = pygame.PixelArray(screen)
# pixarr[30][50] = (255,255,255)
course = pygame.image.load(img)

# Robot Variables
robot_image = pygame.image.load('car.png')
size = (40, 40)
robot_image = pygame.transform.scale(robot_image, size)

## Starting parameters
x = sp[0][0]- size[0]/2
y = sp[0][1]- size[1]/2
angle = 0 
final_angle = get_angle(sp, 0)
angle_change, x_change, y_change, x_distance, y_distance = drive(sp, 0)

time.sleep(2)

## Simulation Loop
while True:    
    
    screen.blit(course, (0, 0))
    
    # End Condition
    if x >= (sp[0][0] - size[0]/2) + sp[-1][0]- sp[0][0]:
        x = (sp[0][0] - size[0]/2) + sp[-1][0]- sp[0][0]
        y = (sp[0][1]- size[1]/2) +  sp[-1][1]- sp[0][1]
    
    for e in range(len(sp)-1):
        pygame.draw.line(screen, (0, 0, 255), sp[e], sp[e+1], 2)
        
    for i in range(len(sp)-1):
        if x < sp[i+1][0] - size[0]/2:
            break
                             
    final_angle = get_angle(sp, i)
    # print(final_angle)
    angle_change, x_change, y_change, x_distance, y_distance = drive(sp, i)
    
## Angle Rotation and drive translation
        
    if angle != final_angle:
        if abs(final_angle - angle) >= 1:
            if angle < final_angle:
                angle += angle_change
            else:
                angle -= angle_change
                    
        else:
            if angle < final_angle:
                angle += (final_angle - angle)
            else:
                angle -= (angle- final_angle)
    else:
        if x_change > 0:  
            x += x_change 
        else:
            x -= x_change
        if y_change > 0:  
            y -= y_change 
        else:
            y += y_change    
     
    robot(robot_image, x, y, angle)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    time.sleep(0.01)    
    pygame.display.update()
        
