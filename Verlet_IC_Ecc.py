# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 22:29:44 2016

@author: Admin
"""

from __future__ import division
import numpy as np 

AU = 149597871000
Ms = 1.989*10**30
Me = 5.972*10**22

"Defining Variables"
N = 2
t_max = 3.1556e7/1.25; t = 0
dt_max = t_max/5

v =  (2*np.pi*AU)/t_max

mass = np.array([Ms,Me])

pos = np.zeros((N,3))
vel = np.zeros((N,3))

pos[1] = np.array([0,AU,0])
vel[1] = np.array([v/5,0,0])


e = 0.0005*AU; n = 0.1