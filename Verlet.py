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

def f1(t,l): 
    return np.cos(l*t)    # eq of d^2y/dt^2

for i in range(len(R)):
    T = R[i][1]; Y = R[i][0][1]
    plt.subplot(2,1,1)
    plt.plot(T, Y, label=r'$dt = %.5f$' %(Tmax/n[i]))
    plt.xlabel(r'$Time$')
    plt.ylabel(r'$Y$') 
    plt.title('Graph of ODE')
    plt.legend(loc='best') 
    plt.grid() 
    plt.subplot(2,1,2)
    plt.plot(T, f1(T,w)-Y, label=r'$delta$ $t = %.5f$' %(Tmax/n[i]) )
    plt.xlabel(r'$Time$')
    plt.ylabel(r'$Error$') 
    plt.legend(loc='best')
    plt.grid() 

a,b = ConvergenceTest(ODEsolve, Tmax, n, f, ic, Ver, 2)

plt.figure()
plt.subplot(2,1,1)
plt.plot(a, label=r'$Y - Y/2$')
plt.plot(b, label=r'$Y/2 - Y/4$')
plt.xlabel(r'$Time$')
plt.ylabel(r'$Convergence$') 
plt.title('Graph of Convergence and Errors')
plt.legend(loc='best') 
plt.grid() 
plt.subplot(2,1,2)
plt.plot(a/b, label=r'$\frac{Y - Y/2}{Y/2 - Y/4}$')
plt.xlabel(r'$Time$')
plt.ylabel(r'$Error$') 
plt.legend(loc='best')
plt.grid() 
    
dt = (1/2)**np.linspace(1,18,18); Na = Tmax/dt

A = [ODEsolve(Tmax, n, f, Ver, ic) for i, n in enumerate(Na)] 

Ydt = [A[i][0][0][-1] for i in range(len(A))]
Tdt = [A[i][1][-1] for i in range(len(A))]

Te = np.array(Tdt); Ye = f1(Te,w)
 
plt.figure()   
plt.loglog(Na, Ydt, label=r'$Error$')
plt.xlabel(r'$Time$')
plt.ylabel(r'$Y$') 
plt.title('Graph of ODE')
plt.legend(loc='best') 
plt.grid()     