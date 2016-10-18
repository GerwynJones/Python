# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 09:11:38 2016

@author: Admin
"""

from __future__ import division
import numpy as np 
import matplotlib.pyplot as plt

N = 2

t = 100; dt = 0.1
n = int(t/dt)

G = 6.67e-11
M = np.ones(N)
AU = 149597871000

ip = np.array([0,AU])
iv = np.array([30000,0])

vx = np.zeros((n,N))
vy = np.zeros((n,N))
px = np.zeros((n,N))
py = np.zeros((n,N))

py[0,1] = ip[1]
vx[0,1] = iv[0]


ax = np.zeros((n,N))
ay = np.zeros((n,N))

for i in range(1,n):
    for j in range(N-1):
        for k in range(j+1,N):
            x = px[j]-px[k]
            y = py[j]-py[k]
            c = -G/(x**2 + y**2)**(3/2)
            ax[j] = ax[j] + c*M[k]*x
            ax[k] = ax[k] - c*M[j]*x
            ay[j] = ay[j] + c*M[k]*y
            ay[k] = ay[k] - c*M[j]*y
            
    for j in range(N):
        "Velocities:"
        vx[i,j] = vx[j-1] + dt*ax[j-1,]
        vy[i,j] = vy[j-1] + dt*ay[j-1,i]        
        "Position:"
        px[i,j] = px[i-1,j] + dt*vx[i-1,j]
        py[i,j] = py[i-1,j] + dt*vy[i-1,j]



        
            
            
    