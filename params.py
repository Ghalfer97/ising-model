import numpy as np

D = 2 #dimensions
size = 16 #length of dimensions
J = 1.0 #strength of interactions
kb = 1.0 #Boltzmann constant
T = 0.3 #Temperature
beta = 1.0/(kb*T)

MCsweeps = 200 #number of Monte Carlo samples
metroskips = 3 #number of sweeps between samples
transient = 500 #reaching equilibrium

#lattice side lengths
L = np.zeros(D, dtype=int)

#for equal sides
for i in range(D):
        L[i] = size

#temperature range
temps = np.arange(1.3, 3.1, 0.1)
