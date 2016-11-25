#!/usr/bin/env python
"""
Created on Tue Oct 18 09:11:38 2016

@author: Admin
"""

from __future__ import division
import numpy as np 
from numpy import linalg as LA

from Verlet_IC_Ecc import N, n, e, t, t_max, dt_max, mass, pos, vel

#####################

a0 = []; Ta = []
b0 = []; Tb = []
c0 = []; Tc = []

Tsum = []

T = [] 

####################

def Verp(ovel, opos, dt, a):
    "Position:"
    pos = opos + ovel*dt + .5*a*dt**2
    return pos
    
def Verv(pos, mass, ovel, dt, a, e):
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
            F = (G/(m+e)**3)*r # check (m+e) part
            
            a[i] += -F*mass[j]
            a[j] += F*mass[i]
            pe[i] += -(G*mass[i]*mass[j])/(m+e) # Check PE
            pe[j] += (G*mass[j]*mass[i])/(m+e)
            ke[i] += .5*mass[i]*vi**2
            ke[j] += -.5*mass[j]*vj**2
            
    return a, pe, ke


while t < t_max:   
    
    ac, pe, ke = acc(pos, mass, vel, e)

    dt_grav =  np.min([dt_max,((2*n*e)/(np.max(LA.norm(ac, axis = 1)))**2)**.5])

    T.append(t + dt_grav)
    print(t/t_max)*100 

    "Verlet Method"
    opos = pos
    ovel = vel

    pos = Verp(ovel, opos, dt_grav, ac)
    vel = Verv(pos, mass, ovel, dt_grav, ac, e)

    t += dt_grav
    
    """dump pos into file"""
    a0.append(pos[0])
    b0.append(pos[1])
#    c0.append(pos[2])    
    """dump energies into file"""
    Ta.append(pe[0] + ke[0])
    Tb.append(pe[1] + ke[1])
#    Tc.append(pe[2] + ke[2]) 
    Tsum.append(pe[0] + ke[0] + pe[1] + ke[1]) # + pe[2] + ke[2])

    if t == t_max:
        break
    
