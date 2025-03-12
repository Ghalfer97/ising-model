import lattice
import numpy as np

#pnt is the index of the spin whose interactions
#we are measuring
#J is defined on the links of the lattice
#we 'associate' the links extending from each point
#in the positive direction of each dimension
#with that point in memory (i.e the links are contiguous in the array
#and there are D times as many of them as spins)
#So when pnt is interacting with it's neighbour in a negative
#direction, we use an index in the J array associated with
#the neighbour. In the positive direction we use it's 'own'
def H_loc(lat, pnt): #local Hamiltonian contribution
        pnt = int(pnt)
        spin_sum = 0
        # nead to sum nearest neighbours in each dimension
        # also need to resolve periodic boundary conditions
        for i in range(lat.D):
                # In the negative direction of dimension i
                if(pnt%(lat.traverse[i]*lat.L[i]) < lat.traverse[i]): # negative direction pbc
                        neighbour = pnt + (int(lat.L[i] - 1))*lat.traverse[i]
                        spin_sum += lat.J[lat.D*neighbour + i]*lat.sigma[neighbour]
                else:
                        neighbour = pnt - lat.traverse[i]
                        spin_sum += lat.J[lat.D*neighbour + i]*lat.sigma[neighbour]
                
                # In the positive direction of dimension i
                if((pnt + lat.traverse[i])%(lat.traverse[i]*lat.L[i]) < lat.traverse[i]): # positive direction pbc
                        spin_sum += lat.J[lat.D*pnt + i]*lat.sigma[pnt - (int(lat.L[i] - 1))*lat.traverse[i]]
                else:
                        spin_sum += lat.J[lat.D*pnt + i]*lat.sigma[pnt + lat.traverse[i]]

        return -1.0*lat.sigma[pnt]*spin_sum - lat.h[pnt]*lat.sigma[pnt]

def H(lat):
        sum = 0
        for i in range(lat.size):
                sum += H_loc(lat, i)

        return sum/2

def energy_dif(lat, pnt):
        pnt = int(pnt)
        spin_sum = 0

        # nead to sum nearest neighbours in each dimension
        # also need to resolve periodic boundary conditions
        for i in range(lat.D):
                if(pnt%(lat.traverse[i]*lat.L[i]) < lat.traverse[i]): # negative direction pbc
                        neighbour = pnt + (int(lat.L[i] - 1))*lat.traverse[i]
                        spin_sum += lat.J[lat.D*neighbour + i]*lat.sigma[neighbour]
                else:
                        neighbour = pnt - lat.traverse[i]
                        spin_sum += lat.J[lat.D*neighbour + i]*lat.sigma[neighbour]
                if((pnt + lat.traverse[i])%(lat.traverse[i]*lat.L[i]) < lat.traverse[i]): # positive direction pbc
                        spin_sum += lat.J[lat.D*pnt + i]*lat.sigma[pnt - (int(lat.L[i] - 1))*lat.traverse[i]]
                else:
                        spin_sum += lat.J[lat.D*pnt + i]*lat.sigma[pnt + lat.traverse[i]]

        return 2.0*lat.sigma[pnt]*spin_sum + 2.0*lat.h[pnt]*lat.sigma[pnt]

def magnetisation(lat):
        return float(abs(np.sum(lat.sigma)))/float(lat.size)

#returns the variance of array x
#used for heat capacity and magnetic susceptibility
def variance(x):
	mean = 0.0
	for i in range(len(x)):
		mean += x[i]
	
	mean /= len(x)

	var = 0
	for i in range(len(x)):
		var += (x[i] - mean)**2

	return var/len(x)
