params.py
This script initialises the variables used in creating the Ising Model

lattice.py
This script initialises the lattice structure in the dimensions given in params.py
It randomises the number of positively/negatively charged spins within the lattice structure
Sets the interaction and field strengths based on the lattice structure that has been realised

simulation.py
This script plots all our results against a linearly changing temperature value set in params.py
Applies the formulae in measurement.py and calculates the ferromagnetic changes to the lattice based off the number of sweeps and Monte Carlo samples defined in params.py

measurement.py
Defines all the formulae used in the Ising model to calculate the results of the Ising Model.
This includes the local hamiltonian contribution, the hamiltonian contribution, the change in energy, magnetisation, and variance

testing.py
This script is testing the behaviour of the ferromagnetic, anti-ferromagnetic, and non-interacting Ising Model.

ising.py
This is the main script which calls all other scripts and outputs our results
