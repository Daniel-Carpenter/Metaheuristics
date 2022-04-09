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
Question 4 - Hill Climbing Random Restarts using First Acceptance
===============================================================================
"""

# =============================================================================
# Function to generate a hill climb with random resets 
# =============================================================================

# Returns a list of the best solution found:
#   [0] totalValue:       Total value of the value bag
#   [1] totalWeight:      Associated weight of the bag
#   [2] solutionsChecked: Number of solutions checked
#   [3] numberOfItems:    Total number of items packed
#   [4] itemsPacked:      A list of the items packed

# The indices of the solutions returned from `hillClimbFirstAccept()` function
VALUE_IDX      = 0 # The value index of the output to the hill climb function
WEIGHT_IDX     = 1 # Weight of the solution
SOL_CHCKED_IDX = 2 # The numner of solutions checked
NUM_ITEMS_IDX  = 3 # The number of items in the solutions knapsack
ITEMS_PCKD_IDX = 4 # List of the items packed

def hillClimbFirstAccept():
    
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
                
                break # >> Exit loop << (first accept change from best acceptance)
    
        # Checks for platueau and feasibility
        if f_best == f_curr and (f_curr[1] < maxWeight):  # if there were no improving solutions in the neighborhood
            done = 1
        
        else:
            x_curr = x_best[:]  # else: move to the neighbor solution and continue
            f_curr = f_best[:]  # evalute the current solution
    
            # print("\nTotal number of solutions checked: ", solutionsChecked)
            # print("Best value found so far: ", f_best)
    
    return [              # Return a list of important values:
        f_best[0],        # totalValue
        f_best[1],        # totalWeight
        solutionsChecked, # solutionsChecked
        np.sum(x_best),   # numberOfItems
        x_best            # itemsPacked
        ]

        
# =============================================================================
# Function to do Hill Climbing with random restarts (using first acceptance)
# =============================================================================

def kRestartsHillClimbFirstAccept(k_restarts, numSolutionsToShow):
    
    # List of the optimal solutions, including the returned output from the 
    # `hillClimbFirstAccept()` function
    optimalSolutions = [] 
    bestIdx          = 0  # Stores the index of the best value
    
    # Iterate through k restarts of hill climbing with first accept
    for theCurrentRestart in range(0, k_restarts):
        optimalSolutions.append(hillClimbFirstAccept())
        
        # See the optimal value of the restart
        # print('Sol. Idx: [%g]' % theCurrentRestart, '\tVal: %g' % 
        #       optimalSolutions[theCurrentRestart][VALUE_IDX]) # Comment to hide best value from restart
        
        # Check to see if the current solution is better than the incumbant. 
        if (theCurrentRestart != 0) and (  optimalSolutions[theCurrentRestart][VALUE_IDX] 
                                         > optimalSolutions[bestIdx][VALUE_IDX]):
            
            # If this solution is better, then store it as the best index
            bestIdx = theCurrentRestart
            
    
    # Simple function to print a solution (from list idx) of restarted solutions
    def printSolution(solutionIdx):
        
        # Print the output
        print('Solution Index: ', solutionIdx, '\n',
              'Solution value:',  optimalSolutions[solutionIdx][VALUE_IDX], '\n',
              'Solution weight:', optimalSolutions[solutionIdx][WEIGHT_IDX], '\n',
              'Number of solutions checked:', optimalSolutions[solutionIdx][SOL_CHCKED_IDX], '\n',
              'Number of items in bag:',   optimalSolutions[solutionIdx][NUM_ITEMS_IDX], '\n',
              'List of items packed:',   optimalSolutions[solutionIdx][ITEMS_PCKD_IDX], '\n'
              )
        
    
    # RETRIEVE AND PRINT SOLUTIONS  -------------------------------------------
        
    # Print best solution
    print('\n-------- THE *BEST* SOLUTION --------'), printSolution(bestIdx) 
    
    print('\n-------- %g Other Solutions --------\n' % numSolutionsToShow)
    
    # Print solutions (number to show defined in the function)
    for solutionNum in range(0, numSolutionsToShow):
        printSolution(solutionNum) # print another example
        
    # Return the best solution, best idx, and the list of restarted solutions
    return [optimalSolutions[bestIdx][VALUE_IDX], bestIdx, optimalSolutions]
    

k_restarts         = 25 # Number of restarts
numSolutionsToShow = 2  # Number of solutions to show. Could be the optimal FYI

# Call function - Random restarts with *first* acceptance hill climbing
kRestartsHillClimbFirstAccept(k_restarts, numSolutionsToShow)
