# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 22:22:15 2016

@author: patri
"""
from numpy.linalg import norm
from numpy import zeros, array
from matplotlib.pyplot import plot


AU = 149597871000
Ms = 1.989*10**30
Me = 5.972*10**24
Ma = 6.39*10**23
AUa = 1.524*AU

"Defining Variables"
N = 3
t_max = 2*687*24*60*60
dt = 1000
steps = 1
G = 6.67408*10**-11
mass = array([Me,Ms,Ma])
pos = zeros((N,3*(steps+1)))
vel = zeros((N,3))
pos[0][0:3] = array([0,AU,0])
pos[2][0:3] = array([0,-AUa,0])
vel[0][0:3] = array([30000,0,0])
vel[2][0:3] = array([-24000,0,0])
ind = 0

"Forces"
for o in range(0,steps):
    a = zeros((N,3))
    for i in range(0,N-1):
        for j in range(i+1,N):
            r = norm(pos[i][ind:ind+3]-pos[j][ind:ind+3])
            F = -G/r**3*(pos[i][ind:ind+3]-pos[j][ind:ind+3])
            a[i] += F*mass[j]
            a[j] += -F*mass[i]
    "Euler's Method"
    ind+=3
    for i in range(0,N):
        "Position:"
        pos[i][ind:ind+3] = pos[i][ind-3:ind] + dt*vel[i]
        "Velocities:"
        vel[i] += dt*a[i]

for i in range(0,N):
    plot(pos[i][::3],pos[i][1::3])
