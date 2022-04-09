"""
Hill Climbing

Student name: Daniel Carpenter & Kyle (Chris) Ferguson
Date: April 2022
"""

# Do Not change:
#   random number generator
#   number of items (should be 150)
#   random problem instance
#   weight limit of the knapsack

# =============================================================================
# INPUTS - Do not change
# =============================================================================

# Import python libraries
from random import Random  # need this for the random number generation -- do not change
import numpy as np


# Set the seet 
seed = 51132021
myPRNG = Random(seed)

# to get a random number between 0 and 1, use this:             myPRNG.random()
# to get a random number between lwrBnd and upprBnd, use this:  myPRNG.uniform(lwrBnd,upprBnd)
# to get a random integer between lwrBnd and upprBnd, use this: myPRNG.randint(lwrBnd,upprBnd)

n = 150 # number of elements in a solution

# create an "instance" for the knapsack problem
value = []
for i in range(0, n):
    value.append(round(myPRNG.triangular(150, 2000, 500), 1))

weights = []
for i in range(0, n):
    weights.append(round(myPRNG.triangular(8, 300, 95), 1))

# define max weight for the knapsack
maxWeight = 2500


# =============================================================================
# EVALUATE FUNCTION - evaluate a solution x
# =============================================================================

# monitor the number of solutions evaluated
solutionsChecked = 0

# function to evaluate a solution x
def evaluate(x, r):

    itemInclusionList = np.array(x)
    valueOfItems      = np.array(value)
    weightOfItems     = np.array(weights)

    totalValue  = np.dot(itemInclusionList, valueOfItems)   # compute the value of the knapsack selection
    totalWeight = np.dot(itemInclusionList, weightOfItems)  # compute the weight value of the knapsack selection

    # Handling infeasibility --------------------------------------------------
    
    # If the total weight exceeds the max allowable weight, then 
    if totalWeight > maxWeight:
        
        # Randomly remove ann item. If not feasible, then try evaluating again until feasible
        randIdx = myPRNG.randint(0,n-1) # generate random item index to remove
        x[r] = 0                        # Don't include the index r from the knapsack
        evaluate(x, r=randIdx)          # Try again on the next to last element
        
    else: 
        # Finish the process if the total weight is satisfied
        # (returns a list of both total value and total weight)
        return [totalValue, totalWeight]
        
    # returns a list of both total value and total weight
    return [totalValue, totalWeight]


# =============================================================================
# NEIGHBORHOOD FUNCTION - simple function to create a neighborhood
# =============================================================================

# 1-flip neighborhood of solution x
def neighborhood(x):

    nbrhood = [] 

    # Set up n number of neighbors with list of lists
    for i in range(0, n):
        nbrhood.append(x[:])
        
        # Flip the neighbor from 0 to 1 or 1 to 0
        if nbrhood[i][i] == 1:
            nbrhood[i][i] = 0
        else:
            nbrhood[i][i] = 1

    return nbrhood


# =============================================================================
# INITIAL SOLUTION FUNCTION - create the initial solution
# =============================================================================

# create a feasible initial solution
def initial_solution():

    x = [] # empty list for x to hold binary values indicating if item i is in knapsack

    # Create a initial solution for knapsack (Could be infeasible), by 
    # randomly create a list of binary values from 0 to n. 1 if item is in the knapsack
    for item in range(0, n):
        x.append(myPRNG.randint(0,1))
        
    totalWeight = np.dot(np.array(x), np.array(weights)) # Sumproduct of weights and is included
    
    
    # While the bag is infeasible, randomly remove items from the bag.
    # Stop once a feasible solution is found.
    knapsackSatisfiesWeight = totalWeight <= maxWeight # True if the knapsack is a feasible solution, else false

    while not knapsackSatisfiesWeight:
        
        randIdx = myPRNG.randint(0,n-1) # Generate random index of item in knapsack and remove item
        x[randIdx] = 0
        
        # If the knapsack is feasible, then stop the loop and go with the solution
        totalWeight = np.dot(np.array(x), np.array(weights)) # Recalc. Sumproduct of weights and is included
        if (totalWeight <= maxWeight):
            knapsackSatisfiesWeight = True

    return x


"""
===============================================================================
Question 5 - Hill Climbing with Random Walk , using *BEST* Acceptance
===============================================================================
"""

# Function that performs hill climb with random walk, using best acceptance method.
# There is a probability of p to either hill climb or go on a random walk
# Binomial experiment chosen since it models a probability of success or failure,
# in this case a succuss is considered continuing to climb the hill and search 
# for better solution. Failure is going on a random walk.

def hillClimbRandWalk(probOfClimb=0.50): # default probability 50%
    
    ## GET INITIAL SOLUTION -------------------------------------------------------
    
    # variable to record the number of solutions evaluated
    solutionsChecked = 0
    
    x_curr = initial_solution()  # x_curr will hold the current solution
    x_best = x_curr[:]  # x_best will hold the best solution
    
    r = randIdx = myPRNG.randint(0,n-1) # a random index
    
    # f_curr will hold the evaluation of the current soluton
    f_curr = evaluate(x_curr, r)
    f_best = f_curr[:]
    
    
    ## BEGIN LOCAL SEARCH LOGIC ---------------------------------------------------
    done = 0
    
    while done == 0:
    
        # create a list of all neighbors in the neighborhood of x_curr
        Neighborhood = neighborhood(x_curr)
    
        for s in Neighborhood:  # evaluate every member in the neighborhood of x_curr
            solutionsChecked = solutionsChecked + 1
            if evaluate(s, r)[0] > f_best[0]:
                
                # find the best member and keep track of that solution
                x_best = s[:]
                f_best = evaluate(s, r)[:]  # and store its evaluation
                
        # Checks for platueau and feasibility
        if f_best == f_curr and (f_curr[1] < maxWeight):  # if there were no improving solutions in the neighborhood
                    
            # 1 if take hill climb path, 0 if take random walk path
            # Binomial chosen since gives result given probability of success
            takeHillClimbPath = np.random.binomial(1, probOfClimb, 1) 
    
            # If the binomial experiment choses to take the hill clim path,
            # then we know we are done. Else, choose a random neighbor
            if takeHillClimbPath == 1:
                done = 1
            
        
        else:
            x_curr = x_best[:]  # else: move to the neighbor solution and continue
            f_curr = f_best[:]  # evalute the current solution
    
            # Commented out just to keep the output cleaner
            # print("\nTotal number of solutions checked: ", solutionsChecked)
            # print("Best value found so far: ", f_best)
    
    print("\nFinal number of solutions checked: ", solutionsChecked, '\n',
          "Best value found: ", f_best[0], '\n',
          "Weight is: ", f_best[1], '\n',
          "Total number of items selected: ", np.sum(x_best), '\n\n',
          "Best solution: ", x_best)

# Call the function, given the probability to hill climb (rather than random walk)
hillClimbRandWalk(probOfClimb=0.50)

