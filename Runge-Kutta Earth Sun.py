# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 20:42:24 2016

@author: Gerwyn Jones
"""
from __future__ import division
import numpy as np 
import matplotlib.pyplot as plt

from ODE import ODEsolve, ConvergenceTest

def f(t, r, l):
    """ A function to call yprime and y """
    return r[1], (l)*r[0],
    
def Rk4(ra, f, t, dt, l):
    """ The Y array has two values so we need to split them up 
    when using euler"""
#    f1,f2 = f(t, y, l)   # f1 gives the value y of the function and f2 gives the value of yprime of the function
    ri,rpi = ra        # yb gives the initial y values and yc gives initail yp values

    # using Runge-Kutta method
    k1 = f(t, ra, l)
    ki1 = np.array(k1)
    k2 = f(t,ra + ki1*dt/2, l)
    ki2 = np.array(k2)
    k3 = f(t,ra + ki2*dt/2, l)
    ki3 = np.array(k3)
    k4 = f(t,ra + ki3*dt, l)  
  
    r = ri + (dt/6)*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0])  # y value
    rp = rpi + (dt/6)*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1])  # yprime value
#    
    return r, rp

#lambda
<<<<<<< HEAD
G = 6.67408e-11; Me = 5.9724e24; Ms = 1.9885e30
R = 1.496e11
=======
G = 6.67408e-5; Me = 5.9724e18; Ms = 1.9885e24
R = 1.496e5
>>>>>>> origin/master
l = -(G*Ms*Me)/(R**3)

#defining initial conditions 
ti = 0; Tmax = 3.154e1
w = (np.pi*2)/Tmax; v = w*R

#time steps 
N = 1e4

#collecting initial conditions
ic = np.array([ti, R, v, l])  # initial time, final time, initial y and lambda

# solving ODE
X = ODEsolve(Tmax, N, f, Rk4, ic) 

<<<<<<< HEAD
T = X[0][1]; Y = X[0][0]
=======
T = R[1]; Y = R[0][0]
>>>>>>> origin/master

plt.plot(T, Y, label=r'$dt = %.5f$' %(Tmax/N))
plt.xlabel(r'$Time$')
plt.ylabel(r'$Y$') 
plt.title('Graph of ODE')
plt.legend(loc='best') 
plt.grid() 

