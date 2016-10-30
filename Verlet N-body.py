# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 09:11:38 2016

@author: Admin
"""

from __future__ import division
import numpy as np 
import matplotlib.pyplot as plt
from numpy import linalg as LA
from mpl_toolkits.mplot3d import Axes3D


def Verp(ovel, opos, dt, a):
    "Position:"
    pos = opos + ovel*dt + .5*a*dt**2
    return pos
    
def Verv(pos, mass, ovel, a, e):
     "Velocities:"
     an, pe, ke = acc(pos, mass, ovel, e)
     vel = ovel + .5*(a + an)*dt
     return vel

def acc(pos, mass, vel, e):
    
    a = np.zeros((N,3))
    pe = np.zeros((N,1))
    ke = np.zeros((N,1))
    
    G = 6.67408*10**-11
    
    for i in range(0,N-1):
        for j in range(i+1,N):
            vi = LA.norm(vel[i]) 
            vj = LA.norm(vel[j])
            
            r = pos[i]-pos[j]
            m = LA.norm(r)
            F = -(G/(m+e)**3)*r
            
            a[i] += F*mass[j]
            a[j] += -F*mass[i]
            pe[i] += (G*mass[i]*mass[j])/(m+e)
            pe[j] += (G*mass[j]*mass[i])/(m+e)
            ke[i] += .5*mass[i]*vi**2
            ke[j] += .5*mass[j]*vj**2
            
        return a, pe, ke

AU = 149597871000
Ms = 1.989*10**30
Me = 5.972*10**24
Ma = 6.39*10**23
AUa = 1.524*AU

"Defining Variables"
N = 3
t_max = 3.1556e7
dt = 100
steps = int(2*t_max/dt)

v = (2*np.pi*AU)/t_max

mass = np.array([Ms,Me,Ma])
pos = np.zeros((N,3))
vel = np.zeros((N,3))

pos[1] = np.array([0,0.33*AU,0.05*AU])
pos[2] = np.array([0,0.3*AUa,0])
vel[1] = np.array([v,0,0])
vel[2] = np.array([24000,0,0])
e = 0.05*AU

a0 = []; Ta = []
b0 = []; Tb = []
c0 = []; Tc = []

for i in range(0,steps):
#    print(i/steps*100)
    a, pe, ke = acc(pos, mass, vel, e)

    "Verlet Method"
    opos = pos
    ovel = vel

    pos = Verp(ovel, opos, dt, a)
    vel = Verv(pos, mass, ovel, a, e)
    
    """dump pos into file"""
    a0.append(pos[0])
    b0.append(pos[1])
    c0.append(pos[2])    
    """dump energies into file"""
    Ta.append(pe[0] - ke[0])
    Tb.append(pe[1] - ke[1])
    Tc.append(pe[2] - ke[2]) 


a = np.zeros((steps,3))
b = np.zeros((steps,3))
c = np.zeros((steps,3))

for i in range (0,steps):
    a[i] = a0[i]
    b[i] = b0[i]
    c[i] = c0[i]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.plot(a[:,0],a[:,1],a[:,2]); plt.plot(b[:,0],b[:,1],b[:,2]); plt.plot(c[:,0],c[:,1],c[:,2])

figure()
plt.plot(Ta), plt.plot(Tb); plt.plot(Tc)