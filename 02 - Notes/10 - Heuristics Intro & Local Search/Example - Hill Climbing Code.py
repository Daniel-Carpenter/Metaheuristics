#basic hill climbing search provided as base code for the DSA/ISE 5113 course
#author: Charles Nicholson
#date: 4/5/2017

#NOTE: YOU MAY CHANGE ALMOST ANYTHING YOU LIKE IN THIS CODE.  
#However, I would like all students to have the same problem instance, therefore please do not change anything relating to:
#   random number generation
#   number of items (should be 100)
#   random problem instance
#   weight limit of the knapsack

#------------------------------------------------------------------------------

#Student name:  Solutions for 2022
#Date: April 13, 2022


#need some python libraries
#import copy
from random import Random   #need this for the random number generation -- do not change
import numpy as np
#import math
#from math import *
import operator as op
from functools import reduce


#to setup a random number generator, we will specify a "seed" value
#need this for the random number generation -- do not change
seed = 51132021
myPRNG = Random(seed)

#to get a random number between 0 and 1, use this:             myPRNG.random()
#to get a random number between lwrBnd and upprBnd, use this:  myPRNG.uniform(lwrBnd,upprBnd)
#to get a random integer between lwrBnd and upprBnd, use this: myPRNG.randint(lwrBnd,upprBnd)

#number of elements in a solution
n = 150

#create an "instance" for the knapsack problem
value = []
for i in range(0,n):
    #value.append(round(myPRNG.expovariate(1/500)+1,1))
    value.append(round(myPRNG.triangular(150,2000,500),1))
    
weights = []
for i in range(0,n):
    weights.append(round(myPRNG.triangular(8,300,95),1))
    
#define max weight for the knapsack
maxWeight = 2500

#change anything you like below this line ------------------------------------

#monitor the number of solutions evaluated
solutionsChecked = 0

#function to evaluate a solution x
def evaluate(x):
          
    a=np.array(x)
    b=np.array(value)
    c=np.array(weights)
    
    totalValue = np.dot(a,b)     #compute the value of the knapsack selection
    totalWeight = np.dot(a,c)    #compute the weight value of the knapsack selection
    
    
    #using a penalty structure --- you can change the penalty weight
    if totalWeight > maxWeight:
        totalValue = 0.85*totalValue - 10*(totalWeight - maxWeight)**2

    return [totalValue, totalWeight]   #returns a list of both total value and total weight
       
          
       
#simple function to create a neighborhood: 1-flip neighborhood of solution x         
def neighborhood(x):
        
    nbrhood = []     
    
    for i in range(0,n):
        nbrhood.append(x[:])
        if nbrhood[i][i] == 1:
            nbrhood[i][i] = 0
        else:
            nbrhood[i][i] = 1
      
    return nbrhood

        
 
     
     
#function to print out results
def output(methodName, solutionsChecked, finalVal, finalWt, finalQty, finalSol):
    print (methodName , "------------\n")
    print ("Final number of solutions checked: ", solutionsChecked)
    print ("Best value found: ", finalVal)
    print ("Weight is: ", finalWt)
    print ("Total number of items selected: ", finalQty)
    print ("Best solution: ", finalSol, "\n\n")



#create the initial solution
def initial_solution(probIncluded):
    x = []   #i recommend creating the solution as a list
    
    for i in range(0, n):
        if myPRNG.random() < probIncluded:       
            x.append(1)
        else: 
            x.append(0)
        
    return x


#creates initial solution and evaluates it
def initialize_search(probIncluded):

    x_curr = initial_solution(probIncluded)  #x_curr will hold the current solution 
    x_best = x_curr[:]           #x_best will hold the best solution 
    f_curr = evaluate(x_curr)    #f_curr will hold the evaluation of the current soluton 
    f_best = f_curr[:]    
    
    return x_curr, x_best, f_curr, f_best 
   


#core of hill climbing logic -- performs one iteration of the hill climbing search, but does not "move" to the new solution
#can use either "first accept" or "best accept"
def hill_climbing_iteration(x_curr, x_best, f_curr, f_best, method="B" ):
        
    if method == "B": methodName = "Hill Climbing - Best Accept"
    elif method == "F": methodName = "Hill Climbing - First Accept"
        
    Neighborhood = neighborhood(x_curr[:])       #creates the neighborhood of the current solution x_curr
    solutionsChecked = 0
    for s in Neighborhood:                       #evaluate every member in the neighborhood of x_curr
        solutionsChecked = solutionsChecked + 1
        currentEval = evaluate(s)
        if currentEval[0] > f_best[0]:   
            x_best = s[:]                 #find the best member and keep track of that solution
            f_best = currentEval[:]       #and store its evaluation 
                    
            if method == "F": break       #if "First Accept", then do not look through the remainder of the neighborhood
                
    return [x_best[:], f_best[:], solutionsChecked]    


