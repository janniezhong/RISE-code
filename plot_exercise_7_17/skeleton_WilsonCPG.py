# this script implements a linear version of Wilson's 
# locust flight central pattern generator (CPG). Modified
# from Tom Anastasio's mfile to Python code.
# Modified for BU's RISE Practicum Comp Neuro lab by mbezaire@bu.edu


###############################
# import libraries with special
# functions needed in this script
###############################

import numpy as np
import matplotlib.pyplot as plt


###############################
# Define connections between cells in network
###############################

# The connection weights (from input to neurons
# and between each neuron) have already been set:

# input weights
v1=0
v2=1
v3=0
v4=0  

# feedback weights to unit one (left depressor)
w11=0.9   # from self
w12=0.2   # from same side elevator
w13=0
w14=0  

# feedback weights to unit two (left elevator)
w21=-0.95 # from same side depressor
w22=0.4   # from self
w23=-0.5  # from other side elevator
w24=0

# weights to unit three (right elevator)
w31=0
w32=-0.5  # from other side elevator
w33=0.4   # from self
w34=-0.95 # from same side depressor  

# weights to unit four (right depressor)
w41=0
w42=0
w43=0.2   # from same side elevator
w44=0.9   # from self

# Now organize the individuals weights
# into a vector (for the input weights) and a
# matrix (for the weights of the connections
# between cells. 

# Input weight matrix (a vector)
V=[v1, v2, v3, v4]  

# Feedback weight matrix (a matrix)
W=[[w11, w12, w13, w14],   
   [w21, w22, w23, w24],
   [w31, w32, w33, w34],
   [w41, w42, w43, w44]]


###############################
# Set up simulation
###############################
# TO DO: Set up the simulation. First, define
#        a variable tEnd that is equal to the
#        last time step we want to
#        simulate, 100:
tEnd = 100

# TO DO: Now, create a list called tVec that we
#        can use as a vector of all the time
#        steps. Use the range function with two
#        arguments: the first time step (t=0)
#        and the last time step (tEnd+1):
tVec =  list(range(0, tEnd+1))
#tVec = [0]*(tEnd+1)

# TO DO: Find the total number of time steps
#        that we want to simulate and store it
#        in the variable nTs

nTs = len(tVec)


# TO DO: Create a placeholder location to store
#        the simulation results. Use the np.zeros function
#        to create a matrix y that is 4 rows long and has one
#        columns for each time step of the simulation. That
#        way we can track the activity of each of the four
#        cells in our circuit throughout the simulation:
y = np.zeros((4,tEnd+1)) 

###############################
# Define input stimulation
###############################
# TO DO: Define the stimulation for the model.
#        First, create a blank numpy vector x that
#        is filled with zeros and is long enough
#        that there is one element for each time
#        step in the simulation:

x = np.zeros((1,nTs))

# TO DO: Define a variable called 'fly' that stores
#        the timestep at which the wings should start
#        flying (ie, when the input should be sent to
#        the circuit to start the central pattern). Use
#        timestep 11 as the start.

fly = 11

# TO DO: In the input vector x, set the stimulation to 1
#        only for the element corresponding to the timestep
#        stored in the 'fly' variable, all other elements
#        should remain 0. Tip: Because x is a numpy vector
#        instead of a regular python list, we need to specify
#        both the row and column indices. x is a vector with 1
#        row and many columns (equal to the number of time steps)
#        so we specify the row index as 0.

x[0,fly] = 1

###############################
# Run simulation
###############################

# TO DO: Run the simulation. Use a for loop and the range function
#        to iterate through each time step and compute the activity
#        of each cell. Refer back to the Lab Manual for help writing
#        the command that computes the activity of each cell:
# for t ...
#     y[:,t] = ...
for t in range (0, nTs):
    y[:,t] = np.dot(W,y[:,t-1]) + np.dot(V,x[0,t-1])

###############################
# Plot the results
###############################
fig = plt.figure()
plt.plot(tVec,x[0], linewidth=2, color='k', linestyle='-', label="Input")
plt.plot(tVec,y[0,:], linewidth=2, color='b', linestyle=':',label='Y1: left depressor')
plt.plot(tVec,y[1,:], linewidth=2, color='b', linestyle='-',label='Y2: left elevator')
plt.plot(tVec,y[2,:], linewidth=2, color='r', linestyle='-',label='Y3: right elevator')
plt.plot(tVec,y[3,:], linewidth=2, color='r', linestyle=':',label='Y4: right depressor')
plt.xlabel('Time Step')
plt.ylabel('Input and Unit Responses')
plt.legend()
plt.show()
