import lattice
import simulation
import random as rand
import numpy as np
import matplotlib.pyplot as plt

def ferromagnetic():
	D = 2
	Ls = [40, 40]
	latt = lattice.Lattice(D, Ls)
	latt.randomise()
	latt.set_J(np.ones(latt.D*latt.size))
	print ('Evolving low temperature, ferromagnetic lattice towards equilibrium...')
	for i in range(100):
		simulation.metrosweep(latt)
	
	print ('Should tend to be uniform')
	latt.print_lat()
	print ('Done.')
	plt.show()

def anti_ferromagnetic():
	D = 2
	Ls = [40, 40]
	latt = lattice.Lattice(D, Ls)
	latt.randomise()
	latt.set_J(-1.0*np.ones(latt.D*latt.size))
	print ('Evolving low temperature, anti-ferromagnetic lattice towards equilibrium...')
	for i in range(100):
			simulation.metrosweep(latt)

	print ('Should tend to be non-uniform')
	latt.print_lat()
	print ('Done.')
	plt.show()

def non_zero_h():
	D = 2
	Ls = [40, 40]
	latt = lattice.Lattice(D, Ls)
	latt.randomise()
	latt.set_h(np.ones(latt.size))
	print ('Evolving low temperature lattices with non-zero external field...')
	print ('First Positive...')
	for i in range(100):
		simulation.metrosweep(latt)

	print (latt.sigma)
	plt.figure(1)
	latt.print_lat()
	print ('Then negative..')
	latt.randomise()
	latt.set_h(-1.0*np.ones(latt.size))
	print ('Should be dominated by opposite spins as one another')
	for i in range(100):
		simulation.metrosweep(latt)

	print (latt.sigma)
	plt.figure(2)
	latt.print_lat()
	print ('Done.')
	plt.show()

def non_uniform_J():
	D = 2
	Ls = [40, 40]
	latt = lattice.Lattice(D, Ls)
	latt.randomise()
	Js = np.zeros(latt.D*latt.size)
	for i in range(latt.D*latt.size):
		Js[i] = rand.uniform(-1, 1) 

	latt.set_J(Js)
	print ('Evolving low temperature lattice with non-uniform, random interaction strengths...')
	for i in range(100):
		simulation.metrosweep(latt)

	latt.print_lat()
	print ('Done.')
	plt.show()

def non_uniform_h():
	D = 2
	Ls = [40, 40]
	latt = lattice.Lattice(D, Ls)
	latt.randomise()
	hs = np.zeros(latt.size)
	for i in range(latt.size):
		hs[i] = rand.uniform(-1, 1)

	latt.set_h(hs)
	print ('Evolving low temperature lattice with non-uniform random external field...')
	for i in range(100):
		simulation.metrosweep(latt)

	latt.print_lat()
	print ('Done.')
	plt.show()

def multiple_dimensions():
	print ('Testing successful simulation of different dimensions of lattices')
	for d in range(2, 5):
		lens = 8*np.ones(d, dtype=int)
		latt = lattice.Lattice(d, lens)
		latt.randomise()
		print ('Evolving', d, 'D lattice...')
		for i in range(100):
			simulation.metrosweep(latt)
		
		print ('Done.')

def different_length_sides():
	print ('Testing two cases of random side-length (non-cubic) lattices for each of D=2, D=3, D=4')
	for d in range(2, 5):
		lens = np.ones(d, dtype=int)
	for i in range(d):
		lens[i] *= rand.randint(2, 10)
		latt = lattice.Lattice(d, lens)
	latt.randomise()
	print ('Evolving ', lens, ' lattice')
	for i in range(100):
		simulation.metrosweep(latt)

	print ('Done.')

def run_all_tests():
	print ('Running all tests...')
	ferromagnetic()
	anti_ferromagnetic()
	non_zero_h()
	non_uniform_J()
	non_uniform_h()
	multiple_dimensions()
	different_length_sides()
	print ('All tests complete.')
