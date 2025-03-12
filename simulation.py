import params
import measurement
import lattice
import numpy as np
import math
import random as rand
import matplotlib.pyplot as plt
from scipy import stats

class Results:
	def __init__(res):
		res.E = np.zeros(len(params.temps))
		res.M = np.zeros(len(params.temps))
		res.chi = np.zeros(len(params.temps))
		res.Cv = np.zeros(len(params.temps))
		res.curie_temp_Cv = 0.0
		res.curie_temp_chi = 0.0
		res.curie_temps = np.zeros(3)
		res.curie_sample_size = np.zeros(3)

	def plot_energy(res):
		plt.figure()
		plt.title('Lattice Energy vs Temperature')
		plt.xlabel('T')
		plt.ylabel('E')
		plt.plot(params.temps, res.E, 'o')
		plt.show()

	def plot_magnetisation(res):
		plt.figure()
		plt.title('Lattice Absolute Magnetisation vs Temperature')
		plt.xlabel('T')
		plt.ylabel('M')
		plt.plot(params.temps, res.M, 'o')
		plt.show()
	
	def plot_mag_susc(res):
		plt.figure()
		plt.title('Lattice Magnetic Susceptibility vs Temperature')
		plt.xlabel('T')
		plt.ylabel('chi')
		plt.plot(params.temps, res.chi, 'o')
		plt.show()
	
	def plot_heat_cap(res):
		plt.figure()
		plt.title('Lattice Heat Capacity vs Temperature')
		plt.xlabel('T')
		plt.ylabel('Cv')
		plt.plot(params.temps, res.Cv, 'o')
		plt.show()

	def curie_temp(res):
		print ('Curie temperature =', "%.2f" % res.curie_temp_Cv)
		print ('Curie temperature =', "%.2f" % res.curie_temp_chi)

	def plot_curie_temps(res):
		slope, intercept, r_value, p_value, std_err = stats.linregress(res.curie_sample_size,res.curie_temps)
		x = np.arange(0.0, res.curie_sample_size[-1], 0.1)
		fit = slope*x + intercept
		plt.figure()
		plt.title('Curie Temperature for varying lattice sizes')
		plt.xlabel('Tc')
		plt.ylabel('size')
		plt.plot(res.curie_sample_size, res.curie_temps, 'o', x, fit)
		plt.show()

def update(lat, pnt):
	dE = measurement.energy_dif(lat, pnt)
	params.beta
	prob = math.exp(-1.0*params.beta*dE)

	if(rand.uniform(0, 1) < prob):
		lat.sigma[pnt] *= -1

def metrosweep(lat):
	for i in range(lat.size):
		pnt = rand.randint(0, lat.size - 1)
		update(lat, pnt)

# reach equilibrium
def equilibrate(lat):
	for i in range(params.transient):
		metrosweep(lat)

#runs the entire temperature range defined in params
def run_simulation(lat, results):
	print ('Running for temperatures from', "%.1f" % params.temps[0], 'to', "%.2f" % params.temps[-1])
	max_Cv = 0.0
	max_chi = 0.0
	for t in range(len(params.temps)):
		T = params.temps[t]
		params.beta = 1.0/(T*params.kb)

		if(params.temps[t] < ((lat.D - 1.0)*2.2 - 1.0)):
			lat.cold_start()
		else:
			lat.randomise()

		equilibrate(lat)

		energy = 0.0
		mag = 0.0
		Es = np.zeros(params.MCsweeps)
		Ms = np.zeros(params.MCsweeps)
		for i in range(params.MCsweeps):
			for j in range(params.metroskips):
				metrosweep(lat)

			Es[i] = measurement.H(lat)
			energy += Es[i]
			Ms[i] = measurement.magnetisation(lat)
			mag += Ms[i]

		energy /= float(params.MCsweeps)
		mag /= float(params.MCsweeps)
		
		results.E[t] = energy
		results.M[t] = mag

		results.Cv[t] = (params.beta**2)*measurement.variance(Es)
		results.chi[t] = params.beta*measurement.variance(Ms)

		if(results.Cv[t] > max_Cv):
			max_Cv = results.Cv[t]
			results.curie_temp_Cv = params.temps[t]

		if(results.chi[t] > max_chi):
			max_chi = results.chi[t]
			results.curie_temp_chi = params.temps[t]

		print('t = ', "%.2f" % T, 'complete')

#very expensive
#make sure to set appropriate temperature range and accuracy
def curie_temp(results, D):
	print ('Running temperature range for three different lattice sizes...')
	sizes = [4, 8, 16]
	for i in range(len(sizes)):
		lengths = sizes[i]*np.ones(D, dtype=int)
		latt = lattice.Lattice(D, lengths)
		run_simulation(latt, results)
		results.curie_temps[i] = results.curie_temp_Cv
		results.curie_sample_size[i] = 1.0/latt.size
