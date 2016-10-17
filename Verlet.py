# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 16:03:10 2016

@author: Admin
"""
from __future__ import division
import numpy as np 
import matplotlib.pyplot as plt

from ODE import ODEsolve, ConvergenceTest

def f(t, y, l):
    """ A function to call yprime and y """
    return l*y
    
def Ver(ya, fa, t, dt, l):
    """ The Y array has two values so we need to split them up 
    when using euler"""
    yi, ypi = ya 
    f = fa(t, yi, l)   # f1 gives the value y of the function and f2 gives the value of yprime of the function
    # yb gives the initial y values and yc gives initail yp values

    # using Verlet method
    y = yi +ypi*dt + .5*f*(dt*dt)
    yp = ypi + .5*(f + fa(t,y,l))*dt     
    
    return y, yp

   
#lambda
w = 2*np.pi; l = -w*w

#defining initial conditions 
ti = 0; Tmax = 1
yi = 1; ypi = 0

#time steps 
N = 1000; n = np.array([N,2*N,4*N])

#collecting initial conditions
ic = np.array([ti, yi, ypi, l])  # initial time, final time, initial y and lambda
 
# solving ODE
R = [ODEsolve(Tmax, N, f, Ver, ic) for i,N in enumerate(n)]

