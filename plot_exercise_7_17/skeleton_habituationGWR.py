# Based on Tom Anastasio's habituationGWR.m
# this script sets up a very simple simulation of habituation
# of the Aplysia gill withdrawal reflex
#
# Modified for BU's RISE Practicum Comp Neuro lab by mbezaire@bu.edu

###############################
# import libraries with special
# functions needed in this script
###############################
import numpy as np
import matplotlib.pyplot as plt

###############################
# Define input stimulation
###############################
# TO DO: Set a variable called stv to 4, this will define 
#        the weight of the connection from input to output
stv = 4 

# TO DO: set up an input pulse called pls
pls = [0, 0, 1, 0, 0]

# TO DO: then create a list of 6 pulses, called x, to use for input
x = pls*79

v = stv # Set connection weight to start weight value

###############################
# Set up and run simulation
###############################

nTs = len(x) # find the length of the input list
y = np.zeros((1,nTs)) # set up (define) a vector for the output time series

# TO DO: use a for-loop to iterate 
#        through each time step in 
#        the input series and calculate
#        the output at each time step. Ex:
# for ...
#     then indent 4 spaces and write the equation that
#     describes how each input value in the vector x is 
#     transformed to the output value in the vector y

for t in range(0, nTs):
    y[0,t] = v*x[t]
    if x[t]>0:
        v = v * 0.7



###############################
# Plot the results
###############################

# Plot both the input series (vector x)
# and the resulting output series (vector y)
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.plot(x) #, color='white',  antialiased=False, edgecolors='black', linewidth=1, shade=False, alpha=1)
ax1.set_ylabel('Input')
ax1.set_xlim(0, nTs)
ax1.set_ylim(0, 1.1)

ax2 = fig.add_subplot(212)
ax2.plot(y[0]) #, color='white',  antialiased=False, edgecolors='black', linewidth=1, shade=False, alpha=1)
ax2.set_xlabel('Time step')
ax2.set_ylabel('Output')
ax2.set_xlim(0, nTs)
ax2.set_ylim(0, stv+0.5)

plt.show()
