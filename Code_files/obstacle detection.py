# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:08:24 2020

@author: Paras

contour detection 

Add area threshold to consider into contour to remove noise

"""
import numpy as np 
import cv2 
from matplotlib import pyplot as plt 
from scipy.spatial import distance


cap = cv2.VideoCapture(0) 

try:
    while(1):
        _, frame = cap.read()
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # blur = cv2.GaussianBlur(gray,(1,1),1000)
        
        ret, thresh = cv2.threshold(gray, 50, 255,cv2.THRESH_BINARY_INV)
       
    #    _, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
    
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #    cnt = contours[0]
    #    M = cv2.moments(cnt)
    #    epsilon = 0.1*cv2.arcLength(cnt,True)
    #    approx = cv2.approxPolyDP(cnt,epsilon,True)
     
        for i in range(len(contours)):
            cnt = contours[i]
            
    #        epsilon = 0.8* cv2.arcLength(cnt, True)
    #        approx = cv2.approxPolyDP(cnt, epsilon, True)
    
            rect = cv2.minAreaRect(cnt)
           
            box = cv2.boxPoints(rect)
            print(box)
            box = np.int0(box)
            frame = cv2.drawContours(frame, [box] , -1, (0,255,0), 2)
#            frame = cv2.rectangle(frame,cnt,(0,0,255),2)
        
        
    #    cnt = contours[0]
    #    M = cv2.moments(cnt)
        cv2.imshow('frame', frame)
        cv2.imshow('thresh', thresh)
    
        k = cv2.waitKey(1)
        if k == 27:
            break
except Exception as E:
    print('ERROR OCCURED')
    print (E)
    
finally:
    cap.release()
    cv2.destroyAllWindows()

#image = cv2.imread('C:\\Users\\HP\\Desktop\\major proje ct\\obstacle course.png')
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow('gray',gray)
#
#ret,thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV)
#_, contours,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#
#for i in range(len(contours)):
#    cnt = contours[i]
#    rect = cv2.minAreaRect(cnt)  
#    box = cv2.boxPoints(rect)
#    print(box)
#    box = np.int0(box)
#    image = cv2.drawContours(image, [box] , -1, (0,255,0), 2)        
#    image1 = cv2.drawContours(image, cnt , -1, (0,255,0), 2)        
#
#
#cv2.imshow('image',image)
#
#cv2.waitKey(0)
#cv2.destroyAllWindows()