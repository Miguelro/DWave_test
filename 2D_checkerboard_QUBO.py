import dimod

exactsolver = dimod.ExactSolver()

#Define Q matrix
#Q = {(0,0):-1, (0,1):0.5, (0,2):0.5, (1,0):0.5, (1,1):-1, (1,3):0.5, (2,0):0.5, (2,2):-1, (2,3):0.5, (3,1):0.5, (3,2):0.5, (3,3):-1}
Q = {(0,0):-1, (0,1):1, (0,2):1, (1,1):-1, (1,3):1, (2,2):-1, (2,3):1, (3,3):-1}


bqm = dimod.BinaryQuadraticModel.from_qubo(Q,offset=0.0)
results = exactsolver.sample(bqm)

#print the results
for smpl, energy in results.data(['sample', 'energy']):
    print(smpl, energy)

print(bqm.energy({0: 0, 1: 1, 2: 1, 3: 0}))
print(bqm.linear)