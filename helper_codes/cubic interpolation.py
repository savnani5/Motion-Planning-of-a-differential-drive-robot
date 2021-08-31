# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 17:36:38 2020

@author: Paras

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

sp = [(81, 350), (118, 350), (317, 224), (526, 100), (601, 85), (765, 49)]

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

print(nsp)
plt.plot(x, y, 'o', xnew, f1(xnew), '-', xnew, f2(xnew), '--')
plt.legend(['data', 'linear', 'quadratic'], loc='best')
plt.show()

