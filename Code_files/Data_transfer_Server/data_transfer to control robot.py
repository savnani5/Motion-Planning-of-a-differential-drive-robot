# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 15:02:42 2020

@author: Paras


Data transfer using wifi

"""
import socket               
import pygame
import sys

sock = socket.socket()
 
host = "192.168.137.189" #ESP32 IP in local network
port = 80             #ESP32 Server Port    
 
sock.connect((host, port))

#initialize the pygame
pygame.init()

# sets the window title
pygame.display.set_caption(u'Robot Control')

# sets the window size
pygame.display.set_mode((400, 400))

# infinite loop
while True:
    # gets a single event from the event queue
    event = pygame.event.wait()

    # if the 'close' button of the window is pressed
    if event.type == pygame.QUIT:
        # stops the application
        break

    # captures the 'KEYDOWN' and 'KEYUP' events
    if event.type in (pygame.KEYDOWN, pygame.KEYUP):
        # gets the key name
        key_name = pygame.key.name(event.key)

        # converts to uppercase the key name
        #key_name = key_name.upper()

        # if any key is pressed
        if event.type == pygame.KEYDOWN:
            # prints on the console the key pressed
            print (u'"{}" key pressed'.format(key_name))
            message = key_name.encode()
            sock.send(message)
        # if any key is released
        elif event.type == pygame.KEYUP:
            # prints on the console the released key
            print (u'"{}" key released'.format(key_name))
            message = 'k'.encode()
            sock.send(message)

# finalizes Pygame
pygame.quit() 
sock.close()
sys.exit() 