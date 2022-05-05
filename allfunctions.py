### ### GIZEM YILDIRIM

import numpy as np


def initial_solution(populationSize: int, nItems: int) -> list:
    """ Here we generate random solutiins"""
    population = []
    for i in range(populationSize):
        temp = []
        for j in range(nItems):
            if np.random.random()>0.5:
                temp.append(1)
            else:
                temp.append(0)
        population.append(temp)
    return(population)

def my_profit(mylist: list, items: list, bagWeight: float, bagArea: float) -> float:
    """ Here we calculate the cost of the solutions we have"""
    profit = 0
    weight = 0
    area = 0
    feasible = 1
    for i in range(len(mylist)):
        profit += mylist[i]*items[i][1]
        weight += mylist[i]*items[i][0]
        area += mylist[i]*items[i][2]
        
    if weight > bagWeight and area > bagArea:
        feasible = 0
        profit = profit - 1 * (weight-bagWeight)
    elif weight < bagWeight and area < bagArea:
        feasible = 0
        profit = profit - 1 * (weight+bagArea)
    elif weight > bagWeight and area < bagArea:
        feasible = 0
        profit = profit - 1 * (weight-bagWeight+bagArea)
        
   
    if mylist[1] == 0: # if item 2 whose index is 1 is equal to zero, infeasible
        feasible = 0
    elif mylist[9] == 1 : # if item 10 whose index is 9 is equal to one, infeasible
        feasible = 0
    elif sum(mylist) < 4 : # if there are less than 4 items in the fag, infeassible
        feasible = 0
    
        #profit = max(profit, 0)       
    return(profit,feasible)

def crossover(parent1: list, parent2: list, items: list, bagWeight: float, bagArea: float)-> (list, list):
    """Using the operator of crossover we want to have two new children"""
    place2cut = int(np.random.random()*len(parent1[0]))
    child1 = parent1[0][:place2cut]
    child1.extend(parent2[0][place2cut:])
    profit, feasible = my_profit(child1, items, bagWeight, bagArea)
    newchild1= [child1, profit, feasible]
    
    child2 = parent2[0][:place2cut]
    child2.extend(parent1[0][place2cut:])
    profit, feasible = my_profit(child2, items, bagWeight, bagArea)
    newchild2= [child2, profit, feasible]    
    
    return(newchild1,newchild2)

def reversion(parent: list, items: list, bagWeight: float, bagArea: float) -> (list):
    """This function reverses the choromosome of the parent and produces a new child"""
    child = parent[0]
    child.reverse()
    profit, feasible = my_profit(child, items, bagWeight, bagArea)
    newchild = [child, profit, feasible]
    
    return(newchild)
    