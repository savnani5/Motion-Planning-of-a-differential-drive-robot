# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 16:19:03 2020

@author: Paras


import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 1000)
f = np.arange(0, 1000)
g = np.arange(750,-250,-1)
h = np.arange(750, 0,-1)
#j = np.arange(450,250,-1)
#g = np.sin(np.arange(0, 10, 0.01) * 2) * 1000

plt.plot(x, f, '-')
plt.plot(x, h, '-')
plt.plot(x, g, '-')
#plt.plot(h, g, '-')

idx = np.argwhere(np.diff(np.sign(x - g))).flatten()
print(idx)
plt.plot(x[idx], g[idx], 'ro')
plt.show()
"""
from shapely import geometry
import time

start_time = time.time()

line1 = geometry.LineString([(0,0), (50,50)])
line2 = geometry.LineString([(50,10), (30,30)])


x = str(line1.intersection(line2))

print(type(x))
print(line1.intersection(line2))

if 'POINT' in x: 
    print('hi')
counter = 0
while True:
    counter = counter + 1
    if counter == 5500000:
        break
    
print(time.time()-start_time)

