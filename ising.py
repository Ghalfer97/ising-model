#! /usr/lib/bin/python

import params
import lattice
import simulation
import testing
import matplotlib.pyplot as plt


# create lattice
lat = lattice.Lattice(params.D, params.L)

#simulate range of temperatures
results = simulation.Results()
simulation.run_simulation(lat, results)
#simulation.curie_temp(results, 2)

results.plot_energy()
results.plot_magnetisation()
results.plot_mag_susc()
results.plot_heat_cap()
results.curie_temp()

#results.plot_curie_temps()


testing.run_all_tests()

