# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 22:29:44 2016

@author: Admin
"""

from __future__ import division
import numpy as np 

AU = 149597871000; A = 3000*AU
Ms = 1.989*10**30
Me = 5.972*10**24

"Defining Variables"
N = 2
t_max = 3.1556e7*(150.11e3); t = 0
dt_max = t_max/500

V =  2*(2*np.pi*A)/t_max

mass = np.array([Ms,Me])

pos = np.zeros((N,3))
vel = np.zeros((N,3))

pos[1] = np.array([0,A,0])
vel[1] = np.array([V/3,0,0])


e = 0.6*AU; n = 2


a = []; Ta = []
b = []; Tb = []

Tsum = []

T = [] 