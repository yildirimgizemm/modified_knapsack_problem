### GIZEM YILDIRIM 


import numpy as np
import pandas as pd
import math
rnd = np.random
rnd.seed(100)
import copy
from importlib import reload
from allfunctions_gizem_yildirim_hw2 import initial_solution, my_profit, crossover, reversion

#%% Main Script

# Problem Definition
MaxIt = 1000
nItems = 60 # number of items
items = []
totalWeight = 0
totalArea = 0
populationSize = 30 # can be any number
crossOverRange = math.ceil(populationSize * 0.40) # 40% of Population size
reversionRange = math.ceil(populationSize * 0.60) # 60% of population size  

for i in range(nItems):
    tempWeight = int(2 + (10-2)*np.random.random()) # Generate random numbers between [2,10]
    tempValue = int(12 + (20-12)*np.random.random()) # Generate random numbers between [12,20]
    tempArea = 2 + (10-2)*np.random.random() # Generate floats between [2,10]
    items.append([tempWeight,tempValue,tempArea])
    totalWeight += tempWeight
    totalArea += tempArea
    
bagWeight = round(0.6 * totalWeight,2)
bagArea = round(0.4 * totalArea,2)

# Create Initial Solutions
population = initial_solution(populationSize, nItems)

# Calculate the Profit of each entry of the population
newPopulation = []
for i in range(populationSize):
    profit, feasible = my_profit(population[i],items,bagWeight, bagArea)
    newPopulation.append([population[i],profit,feasible])

# Update the population    
population = copy.deepcopy(newPopulation)    

# Main
bestProfit = 0
bestProfitFeasible = 0
bestFeasibleSolution = 0
for i in range(len(population)):
    if population[i][1] > bestProfit:
        bestProfit = population[i][1]
        if population[i][2]==1:
            bestProfitFeasible = 1
            
for iteration in range(MaxIt):

    # Crossover
    for iteration1 in range(crossOverRange):
        # Tournoment # RolletteWheel
        parent1 = population[int(np.random.random()*len(population))]
        parent2 = population[int(np.random.random()*len(population))]
        child1, child2 = crossover(parent1, parent2, items, bagWeight, bagArea)
        population.append(child1)
        population.append(child2)
        
    # Reversion
    for iteration1 in range(reversionRange):
        parent = population[int(np.random.random()*len(population))]
        child = reversion (parent, items, bagWeight,bagArea)
        population.append(child)
    
    # Sort and Truncate
    population.sort(key = lambda x:x[1])
    population = population [::-1]
    population = population[:populationSize]
    for i in range(len(population)):
        if population[i][2]==1: # is feasible
            bestFeasibleSolution = population[i][1]
            break
    bestProfit = population[0][1]
    bestProfitFeasible = population[0][2] # 0 or 1 binary
    if bestProfitFeasible == 1:
        feasiblity = '*'
    else:
        feasiblity = ' '
    print("The best profit so far is: " + str(bestProfit)+" The best feasible profit is: " + str(bestFeasibleSolution))
    #print(str(bestProfit) + feasiblity)