#hill climber: primary method for hill climbing 
# initializes the search -- the probability value is used to setup the initial solution 
# -- calls the "hill climber iteration" method which performs one iteration of the hill climbing search
#can use either "first accept" or "best accept"
def hill_climber(method="B", probability=0.1, printOutput=True):
    
    if method == "B": methodName = "Hill Climbing - Best Accept"
    elif method == "F": methodName = "Hill Climbing - First Accept"
    
    done = 0
    solutionsChecked = 0
    x_curr, x_best, f_curr, f_best = initialize_search(probability)    
    
    while done == 0:
        
        x_curr, f_best, sols = hill_climbing_iteration(x_curr[:], x_best[:], f_curr[:], f_best[:], method)
                   
        solutionsChecked = solutionsChecked + sols
        if f_best == f_curr:           #if there were no improving solutions in the neighborhood
            done = 1
        else:
            f_curr = f_best[:]
            
    if printOutput: output(methodName, solutionsChecked, f_best[0], f_best[1], np.sum(x_best),  x_best)
    return [x_curr, f_best, solutionsChecked]
        
        
#hill climbing with random restarts, K = number of restarts
def hill_climbing_randomRestarts(method, probability=0.1, K=10):
    
    if method == "B": methodName = "Hill Climbing w/Random Restarts (" +  str(K) + ") - Best Accept"
    elif method == "F": methodName = "Hill Climbing w/Random Restarts (" + str(K) + ") - First Accept"
    
    xR, fR, solutionsChecked = hill_climber(method, probability, False)
    
    x_best = xR[:]
    f_best = fR[:]    
    
    for i in range(K-1):
        xR, fR, sols = hill_climber(method, probability, False)
        solutionsChecked = solutionsChecked + sols
        
        if fR[0] > f_best[0]: 
            f_best = fR[:]
            x_best = xR[:]
        
    output(methodName, solutionsChecked, f_best[0], f_best[1], np.sum(x_best),  x_best)
  


#choosing a and evaluating a random neighbor of x from a 1-flip neighborhood    -- use with the random walk function
def randomNeighbor(x):

    newX = myPRNG.choice(neighborhood(x[:]))[:]
    currentEval = evaluate(newX)
    
    return [newX[:], currentEval[:], 1]    



#stopping criterion is based on a mininum number of solutions to check
#also requires a "randomWalk" probability (defualted to 0.5)
def hill_climber_randomwalk(method="B", probability=0.1, randomWalkprob=0.5, solutionsToCheck=1000, printOutput=True):
    
    if method == "B": methodName = "Hill Climbing with Random Walk - Best Accept"
    elif method == "F": methodName = "Hill Climbing with Random Walk - First Accept"
    
    done = 0
    solutionsChecked = 0
    x_curr, x_best, f_curr, f_best = initialize_search(probability)    

    while done == 0:
          
        #with certain probability perform random walk
        if myPRNG.random() < randomWalkprob:
            
            x_curr, f_curr, sols = randomNeighbor(x_curr)
            solutionsChecked = solutionsChecked + sols
            
            if f_curr[0] > f_best[0]: 
                f_best = f_curr[:]
                x_best = x_curr[:]    
        
        #otherwise, perform a hill climbing iteration
        else:
    
            x_curr, f_curr, sols = hill_climbing_iteration(x_curr[:], x_best[:], f_curr[:], f_best[:], method)
            solutionsChecked = solutionsChecked + sols
            
            if f_curr[0] > f_best[0]: 
                f_best = f_curr[:]
                x_best = x_curr[:]         

        #manage stopping condition
        if solutionsChecked >= solutionsToCheck:
            done = 1

    if printOutput: output(methodName, solutionsChecked, f_best[0], f_best[1], np.sum(x_best),  x_best)
    return [x_curr, f_best, solutionsChecked]



def main():
    print ("start....")
        
    #some examples with 'first accept'
    hill_climber("F", probability = 0.25)
    hill_climbing_randomRestarts("F", probability = 0.25, K=200)
    hill_climber_randomwalk(method="F", probability=0.25, randomWalkprob=0.5, solutionsToCheck=15000, printOutput=True)   
          
    #some examples with 'best accept'
    hill_climber("B", probability = 0.25)
    hill_climbing_randomRestarts("B", probability = 0.25, K=100)
    hill_climber_randomwalk(method="B", probability=0.25, randomWalkprob=0.5, solutionsToCheck=15000, printOutput=True)
    

if __name__ == "__main__":
    main()









         
        


