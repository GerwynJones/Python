# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 09:11:38 2016

@author: Admin
"""

from __future__ import division
import numpy as np 
import matplotlib.pyplot as plt

def Verp(ovel,opos,dt,a):
    "Position:"
    pos = opos + ovel*dt + .5*a*dt**2
    return pos
    
def Verv(pos,mass,ovel,a):
     "Velocities:"
     vel = ovel + .5*(a + acc(pos,mass))*dt
     return vel

def acc(pos,mass):
    a = zeros((N,3))
    G = 6.67408*10**-11
    for i in range(0,N-1):
        for j in range(i+1,N):
            r = pos[i]-pos[j]
            m = np.linalg.norm(r)
            F = -(G/m**3)*r
            a[i] += F*mass[j]
            a[j] += -F*mass[i]
            
        return a

AU = 149597871000
Ms = 1.989*10**30
Me = 5.972*10**24
Ma = 6.39*10**23
AUa = 1.524*AU

"Defining Variables"
N = 3
t_max = 3.1556e7
dt = 100
steps = int(t_max/dt)

v = (2*np.pi*AU)/t_max

mass = array([Ms,Me,Ma])
pos = zeros((N,3))
vel = zeros((N,3))

pos[1] = array([0,AU,0.5*AU])
pos[2] = array([0,-AUa,0])
vel[1] = array([v,0,0])
vel[2] = array([-24000,0,2000])
ind = 0

s = []
e = []
ma = []

for i in range(0,steps):
    print(i/steps*100)
    a = acc(pos,mass)

    "Verlet Method"

    opos = pos
    ovel = vel

    pos = Verp(ovel,opos,dt,a)
    vel = Verv(pos,mass,ovel,a)
    
    """dump pos into file"""
    s.append(pos[:][0])
    e.append(pos[:][1])
    ma.append(pos[:][2])    


