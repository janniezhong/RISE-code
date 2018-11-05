# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np


gmax = 0.005 #uS, gives results in nanoAmperes, maximum conductance
tauR = 2 #ms, rise time constant
tauD = 8\ #ms, decay time constant
eSYN = 0 #millivolts ---- synaptic reversal potential
v = -60 #millivolts, membrane potential
times = np.arange(0, 100, 0.5)


currents = [0]*len(times) #np.zeros((1,len(times)))
conductance = [0]*len(times) #np.zeros((1,len(times)))
for x, I in enumerate(times):
    conductance[x] = gmax * (-np.exp(-times[x]/tauR) + np.exp(-times[x]/tauD))
    currents[x] = conductance[x]*(v - eSYN)
    

import matplotlib.pyplot as plt

f, (ax1, ax2) = plt.subplots(2,1)
ax1.plot(times, conductance)
ax2.plot(times, currents, 'r:')
ax1.set_ylabel('Conductance')
ax2.set_ylabel('Currents')
ax2.set_xlabel('Time')
