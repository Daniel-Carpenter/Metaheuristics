"""
Simulated Annealing
Problem 1

Student name: Daniel Carpenter
Date: April 2022
Class: ISE/DSA 5113
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
def evaluate(x, r=myPRNG.randint(0,n-1)):

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

# Indices of the list returned from the evalution function
VALUE_IDX  = 0 # Value of the bag
WEIGHT_IDX = 1 # Weight of the bag


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
Question 1 - Simulated Annealing
===============================================================================
"""

# Stopping criterion
def stopTheProcedure(k, TOTAL_ITERS):
    return k == TOTAL_ITERS # stop if the iteration are greater than the max iters to perform

# The cooling Schedule for the Caunchy method
def caunchyCoolSchedule(INITIAL_TEMP , k):
    # Calculuate and return the schedule output (t_k)
    t_k = INITIAL_TEMP / (1 + k)               
    return(t_k) 

# The cooling Schedule for the Boltzmannmethod
def boltzmannCoolSchedule(INITIAL_TEMP , k):
    # Calculuate and return the schedule output (t_k)
    t_k = INITIAL_TEMP / np.log(1 + k)               
    return(t_k) 

# General function that takes in a cooling schedule and calculates t[k] 
# meant for ease of changing the cooling schedule
def coolingSchedule(scheduleFunction, INITIAL_TEMP , k):
    return(scheduleFunction(INITIAL_TEMP , k))


# =============================================================================
# SIMULATED ANNEALING ALGORITHM
# =============================================================================

def simAnnealKnapsack(TOTAL_ITERS, INITIAL_TEMP, ACCEPTANCE_THRESHOLD, COOLING_METHOD):
    
    
    ## GET INITIAL SOLUTION -------------------------------------------------------
    
    solutionsChecked = 0 # Keep track of the number of solutions checked
    
    x_curr = initial_solution()  # x_curr will hold the current solution
    f_curr = evaluate(x_curr) # f_curr holds the evaluation of the current soluton
    
    ## BEGIN LOCAL SEARCH LOGIC ---------------------------------------------------
    
    k_iter = 0 # Track the total iterations
    
    # Do not stop the procedure until the stoppping criterion is met
    while not stopTheProcedure(k_iter, TOTAL_ITERS): 
        
        # Create a list of all neighbors in the neighborhood of x_curr
        Neighborhood = neighborhood(x_curr)
        
        m_iter = 0 # Track the iterations at each temperature
        numSolutionsAccepted = 0 # keep track of number of solutions accepted
        
        while numSolutionsAccepted < ACCEPTANCE_THRESHOLD: # must search m times at each temp
            solutionsChecked += 1 # Notate another solution checked
    
            # Randomly select solution from neighbor of current solution
            x_randSolution = Neighborhood[myPRNG.randint(0,n-1)] 
            f_randSolution = evaluate(x_randSolution) # Evalute the solution
            
            
            # CHECK TO SEE IF RANDOM SOLUTION IS BETTER THAN CURRENT --------------
            
            # If the random solution knapsack value is better and is feasible...
            if (f_randSolution[VALUE_IDX] > f_curr[VALUE_IDX] and f_randSolution[WEIGHT_IDX] <= maxWeight):  
                x_curr = x_randSolution[:] # Store it as the current solution
                f_curr = f_randSolution[:]
                numSolutionsAccepted += 1  # Notate that we accepted a solution at this temp
    
            # EVEN THOUGH RANDOM SOLUTION WAS WORSE, ACCEPT IT WITH RANDOM PROB ---
            else:
                # difference between the random and current solution
                solutionsDelta = f_randSolution[VALUE_IDX] - f_curr[VALUE_IDX] 
                
                # Using the given cooling schedule (boltzmann), update the temperature given iteration num
                t_k = coolingSchedule(COOLING_METHOD, INITIAL_TEMP , k_iter) 
                runifProb = myPRNG.uniform(0,1) # With a uniform probability (from 0 to 1)...
                
                # Decide whether to choose the worse solution with random uniform prob 
                if (runifProb <= np.exp(1)**(-solutionsDelta / t_k) 
                    and f_randSolution[WEIGHT_IDX] <= maxWeight):  # and is feasible
                    x_curr = x_randSolution[:] # Store it as the current solution
                    f_curr = f_randSolution[:]
                    
            m_iter += 1 # Increment the iterations at a given temperature
        k_iter += 1 # Increment the total iterations 
                    
        
    # Output of the solution ------------------------------------------------------
    valueOfBestBag     = f_curr[VALUE_IDX]
    weightOfBestBag    = f_curr[WEIGHT_IDX]
    numItemsSelected   = np.sum(x_curr)
    selectedItemsInBag = x_curr[:]
    if COOLING_METHOD == caunchyCoolSchedule: 
        METHOD_CHOSEN = 'Caunchy' 
    else: METHOD_CHOSEN = 'Boltzmann'
    
    # Output a list for the summary output
    solution = [INITIAL_TEMP, METHOD_CHOSEN, ACCEPTANCE_THRESHOLD, k_iter, 
                solutionsChecked, numItemsSelected, weightOfBestBag, valueOfBestBag]
    
    print('\n\n--------- SOLUTION OVERVIEW ---------\n\n',
          'Initial Temp t[0]:',          solution[0], '\n',
          'Method t[k]:',                solution[1], '\n', 
          'Acceptance Threshold M[k]: ', solution[2], '\n', 
          '# Temps. Checked:',           solution[3], '\n', 
          '# Iters:',                    solution[4], '\n', 
          '# Items:',                    solution[5], '\n', 
          'Weight of Bag:',              solution[6], '\n', 
          'Value of Bag:',               solution[7], '\n',
          '\n------------------------------------'
          )
    
    return (solution)


# Call the algorithm given inputs (for Caunchy Method)
simA1 = simAnnealKnapsack(TOTAL_ITERS          = 100, 
                          INITIAL_TEMP         = 1000, 
                          ACCEPTANCE_THRESHOLD = 10, 
                          COOLING_METHOD       = caunchyCoolSchedule
                          )

# Call the algorithm given inputs (for Caunchy Method)
simA2 = simAnnealKnapsack(TOTAL_ITERS          = 200, 
                          INITIAL_TEMP         = 500, 
                          ACCEPTANCE_THRESHOLD = 5, 
                          COOLING_METHOD       = caunchyCoolSchedule
                          )

# Call the algorithm given inputs (for boltzmann Method)
simA3 = simAnnealKnapsack(TOTAL_ITERS          = 100, 
                          INITIAL_TEMP         = 1000, 
                          ACCEPTANCE_THRESHOLD = 10, 
                          COOLING_METHOD       = boltzmannCoolSchedule
                          )

# Call the algorithm given inputs (for boltzmann Method)
simA4 = simAnnealKnapsack(TOTAL_ITERS          = 150, 
                          INITIAL_TEMP         = 750, 
                          ACCEPTANCE_THRESHOLD = 20, 
                          COOLING_METHOD       = boltzmannCoolSchedule
                          )
