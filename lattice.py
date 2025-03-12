#! /usr/lib/bin/python
import numpy as np
import random as rand
import matplotlib.pyplot as plt

# arbitrary dimensional lattice object
# Functions do (in order):
#	initialisation
#	randomise spins
#	cold start - all ones
#	print lattice
#	change strength of interactions
#	change strength of external field
class Lattice:
	def __init__(lat, Dims, Lengths):
		lat.D = Dims
		lat.L = np.zeros(Dims)
		if(len(Lengths) != Dims):
			print('Incorrect number of lengths provided, using the first element for each side')
			for i in range(Dims):
				lat.L[i] = int(Lengths[0])
		else:
			for i in range(Dims):
				lat.L[i] = int(Lengths[i])

		# entire lattice, regardless of dimension
		# is stored in a 1-d array
		# traverse is used for accessing elements
		# by storing the number of elements in the
		# array that exist between succesive spins
		# in a given dimension
		lat.traverse = np.zeros(Dims, dtype=int)
		offset = 1
		for i in range(Dims):
			lat.traverse[i] = offset
			offset = int(Lengths[i]*offset)
		
		lat.size = offset # total number of spins
		
		lat.sigma = np.zeros(lat.size, dtype=int)
		#default J = 1, h = 0
		lat.J = np.ones(Dims*lat.size, dtype=int)
		lat.h = np.zeros(lat.size, dtype=int)
		
	def randomise(lat):
		for i in range(lat.size):
			lat.sigma[i] = rand.randint(1, 2) # one or two
			if(lat.sigma[i] == 2):
				lat.sigma[i] = -1

	def cold_start(lat):
		lat.sigma = np.ones(lat.size, dtype=int)

	def print_lat(lat):
		if(lat.D == 2): 
			grid = lat.sigma.reshape(int(lat.L[0]), int(lat.L[1]))
			plt.imshow(grid, vmin=-1, vmax=1)
		else:
			#for printing more than 2-dimensional lattices
			#line break for each movement through a dimension (except 0th)
			#These are compounded so movement through 3rd dimension
			#is represented by two linebreaks
			for i in range(lat.size):
				print(lat.sigma[i])
				offset = 1
				for j in range(lat.D):
					offset *= lat.L[j]
					if((i+1)%offset == 0):
						print('\n')
	def set_J(lat, Js):
		if(len(Js) != lat.D*lat.size):
			print('incorrect number of interaction strengths provided')
			return
		for i in range(lat.D*lat.size):
			lat.J[i] = Js[i]
			
	def set_h(lat, hs):
		if(len(hs) != lat.size):
			print('incorrect number of field strengths provided')
			return
		for i in range(lat.size):
			lat.h[i] = hs[i]
