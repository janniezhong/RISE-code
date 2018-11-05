# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 13:57:30 2018

@author: janniez
"""
import numpy
from matplotlib import pyplot
from neuron import h, gui
from math import sin, cos, pi


class BallAndStick(object):
    """Two-section cell: A soma with active channels and
    a dendrite with passive properties."""
    def __init__(self):
        self.x = self.y = self.z = 0
        self.create_sections()
        self.build_topology()
        self.build_subsets()
        self.define_geometry()
        self.define_biophysics()
    #
    def create_sections(self):
        """Create the sections of the cell."""
        # NOTE: cell=self is required to tell NEURON of this object.
        self.soma = h.Section(name='soma', cell=self)
        self.dend = h.Section(name='dend', cell=self)
    #
    def build_topology(self):
        """Connect the sections of the cell to build a tree."""
        self.dend.connect(self.soma(1))
    #
    def define_geometry(self):
        """Set the 3D geometry of the cell."""
        self.soma.L = self.soma.diam = 12.6157 # microns
        self.dend.L = 200                      # microns
        self.dend.diam = 1                     # microns
        self.dend.nseg = 5
        h.define_shape() # Translate into 3D points.
    #
    def define_biophysics(self):
        """Assign the membrane properties across the cell."""
        for sec in self.all: # 'all' defined in build_subsets
            sec.Ra = 100    # Axial resistance in Ohm * cm
            sec.cm = 1      # Membrane capacitance in micro Farads / cm^2
        # Insert active Hodgkin-Huxley current in the soma
        self.soma.insert('hh')
        for seg in self.soma:
            seg.hh.gnabar = 0.12  # Sodium conductance in S/cm2
            seg.hh.gkbar = 0.036  # Potassium conductance in S/cm2
            seg.hh.gl = 0.0003    # Leak conductance in S/cm2
            seg.hh.el = -54.3     # Reversal potential in mV
        # Insert passive current in the dendrite
        self.dend.insert('pas')
        for seg in self.dend:
            seg.pas.g = 0.001  # Passive conductance in S/cm2
            seg.pas.e = -65    # Leak reversal potential mV
    #
    def build_subsets(self):
        """Build subset lists. For now we define 'all'."""
        self.all = h.SectionList()
        self.all.wholetree(sec=self.soma)
        
     #
    #### NEW STUFF ADDED ####
    #
    def shape_3D(self):
        """
        Set the default shape of the cell in 3D coordinates.
        Set soma(0) to the origin (0,0,0) and dend extending along
        the X-axis.
        """
        len1 = self.soma.L
        h.pt3dclear(sec=self.soma)
        h.pt3dadd(0, 0, 0, self.soma.diam, sec=self.soma)
        h.pt3dadd(len1, 0, 0, self.soma.diam, sec=self.soma)
        len2 = self.dend.L
        h.pt3dclear(sec=self.dend)
        h.pt3dadd(len1, 0, 0, self.dend.diam, sec=self.dend)
        h.pt3dadd(len1 + len2, 0, 0, self.dend.diam, sec=self.dend)
    #
    def set_position(self, x, y, z):
        """
        Set the base location in 3D and move all other
        parts of the cell relative to that location.
        """
        for sec in self.all:
            # note: iterating like this changes the context for all NEURON
            # functions that depend on a section, so no need to specify sec=
            for i in range(sec.n3d()):
                h.pt3dchange(i,
                        x - self.x + sec.x3d(i),
                        y - self.y + sec.y3d(i),
                        z - self.z + sec.z3d(i),
                        sec.diam3d(i), sec=sec)
        self.x, self.y, self.z = x, y, z
    #
    def rotateZ(self, theta):
        """Rotate the cell about the Z axis."""
        for sec in self.all:
            for i in range(sec.n3d()):
                x = sec.x3d(i)
                y = sec.y3d(i)
                c = cos(theta)
                s = sin(theta)
                xprime = x * c - y * s
                yprime = x * s + y * c
                h.pt3dchange(i, xprime, yprime, sec.z3d(i), sec.diam3d(i), sec=sec)



"""
soma = h.Section(name='soma')
dend = h.Section(name='dend')

h.psection(sec=soma)
dend.connect(soma(1))
h.psection(sec=dend)
h.topology()

