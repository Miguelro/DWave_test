import dimod

#Example took from here: https://quantumcomputing.stackexchange.com/questions/1451/how-do-you-write-a-simple-program-for-a-d-wave-device
J = {(0,1): 1, (0,2): 1, (1,3): 1, (2,3): 1} #Links
h = [-1,0,0,0] #Bias

exactsolver = dimod.ExactSolver()

bqm = dimod.BinaryQuadraticModel.from_ising(h,J,offset=-1.0)
results = exactsolver.sample(bqm)

#print the results
print(results)
#print the energy of a particular state
print(bqm.energy({0: 1, 1: -1, 2:-1,3:-1}))
print(bqm.energy({0: 1, 1: -1, 2:-1,3:1}))


