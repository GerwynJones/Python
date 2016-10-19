# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 16:03:10 2016

@author: Admin
"""
from __future__ import division
import numpy as np 
import matplotlib.pyplot as plt

from ODE import ODEsolve
    
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


    
