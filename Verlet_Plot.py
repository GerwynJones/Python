# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 22:59:34 2016

@author: Admin
"""
from __future__ import division
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from Verlet_main import *

plt.close('all')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.plot(A[:,0],A[:,1],A[:,2],'o'); plt.plot(B[:,0],B[:,1],B[:,2]) #; plt.plot(C[:,0],C[:,1],C[:,2])

plt.figure()
plt.plot(T, Ea/Esum, color = 'blue'), plt.plot(T, Eb/Esum, color = 'red'); plt.plot(T, ((Ea/Esum)+(Eb/Esum)), color = 'black') #; plt.plot(T, Ec/Esum, color = 'green')

fig = plt.figure()
plt.plot(A[:,0],A[:,1], 'o'); plt.plot(B[:,0],B[:,1], 'o') #; plt.plot(C[:,0],C[:,1])
plt.savefig('Graph of Ecc_.png', bbox_inches='tight') 

#plt.xlim(-6e14,6e14); plt.ylim(-6e14,6e14)

plt.figure()
plt.plot(T, acceleration[:,1])

plt.show()


T_max = np.max(dT)
T_min = np.min(dT)
T_Ratio = T_max/T_min

acc_min = np.min(acceleration[:,1])
acc_max = np.max(acceleration[:,1])