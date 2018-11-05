import numpy as np
import matplotlib.pyplot as plt


# Define the cell types
def RScell():		
	C=100
	vr=-60
	vt=-40
	k=0.7
	a=0.03
	b=-2
	c=-50
	d=100
	vpeak=35
	return a, b, c, d, vr, vt, vpeak, k, C

def IBcell():		
	C=150
	vr=-75
	vt=-45
	k=1.2
	a=0.01
	b=5
	c=-56
	d=130
	vpeak=50
	return a, b, c, d, vr, vt, vpeak, k, C

def Ccell():		
	C=50
	vr=-60
	vt=-40
	k=1.5
	a=0.03
	b=1
	c=-40
	d=150
	vpeak=25
	return a, b, c, d, vr, vt, vpeak, k, C


celltype = 'C' #'RS', 'IB', 'C'
# Set up the simulation
T=1000
tau=1
n=int(np.round(T/tau))

v=np.ones((1,n))
u=0*v

# Set up the stimulation
stimVal = 200 #70, 500, 200
I = np.concatenate((np.zeros((1,int(0.1*n))),stimVal*np.ones((1,int(0.9*n)))), axis=1)

# TO DO: Add code here to check which celltype is 
#        requested and call the right function. See
#        the lab manual for hints. Right now, as a 
#        placeholder, we call the one cell that is
#        already defined:


if celltype == 'RS':
    a, b, c, d, vr, vt, vpeak, k, C = RScell()
elif celltype == 'IB':
    a, b, c, d, vr, vt, vpeak, k, C = IBcell()
elif celltype == 'C':
    a, b, c, d, vr, vt, vpeak, k, C = Ccell()
else:
    print("The answer is no")
    
a, b, c, d, vr, vt, vpeak, k, C

   

# initialize the output vector to the resting membrane potential
v = vr*v 

# Run the simulation
for i in range(0,n-1):
	v[0,i+1]=v[0,i]+tau*(k*(v[0,i]-vr)*(v[0,i]-vt)-u[0,i]+I[0,i])/C
	u[0,i+1]=u[0,i]+tau*a*(b*(v[0,i]-vr)-u[0,i])
	if v[0,i+1]>=vpeak:
		v[0,i]=vpeak
		v[0,i+1]=c
		u[0,i+1]=u[0,i+1]+d


# Plot the results
fig = plt.figure()
plt.plot(tau*np.arange(0,n),v.transpose(), linewidth=2, color='k', linestyle='-')
plt.xlabel('Time Step')
plt.ylabel('Cell Response')
plt.show()
