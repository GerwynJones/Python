# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 09:11:38 2016

@author: Admin
"""

from __future__ import division
import numpy as np 
import matplotlib.pyplot as plt

N = 2

t = 3.1556e7; dt = t/360
n = int(t/dt)

G = 6.67e-11
Ms = 1.989e30
Me = 5.972e24
M = np.array([Ms,Me])
AU = 149597871000
e = 0.05*AU

ip = np.array([1,AU])
iv = np.array([30000,0])

vx = np.zeros((n,N))
vy = np.zeros((n,N))
px = np.zeros((n,N))
py = np.zeros((n,N))

py[0] = ip
vx[0,1] = iv[0]

ax = np.zeros((N,N))
ay = np.zeros((N,N))


for j in range(N-1):
    for k in range(j+1,N):
        x = px[k]-px[j]
        y = py[k]-py[j]
        c = -G/((x**2 + y**2)+e)**(3/2)
        ax[j] =+ c*M[k]*x
        ay[j] =+ c*M[k]*y
        ax[k] =+ -c*M[j]*x
        ay[k] =+ -c*M[j]*y

            
for j in range(N):
    for i in range(1,n):
        "Velocities:"
        vx[i,j] = vx[i-1,j] + dt*ax[j]
        vy[i,j] = vy[i-1,j] + dt*ay[j]        
        "Position:"
        px[i,j] = px[i-1,j] + dt*vx[i-1,j]
        py[i,j] = py[i-1,j] + dt*vy[i-1,j]
        
#        e_x[i] = e_x[i-1] + dt*e_vx[i-1] + .5*(a*e_x[i-1])*(dt*dt)
#        e_y[i] = e_y[i-1] + dt*e_vy[i-1] + .5*(a*e_x[i-1])*(dt*dt)
#        "Velocities:"
#        e_vx[i] = e_vx[i-1] + .5*(a*(e_x[i-1] + e_x[i]))*dt
#        e_vy[i] = e_vy[i-1] + + .5*(a*(e_y[i-1] + e_y[i]))*dt



        
            
            
    