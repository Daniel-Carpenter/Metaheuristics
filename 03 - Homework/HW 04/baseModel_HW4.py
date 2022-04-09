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

# need some python libraries
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

    # r = -1

    a = np.array(x)
    b = np.array(value)
    c = np.array(weights)

    totalValue  = np.dot(a, b)  # compute the value of the knapsack selection
    totalWeight = np.dot(a, c)  # compute the weight value of the knapsack selection

    # Recurision for handling infeasible solutions
    if totalWeight > maxWeight:
        x[r] = 0            # Don't include the index r from the knapsack
        evaluate(x, r - 1)  # Try again on the next to last element
    else: 
        # Finish the process if the total weight is satisfied
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
    
    # Start with nothing in the knapsack
    x = [0] * n  

    # Random Initial Solution start - this works too, but less optimal:
    # x = []  # i recommend creating the solution as a list

    # # Randomly create a list of binary values from 0 to n    
    # for i in range(0, n):
    #     x.append(myPRNG.randint(0,1))

    return x


# =============================================================================
# DRIVER - Create initial solution and begin local search
# =============================================================================

## GET INITIAL SOLUTION -------------------------------------------------------

# variable to record the number of solutions evaluated
solutionsChecked = 0

x_curr = initial_solution()  # x_curr will hold the current solution
x_best = x_curr[:]  # x_best will hold the best solution

r = -1 # last element in list

# f_curr will hold the evaluation of the current soluton
f_curr = evaluate(x_curr, r)
f_best = f_curr[:]


## BEGIN LOCAL SEARCH LOGIC ---------------------------------------------------
done = 0

while done == 0:
    # print('Best value: ',    f_best[0])
    # print('Current value: ', f_curr[0])

    # create a list of all neighbors in the neighborhood of x_curr
    Neighborhood = neighborhood(x_curr)

    for s in Neighborhood:  # evaluate every member in the neighborhood of x_curr
        solutionsChecked = solutionsChecked + 1
        if evaluate(s, r)[0] > f_best[0]:
            
            # find the best member and keep track of that solution
            x_best = s[:]
            f_best = evaluate(s, r)[:]  # and store its evaluation

    # ADDED `and`: the current solution must be less than the max weight 
    if f_best == f_curr and (f_curr[1] < maxWeight):  # if there were no improving solutions in the neighborhood
        done = 1
    
    else:
        x_curr = x_best[:]  # else: move to the neighbor solution and continue
        f_curr = f_best[:]  # evalute the current solution

        print("\nTotal number of solutions checked: ", solutionsChecked)
        print("Best value found so far: ", f_best)

print("\nFinal number of solutions checked: ", solutionsChecked)
print("Best value found: ", f_best[0])
print("Weight is: ", f_best[1])
print("Total number of items selected: ", np.sum(x_best))
print("Best solution: ", x_best)
