# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 14:47:26 2018

@author: janniez
"""

import numpy
import simrun
from detailed_cell import DetailedCell
from neuron import h
from matplotlib import pyplot
from math import sin, cos, pi

cells = []
N = 5
r = 50 # Radius of cell locations from origin (0,0,0) in microns
for i in range(N):
    cell = DetailedCell()
    # When cells are created, the soma location is at (0,0,0) and
    # the dendrite extends along the X-axis.
    # First, at the origin, rotate about Z.
    cell.rotateZ(i*2*pi/N)
    # Then reposition
    x_loc = cos(i * 2 * pi / N) * r
    y_loc = sin(i * 2 * pi / N) * r
    cell.set_position(x_loc, y_loc, 0)
    cells.append(cell)


shape_window = h.PlotShape()
shape_window.exec_menu('Show Diam')


stim = h.NetStim() # Make a new stimulator

# Attach it to a synapse in the middle of the dendrite
# of the first cell in the network. (Named 'syn_' to avoid
# being overwritten with the 'syn' var assigned later.)
syn_ = h.ExpSyn(cells[0].dend[0](0.5))

stim.number = 1
stim.start = 9
ncstim = h.NetCon(stim, syn_)
ncstim.delay = 1
ncstim.weight[0] = 0.04 # NetCon weight is a vector.

#changing the tau to decay by 2 ms
syn_.tau = 2

#plot
soma_v_vec, dend_v_vec, t_vec = simrun.set_recording_vectors(cells[0])
simrun.simulate()
simrun.show_output(soma_v_vec, dend_v_vec, t_vec)
pyplot.show()

# Set recording vectors
syn_i_vec = h.Vector()
syn_i_vec.record(syn_._ref_i)

simrun.simulate()

# Draw
fig = pyplot.figure(figsize=(8,4))
ax1 = fig.add_subplot(2,1,1)
soma_plot = ax1.plot(t_vec, soma_v_vec, color='black')
dend_plot = ax1.plot(t_vec, dend_v_vec, color='red')
rev_plot = ax1.plot([t_vec[0], t_vec[-1]], [syn_.e, syn_.e],
        color='blue', linestyle=':')
ax1.legend(soma_plot + dend_plot + rev_plot,
        ['soma', 'dend[0](0.5)', 'syn reversal'])
ax1.set_ylabel('mV')
ax1.set_xticks([]) # Use ax2's tick labels

ax2 = fig.add_subplot(2,1,2)
syn_plot = ax2.plot(t_vec, syn_i_vec, color='blue')
ax2.legend(syn_plot, ['synaptic current'])
ax2.set_ylabel(h.units('ExpSyn.i'))
ax2.set_xlabel('time (ms)')
pyplot.show()

#connect axons from cell n to a synapse
nclist = []
syns = []
for i in range(N):
    src = cells[i]
    tgt = cells[(i + 1) % N]
    syn = h.ExpSyn(tgt.dend[0](0.5))
    syns.append(syn)
    nc = h.NetCon(src.soma(0.5)._ref_v, syn, sec=src.soma)
    nc.weight[0] = 0.05
    nc.delay = 5
    nclist.append(nc)
    syn_.e = -60
    """
    for seg in soma:
        seg.hh.gnabar = 10
        seg.hh.gkbar = 10
        seg.hh.gl = 10
        seg.hh.el = 10
    """
        
soma_v_vec, dend_v_vec, t_vec = simrun.set_recording_vectors(cells[0])
simrun.simulate(tstop=100)
simrun.show_output(soma_v_vec, dend_v_vec, t_vec)
pyplot.show()

#recording the spike times
spike_times = [h.Vector() for nc in nclist]
for nc, spike_times_vec in zip(nclist, spike_times):
    nc.record(spike_times_vec)

simrun.simulate(tstop=100)

#print the results
for i, spike_times_vec in enumerate(spike_times):
    print('cell {}: {}'.format(i, list(spike_times_vec)))


#visualizing raster plots
pyplot.figure()
for i, spike_times_vec in enumerate(spike_times):
    pyplot.vlines(spike_times_vec, i + 0.5, i + 1.5)
pyplot.show()




































