# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 20:42:24 2016

@author: Gerwyn Jones
"""
from __future__ import division
import numpy as np 
import matplotlib.pyplot as plt

from ODE import ODEsolve, ConvergenceTest

def f(t, y, l):
    """ A function to call yprime and y """
    return y[1], l*y[0]
    
def Rk4(ya, f, t, dt, l):
    """ The Y array has two values so we need to split them up 
    when using euler"""
#    f1,f2 = f(t, y, l)   # f1 gives the value y of the function and f2 gives the value of yprime of the function
    yi,ypi = ya        # yb gives the initial y values and yc gives initail yp values

    # using Runge-Kutta method
    k1 = f(t, ya, l)
    ki1 = np.array(k1)
    k2 = f(t,ya + ki1*dt/2, l)
    ki2 = np.array(k2)
    k3 = f(t,ya + ki2*dt/2, l)
    ki3 = np.array(k3)
    k4 = f(t,ya + ki3*dt, l)  
  
    y = yi + (dt/6)*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0])  # y value
    yp = ypi + (dt/6)*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1])  # yprime value
#    
    return y, yp

#lambda
G = 6.67408e-11; Me = 5.9724e24; Ms = 1.9885e30
R = 1.496e11
l = (G*Ms*Me)/(R**3)

#defining initial conditions 
ti = 0; Tmax = 3.154e7
w = (np.pi*2)/Tmax; v = w*R

#time steps 
N = 1e8

#collecting initial conditions
ic = np.array([ti, R, v, l])  # initial time, final time, initial y and lambda

# solving ODE
R = ODEsolve(Tmax, N, f, Rk4, ic) 

T = R[0][1]; Y = R[0][0]

plt.plot(T, Y, label=r'$dt = %.5f$' %(Tmax/n[i]))
plt.xlabel(r'$Time$')
plt.ylabel(r'$Y$') 
plt.title('Graph of ODE')
plt.legend(loc='best') 
plt.grid() 

    
"""
a,b = ConvergenceTest(ODEsolve, Tmax, n, f, ic, Rk4, 4)

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

A = [ODEsolve(Tmax, n, f, Rk4, ic) for i, n in enumerate(Na)] 

Ydt = [A[i][0][0][-1] for i in range(len(A))]
Tdt = [A[i][1][-1] for i in range(len(A))]

Te = np.array(Tdt); Ye = f1(Te,w)
 
plt.figure()   
plt.loglog(Na, Ye, label=r'$Y - Y/2$')
plt.xlabel(r'$Time$')
plt.ylabel(r'$Y$') 
plt.title('Graph of ODE')
plt.legend(loc='best') 
plt.grid()     
"""