#!/usr/bin/env python
"""
Created on Tue Oct 18 09:11:38 2016

@author: Admin
"""

from __future__ import division
import numpy as np 
from numpy import linalg as LA

from Verlet_IC_EMS import *

#####################


def Verp(ovel, opos, dt, a):
    "Position:"
    pos = opos + ovel*dt + .5*a*dt**2
    return pos
    
def Verv(pos, mass, ovel, dt, a, e):
     "Velocities:"
     an, pe = acc(pos, mass, ovel, e)
     vel = ovel + .5*(a + an)*dt
     return vel

def acc(pos, mass, vel, e):
    
    a = np.zeros((N,3))
    pe = np.zeros((N,1))
    
    G = 6.67408e-11
    
    for i in range(0,N-1):
        for j in range(i+1,N):
            
            r = pos[i]-pos[j]
            m = LA.norm(r)
            F = (G/(m+e)**3)*r # check (m+e) part
            
            a[i] += -F*mass[j]
            a[j] += F*mass[i]
            pe[i] += -(G*mass[i]*mass[j])/(m+e) # Check PE
            pe[j] += -(G*mass[j]*mass[i])/(m+e)

            
    return a, pe

def KE(vel, mass):
    
    ke = np.zeros((N,1))
    
    for i in range(0,N):
        vi = LA.norm(vel[i])        
        ke[i] = .5*mass[i]*vi**2

    return ke

while t < t_max:   
    
    ac, pe = acc(pos, mass, vel, e)
    
    ke = KE(vel,mass)

    dt_grav =  np.min([dt_max,((2*n*e)/(np.max(LA.norm(ac, axis = 1))))**.5])

    T.append(t + dt_grav)
    print(t/t_max)*100 

    "Verlet Method"
    opos = pos
    ovel = vel

    pos = Verp(ovel, opos, dt_grav, ac)
    vel = Verv(pos, mass, ovel, dt_grav, ac, e)

    t += dt_grav
    
    """dump pos into file"""
    a.append(pos[0])
    A = np.asarray(a)
    b.append(pos[1])
    B = np.asarray(b)
    c.append(pos[2])    
    C = np.asarray(c)
    """dump energies into file"""
    Ta.append(pe[0] + ke[0])
    Ea = np.asarray(Ta)
    Tb.append(pe[1] + ke[1])
    Eb = np.asarray(Tb)
    Tc.append(pe[2] + ke[2])
    Ec =  np.asarray(Tc)
    Tsum.append(Ea + Eb + Ec)
    Esum =  np.asarray(Tsum)
    
    if t == t_max:
        break
    
