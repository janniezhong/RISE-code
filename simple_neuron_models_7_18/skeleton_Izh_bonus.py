# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 14:41:41 2018

@author: janniez
"""

import numpy as np
import matplotlib.pyplot as plt

# Run the simulation
def defaultEqSolve(a, b, c, d, vr, vt, vpeak, k, C, timestep, numsteps, vectorv, vectoru, vectorI):
    for i in range(0,numsteps-1):
        vectorv[0,i+1]=vectorv[0,i]+timestep*(k*(vectorv[0,i]-vr)*(vectorv[0,i]-vt)-vectoru[0,i]+vectorI[0,i])/C
        vectoru[0,i+1]=vectoru[0,i]+timestep*a*(b*(vectorv[0,i]-vr)-vectoru[0,i])
        if vectorv[0,i+1]>=vpeak:
            vectorv[0,i]=vpeak
            vectorv[0,i+1]=c
            vectoru[0,i+1]=vectoru[0,i+1]+d
    return vectorv



def FSEqSolve(a, b, c, d, vr, vt, vpeak, k, C, timestep, numsteps, vectorv, vectoru, vectorI):
    for i in range(0,numsteps-1):
        
        Uv = 0
        vb = -55 #???
        if v[0,i] >= -55:
            Uv = 0.025*(v[0,i] - vb)**3
        
        vectorv[0,i+1]=vectorv[0,i]+timestep*(k*(vectorv[0,i]-vr)*(vectorv[0,i]-vt)-vectoru[0,i]+vectorI[0,i])/C
        vectoru[0,i+1]=vectoru[0,i]+timestep*a*(b*(Uv-vr)-vectoru[0,i])
        if vectorv[0,i+1]>=vpeak:
            vectorv[0,i]=vpeak
            vectorv[0,i+1]=c
            vectoru[0,i+1]=vectoru[0,i+1]+d
    return vectorv


def LTSEqSolve(a, b, c, d, vr, vt, vpeak, k, C, timestep, numsteps, vectorv, vectoru, vectorI):
    for i in range(0,numsteps-1):
        vectorv[0,i+1]=v[0,i]+timestep*(k*(vectorv[0,i]-vr)*(vectorv[0,i]-vt)-vectoru[0,i]+vectorI[0,i])/C
        vectoru[0,i+1]=vectoru[0,i]+timestep*a*(b*(v[0,i]-vr)-vectoru[0,i])
        if vectorv[0,i+1]>=(40-0.1*vectoru[0,i+1]):
            vectorv[0,i]=vpeak
            vectorv[0,i+1]=-53+0.04*vectoru[0,i+1]
            vectoru[0,i+1]=np.min(u[0,i+1]+20, 670)
    return vectorv

    
def LSEqSolve(a, b, c, d, vr, vt, vpeak, k, C, timestep, numsteps, vectorv, vectoru, vectorI):
    
    for i in range(0,numsteps-1):
        vd = vectorv.copy()
        vectorv[0,i+1]=vectorv[0,i]+timestep*(k*(vectorv[0,i]-vr)*(vectorv[0,i]-vt)+1.2*(vd[0,i]-vectorv[0,i])-vectoru[0,i]+vectorI[0,i])/C        
        vectoru[0,i+1]=vectoru[0,i]+timestep*a*(b*(vectorv[0,i]-vr)-vectoru[0,i])
        if vectorv[0,i+1]>=vpeak:
            vectorv[0,i]=vpeak
            vectorv[0,i+1]=-45
            vectoru[0,i+1]=u[0,i+1]+d
        vd[0,i+1] = vd[0,i] + tau*(0.01*(v[0,i] - vd[0,i]))
    return vectorv

# Define the cell types
def RScell(tau, n, v, u, I):		
	C=100
	vr=-60
	vt=-40
	k=0.7
	a=0.03
	b=-2
	c=-50
	d=100
	vpeak=50
	v = vr*v
	v = defaultEqSolve(a, b, c, d, vr, vt, vpeak, k, C, tau, n, v, u, I)
	return v

def IBcell(tau, n, v, u, I):		
	C=150
	vr=-75
	vt=-45
	k=1.2
	a=0.01
	b=5
	c=-56
	d=130
	vpeak=50
	v = vr*v
	v = defaultEqSolve(a, b, c, d, vr, vt, vpeak, k, C, tau, n, v, u, I)
	return v

def Ccell(tau, n, v, u, I):		
	C=50
	vr=-60
	vt=-40
	k=1.5
	a=0.03
	b=1
	c=-40
	d=150
	vpeak=50
	v = vr*v
	v = defaultEqSolve(a, b, c, d, vr, vt, vpeak, k, C, tau, n, v, u, I)
	return v

def FScell(tau, n, v, u, I):		
	C=20
	vr=-55
	vt=-45
	k=1.0
	a=0.2
	b=1
	c=-40
	d=-55 #arbitrary?
	vpeak=50
	v = vr*v
	v = FSEqSolve(a, b, c, d, vr, vt, vpeak, k, C, tau, n, v, u, I)
	return v

def LTScell(tau, n, v, u, I):		
	C=100
	vr=-56
	vt=-42
	k=1.0
	a=0.03
	b=8
	c=-40
	d=150 #arbitrary?
	vpeak = 50
	v = vr*v
	v = LTSEqSolve(a, b, c, d, vr, vt, vpeak, k, C, tau, n, v, u, I)
	return v

def LScell(tau, n, v, u, I):		
	C=20
	vr=-66
	vt=-40
	k=0.3
	a=0.17
	b=5
	c=-45
	d=100 
	vpeak=30
	v = vr*v
	v = LSEqSolve(a, b, c, d, vr, vt, vpeak, k, C, tau, n, v, u, I)
	return v


celltype = 'LS' #'RS', 'IB', 'C', 'FS', 'LTS', 'LS'
# Set up the simulation
T=1000
tau=1
n=int(np.round(T/tau))

v=np.ones((1,n))
u=0*v

# Set up the stimulation
stimVal = 150 #70, 500, 200
I = np.concatenate((np.zeros((1,int(0.1*n))),stimVal*np.ones((1,int(0.9*n)))), axis=1)

# TO DO: Add code here to check which celltype is 
#        requested and call the right function. See
#        the lab manual for hints. Right now, as a 
#        placeholder, we call the one cell that is
#        already defined:


if celltype == 'RS':
    v = RScell(tau, n, v, u, I)
elif celltype == 'IB':
    v = IBcell(tau, n, v, u, I)
elif celltype == 'C':
    v = Ccell(tau, n, v, u, I)
elif celltype == 'FS':
    v = FScell(tau, n, v, u, I)
elif celltype == 'LTS':
    v = LTScell(tau, n, v, u, I)
elif celltype == 'LS':
    v = LScell(tau, n, v, u, I)
else:
    print("The answer is no")
    
#a, b, c, d, vr, vt, vpeak, k, C

   

# initialize the output vector to the resting membrane potential
#v = vr*v 



# Plot the results
fig = plt.figure()
plt.plot(tau*np.arange(0,n),v.transpose(), linewidth=2, color='k', linestyle='-')
plt.xlabel('Time Step')
plt.ylabel('Cell Response')
plt.show()
