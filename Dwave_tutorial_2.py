import dimod

exactsolver = dimod.ExactSolver()

Q = {(0,0):-16, (0,1):2, (0,2):2, (0,3):2, (0,4):2, 
     (1,1):-15, (1,2):2, (1,3):2, (1,4):2,
     (2,2):-14, (2,3):2, (2,4):2,
     (3,3):-13, (3,4):2,
     (4,4):-12}


bqm = dimod.BinaryQuadraticModel.from_qubo(Q,offset=0.0)
results = exactsolver.sample(bqm)

#print the results
for smpl, energy in results.data(['sample', 'energy']):
    print(smpl, energy)

print(bqm.energy({0: 1, 1: 0, 2: 1, 3: 1, 4:0}))
print(bqm.linear)