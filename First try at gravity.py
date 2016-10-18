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
e_x = zeros(steps)
e_y = zeros(steps)
e_vx = zeros(steps)
e_vy = zeros(steps)
e_x[0] = AU
e_vy[0] = 30000

"Euler's Method"
for i in range(1,steps):
    r  = (e_x[i-1]**2+e_y[i-1]**2)**0.5
    a = -G*Ms/r**3
    "Velocities:"
    e_vx[i] = e_vx[i-1] + dt*a*e_x[i-1]
    e_vy[i] = e_vy[i-1] + dt*a*e_y[i-1]
    "Position:"
    e_x[i] = e_x[i-1] + dt*e_vx[i-1]
    e_y[i] = e_y[i-1] + dt*e_vy[i-1]
plot(e_x,e_y)
plot(0,0,"yo")
