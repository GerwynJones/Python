"""
Creator: Patrik Bernhardsson
Date: 16/10/2016
"""
"Importing functions"
from matplotlib.pyplot import plot
from numpy import zeros

"Defining Variables"
t_max = 365*24*60*60
dt = 60
steps = int(t_max/dt)
AU = 149597871000
G = 6.67408*10**-11
Ms = 1.989*10**30
e_x = zeros(steps+1)
e_y = zeros(steps+1)
e_vx = zeros(steps+1)
e_vy = zeros(steps+1)
e_x[0] = AU
e_vy[0] = (2*pi*AU)/t_max

"Euler's Method"
for i in range(1,steps+1):
    r  = (e_x[i-1]**2+e_y[i-1]**2)**0.5
    a = -G*Ms/r**3
    
    "Position:"
    e_x[i] = e_x[i-1] + dt*e_vx[i-1] + .5*(a*e_x[i-1])*(dt*dt)
    e_y[i] = e_y[i-1] + dt*e_vy[i-1] + .5*(a*e_x[i-1])*(dt*dt)
    "Velocities:"
    e_vx[i] = e_vx[i-1] + .5*(a*(e_x[i-1] + e_x[i]))*dt
    e_vy[i] = e_vy[i-1] + + .5*(a*(e_y[i-1] + e_y[i]))*dt


plot(e_x,e_y)
plot(0,0,"yo")
