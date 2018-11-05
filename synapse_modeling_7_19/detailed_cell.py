# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 15:23:22 2018

@author: janniez
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 13:57:30 2018

@author: janniez
"""
import numpy
from matplotlib import pyplot
from neuron import h
from math import sin, cos, pi


class DetailedCell(object):
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
        
        #index = 0
        #indexName = "" +index
        self.dend = []
        for i in range(0, 9):
            self.dend.append(h.Section(name='dend['+ str(i) +']'))
        
        #self.dend = h.Section(name='dend', cell=self)
    #
    def build_topology(self):
        """Connect the sections of the cell to build a tree."""
        self.dend[0].connect(self.soma(1))
        self.dend[1].connect(self.dend[0](1))
        self.dend[2].connect(self.dend[1](1))
        self.dend[3].connect(self.dend[2](1))
        self.dend[4].connect(self.dend[3](1))
        self.dend[5].connect(self.dend[4](1))
        
        self.dend[6].connect(self.dend[2](1))
        self.dend[7].connect(self.dend[6](1))
        self.dend[8].connect(self.dend[7](1))
    #
    def define_geometry(self):
        """Set the 3D geometry of the cell.""" # microns
        count = 0
        for i in range (0,len(self.dend)):
            self.dend[count].L = 200                      # microns
            self.dend[count].diam = 1                     # microns
            self.dend[count].nseg = 5
            count +=1
        
        self.soma.L = self.soma.diam = 12.6157 # microns
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
        
        count = 0
        for i in range (0,len(self.dend)):
            self.dend[count].insert('pas')
            for seg in self.dend[count]:
                seg.pas.g = 0.001  # Passive conductance in S/cm2
                seg.pas.e = -65    # Leak reversal potential mV
            count +=1
    
    
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
        self.soma.diam = 10
        self.soma.L = 10
        h.pt3dclear(sec=self.soma)
        h.pt3dadd(0, 0, 0, self.soma.diam, sec=self.soma)
        h.pt3dadd(0.0, 5.0, 0.0, self.soma.diam, sec=self.soma)
        h.pt3dadd(0.0, 10.0, 0.0, self.soma.diam, sec=self.soma)
            
        h.pt3dclear(sec=self.dend[0])	
        h.pt3dadd(0.0, 10.0, 0.0, 4.0, sec=self.dend[0])
        h.pt3dadd(0.0, 60.0, 0.0, 4.0, sec=self.dend[0])
        h.pt3dadd(0.0, 110.0, 0.0, 4.0, sec=self.dend[0])
                    
        h.pt3dclear(sec=self.dend[1])	
        h.pt3dadd(0.0, 110.0, 0.0, 3.0, sec=self.dend[1])
        h.pt3dadd(0.0, 160.0, 0.0, 3.0, sec=self.dend[1])
        h.pt3dadd(0.0, 210.0, 0.0, 3.0, sec=self.dend[1])
	
        h.pt3dclear(sec=self.dend[2])	
        h.pt3dadd(0.0, 210.0, 0.0, 2.0, sec=self.dend[2])
        h.pt3dadd(0.0, 310.0, 0.0, 2.0, sec=self.dend[2])
        h.pt3dadd(0.0, 410.0, 0.0, 2.0, sec=self.dend[2])

        h.pt3dclear(sec=self.dend[3])	
        h.pt3dadd(0.0, 410.0, 0.0, 2.0, sec=self.dend[3])
        h.pt3dadd(35.5, 445.5, 0.0, 2.0, sec=self.dend[3])
        h.pt3dadd(71.0, 481, 0.0, 2.0, sec=self.dend[3])

        h.pt3dclear(sec=self.dend[4])	
        h.pt3dadd(71.0, 481.0, 0.0, 1.5, sec=self.dend[4])
        h.pt3dadd(106.5, 516.5, 0.0, 1.5, sec=self.dend[4])
        h.pt3dadd(142.0, 552, 0.0, 1.5, sec=self.dend[4])

        h.pt3dclear(sec=self.dend[5])	
        h.pt3dadd(142.0, 552, 0.0, 1.0, sec=self.dend[5])
        h.pt3dadd(159.7, 569.7, 0.0, 1.0, sec=self.dend[5])
        h.pt3dadd(177.4, 587.4, 0.0, 1.0, sec=self.dend[5])

        h.pt3dclear(sec=self.dend[6])	
        h.pt3dadd(0.0, 410.0, 0.0, 2.0, sec=self.dend[6])
        h.pt3dadd(-35.5, 445.5, 0.0, 2.0, sec=self.dend[6])
        h.pt3dadd(-71.0, 481, 0.0, 2.0, sec=self.dend[6])

        h.pt3dclear(sec=self.dend[7])	
        h.pt3dadd(-71.0, 481.0, 0.0, 1.5, sec=self.dend[7])
        h.pt3dadd(-106.5, 516.5, 0.0, 1.5, sec=self.dend[7])
        h.pt3dadd(-142.0, 552, 0.0, 1.5, sec=self.dend[7])

        h.pt3dclear(sec=self.dend[8])	
        h.pt3dadd(-142.0, 552, 0.0, 1.0, sec=self.dend[8])
        h.pt3dadd(-159.7, 569.7, 0.0, 1.0, sec=self.dend[8])
        h.pt3dadd(-177.4, 587.4, 0.0, 1.0, sec=self.dend[8])
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

#shape_window = h.PlotShape()
#shape_window.exec_menu('Show Diam')

