# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 22:59:34 2016

@author: Admin
"""
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from Verlet_main import a0, b0, c0, Ta, Tb, Tc, Tsum, T

plt.close('all')

a = np.zeros((len(a0),3))
b = np.zeros((len(b0),3))
#c = np.zeros((len(c0),3))

for i in range (0,len(a0)):
    a[i] = a0[i]
    b[i] = b0[i]
#    c[i] = c0[i]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.plot(a[:,0],a[:,1],a[:,2]); plt.plot(b[:,0],b[:,1],b[:,2]) # ; plt.plot(c[:,0],c[:,1],c[:,2])

plt.figure()
plt.plot(T, Ta), plt.plot(T, Tb); plt.plot(T, Tsum) # ; plt.plot(Tc)

fig = plt.figure()
plt.plot(a[:,0],a[:,1], 'o'); plt.plot(b[:,0],b[:,1], 'o') # ; plt.plot(c[:,0],c[:,1])
plt.savefig('Graph of eccentric orbit.png', bbox_inches='tight') 

plt.show()