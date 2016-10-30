# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 09:11:38 2016

@author: Admin
"""

from __future__ import division
import numpy as np 
import matplotlib.pyplot as plt

N = 3

t = 3.1557e7; dt = t/360
n = int(t/dt)

G = 6.67e-11
Ms = 1.989e30
Me = 5.972e24
M = np.array([Ms,Me,3*Me])
AU = 1.496e11
e = 0.05*AU
v = (2*np.pi*AU)/t

ipy = np.array([0,AU,3*AU])
ivx = np.array([0,v,2*v])

vx = np.zeros((n,N))
vy = np.zeros((n,N))
px = np.zeros((n,N))
py = np.zeros((n,N))

py[0] = ipy
vx[0] = ivx

#a = np.zeros((N,2))

for i in range(1,n):
    print((i/n)*100,"%")
    a = np.zeros((N,2))

    for j in range(N):
        for k in range(N):
            if j != k:
                x = px[i-1,k]-px[i-1,j]
                y = py[i-1,k]-py[i-1,j]
                r = np.array([x,y])
                c = -G/((x**2 + y**2)+e)**(3/2)
                a[j,:] =+ c*M[k]*r
                a[k,:] =+ c*M[j]*r


               
    for j in range(N):

        "Velocities:"
        vx[i,j] = vx[i-1,j] + dt*a[j,0]
        vy[i,j] = vy[i-1,j] + dt*a[j,1]        
        "Position:"
        px[i,j] = px[i-1,j] + dt*vx[i,j]
        py[i,j] = py[i-1,j] + dt*vy[i,j]
#        
#        px[i,j] = px[i-1,j] + dt*vx[i-1,j] + .5*(ax[j])*(dt*dt)
#        py[i,j] = py[i-1,j] + dt*vy[i-1,j] + .5*(ay[j])*(dt*dt)
#
#        vx[i,j] = vx[i-1,j] + .5*(c*ax[j] + ax[j])*dt
#        vy[i,j] = vy[i-1,j] + + .5*(c*ay[j] + ay[j])*dt
#
#    "Position:"
#    e_x[i] = e_x[i-1] + dt*e_vx[i-1] + .5*(a*e_x[i-1])*(dt*dt)
#    e_y[i] = e_y[i-1] + dt*e_vy[i-1] + .5*(a*e_x[i-1])*(dt*dt)
#    "Velocities:"
#    e_vx[i] = e_vx[i-1] + .5*(a*(e_x[i-1] + e_x[i]))*dt
#    e_vy[i] = e_vy[i-1] + + .5*(a*(e_y[i-1] + e_y[i]))*dt

        
fig = plt.figure()
ax1 = fig.add_subplot(111)  
ax1.plot(px,py)



        
            
            
    