# Surface area of cylinder is 2*pi*r*h (sealed ends are implicit).
# Here we make a square cylinder in that the diameter
# is equal to the height, so diam = h. ==> Area = 4*pi*r^2
# We want a soma of 500 microns squared:
# r^2 = 500/(4*pi) ==> r = 6.2078, diam = 12.6157
soma.L = soma.diam = 12.6157 # Makes a soma of 500 microns squared.
dend.L = 200 # microns
dend.diam = 1 # microns
print("Surface area of soma = {}".format(soma(0.5).area()))

#biophysical mechanisms in the membrane

for sec in h.allsec():
    sec.Ra = 100    # Axial resistance in Ohm * cm
    sec.cm = 1      # Membrane capacitance in micro Farads / cm^2

# Insert active Hodgkin-Huxley current in the soma
soma.insert('hh')
for seg in soma:
    seg.hh.gnabar = 0.12  # Sodium conductance in S/cm2
    seg.hh.gkbar = 0.036  # Potassium conductance in S/cm2
    seg.hh.gl = 0.0003    # Leak conductance in S/cm2
    seg.hh.el = -54.3     # Reversal potential in mV

# Insert passive current in the dendrite
dend.insert('pas')
for seg in dend:
    seg.pas.g = 0.001  # Passive conductance in S/cm2
    seg.pas.e = -65    # Leak reversal potential mV


#what are the units of this mechanism?
print(h.units('gnabar_hh'))
for sec in h.allsec():
    h.psection(sec=sec)
    
    
    
    
#stimulation
stim = h.IClamp(dend(1))
#display the attributes of the stimulation
dir(stim)
#verify the location
print("segment = {}".format(stim.get_segment()))
#set the fields of the stim
stim.delay = 5
stim.dur = 1
stim.amp = 0.1

#set up the recording vectors, run + plot
v_vec = h.Vector()        # Membrane potential vector
t_vec = h.Vector()        # Time stamp vector
v_vec.record(soma(0.5)._ref_v)
t_vec.record(h._ref_t)
simdur = 25.0

h.tstop = simdur
h.run()

from matplotlib import pyplot
pyplot.figure(figsize=(8,4)) # Default figsize is (8,6)
pyplot.plot(t_vec, v_vec)
pyplot.xlabel('time (ms)')
pyplot.ylabel('mV')
pyplot.show()


#vary the amplitude of current in a loop
import numpy
pyplot.figure(figsize=(8,4))
step = 0.075
num_steps = 4
for i in numpy.linspace(step, step*num_steps, num_steps):
    stim.amp = i
    h.tstop = simdur
    h.run()
    pyplot.plot(t_vec, v_vec, color='black')

pyplot.xlabel('time (ms)')
pyplot.ylabel('mV')
pyplot.show()



dend_v_vec = h.Vector()        # Membrane potential vector
dend_v_vec.record(dend(0.5)._ref_v)

pyplot.figure(figsize=(8,4))
for i in numpy.linspace(step, step*num_steps, num_steps):
    stim.amp = i
    h.tstop = simdur
    h.run()
    soma_plot = pyplot.plot(t_vec, v_vec, color='black')
    dend_plot = pyplot.plot(t_vec, dend_v_vec, color='red')

# After looping, actually draw the image with show.
# For legend labels, use the last instances we plotted
pyplot.legend(soma_plot + dend_plot, ['soma', 'dend'])
pyplot.xlabel('time (ms)')
pyplot.ylabel('mV')
pyplot.show()


pyplot.figure(figsize=(8,4))
for i in numpy.linspace(step, step*num_steps, num_steps):
    stim.amp = i
    h.run()
    soma_plot = pyplot.plot(t_vec, v_vec, color='black')
    dend_plot = pyplot.plot(t_vec, dend_v_vec, color='red')
    
#change the number of segments in the dendrite from 1 to 101
dend.nseg = 101

for i in numpy.linspace(step, step*num_steps, num_steps):
    stim.amp = i
    h.run()
    soma_hires = pyplot.plot(t_vec, v_vec, color='blue')
    dend_hires = pyplot.plot(t_vec, dend_v_vec, color='green')

# After looping, actually draw the image with show.
# For legend labels, use the last instances we plotted
pyplot.legend(soma_plot + dend_plot + soma_hires + dend_hires, ['soma', 'dend', 'soma hi-res', 'dend hi-res'])
pyplot.xlabel('time (ms)')
pyplot.ylabel('mV')
pyplot.show()




shape_window = h.PlotShape()
shape_window.exec_menu('Show Diam')
"""