# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 13:34:27 2018

@author: janniez
"""


import numpy as np
import csv

# time at which each occurred
times = []
# level of stimulation
inputs = []


with open('temperatures.dat', 'rt') as theFile:
    #content = theFile.readlines()
    reader = csv.DictReader( theFile, delimiter = ' ')
    for line in reader:
        times.append(float(line['Day']))
        inputs.append(float(line['Temperature']))

    
#piecewise
def f(I):
    theta = -459.0
    k = 5/9
    if I < theta:
        return 0
    else:
        return (I-32)*k
    
#sigmoidal

def g(I):
    
    theta = 60.0
    k = 1/5
    fbar = 20
    return 8+fbar/(1+np.exp(-k*(I - theta)))

#step
def h(I):
    
    theta = 50.0
    if I < theta:
        return 0
    else:
        return 1

outputf = [0]*len(inputs)
outputg = [0]*len(inputs)
outputh = [0]*len(inputs)

for x, I in enumerate(inputs):
    outputf[x] = f(I)
    outputg[x] = g(I)
    outputh[x] = h(I)


    
    
    
import matplotlib.pyplot as plt

f, (ax1, ax2, ax3) = plt.subplots(3,1)
ax1.plot(times, outputf)
ax2.plot(times, outputg, 'r:')
ax3.plot(times, outputh, 'b:')
ax1.set_ylabel('Temperature (C)')
ax2.set_ylabel('Cups of Water')
ax3.set_ylabel('Coat')
ax2.set_xlabel('Day')
