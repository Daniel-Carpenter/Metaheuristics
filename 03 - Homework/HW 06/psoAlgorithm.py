"""
Particle Swarm Optimization for Schwefel Minimization Problem
Daniel Carpenter
ISE/DSA 5113
"""

import copy
import math
from random import Random
import numpy as np

# Random seed
# to get a random number between 0 and 1, write call this:             randNumGenerator.random()
# to get a random number between lwrBnd and upprBnd, write call this:  randNumGenerator.uniform(lwrBnd,upprBnd)
# to get a random integer between lwrBnd and upprBnd, write call this: randNumGenerator.randint(lwrBnd,upprBnd)
seed = 12345
randNumGenerator = Random(seed)


lowerBound = -500  # bounds for Schwefel Function search space
upperBound = 500  # bounds for Schwefel Function search space

# you may change anything below this line that you wish too -----------------------------------------------------

# note: for the more experienced Python programmers, 
# you might want to consider taking a more object-oriented approach to the PSO implementation, 
# i.e.: a particle class with methods to initialize itself, and update its own velocity and position; 
# a swarm class with a method to iterates through all particles to call update functions, etc.


# =============================================================================
# INPUTS 
# =============================================================================

numDimensions = 2 # number of dimensions of problem
swarmSize     = 5 # number of particles in swarm

# Velocity acceleration constants
phi1 = 2
phi2 = 2 

# Initial Inertia weight (placeholder) # TODO
intertiaWeight = 0.2



# =============================================================================
# SCHWEFEL FUNCTION
# Schwefel function to evaluate a real-valued solution x
# note: the feasible space is an n-dimensional hypercube centered at the origin with side length = 2 * 500
# =============================================================================
def evalFitnessVal(x):
    fitnessValue = 0
    numParticles = len(x)
    
    # For every particle particle, calculate the fitness value based on Schwefel function
    for particle in range(numParticles):
        fitnessValue = fitnessValue + x[particle]*math.sin(math.sqrt(abs(x[particle])))

    fitnessValue = 418.9829*numParticles - fitnessValue

    return fitnessValue


# =============================================================================
# INITIALIZE POSITION AND VELOCITY
# the swarm will be represented as a list of positions, velocities, values, pBestPosition, and pBestPosition values
# note: position[0] and velocity[0] provides the position and velocity of particle 0; 
# position[1] and velocity[1] provides the position and velocity of particle 1; and so on.
# =============================================================================

# In the current time period, position[particle] and velocity[particle] of each particle i, 
# Each particle contains n-dimensional list of the coordinate position & velocity 
position = [[] for _ in range(swarmSize)] # X[particle]: position (2D: x, y) of particle i
velocity = [[] for _ in range(swarmSize)] # V[particle]: velocity (2D: x, y) of particle i


# Lists containing info related to each particle in swarm
pCurrFitValue = []  # X[particle] The current position of particle i
pBestPosition = []  # P[particle] Particle i's historical best position
pBestFitValue = []  # Associated evaluated fitness value for Particle i's historical best position


# =============================================================================
# STEP 1 - SWARM INITIALIZATION 
# Randomly initialize a swarm instance
# Set the partical's best to it's starting position
# =============================================================================
for particle in range(swarmSize):
    for theDimension in range(numDimensions):
        
        # Position: give random value between lower/upper bounds (-500, 500 for schwefel)
        position[particle].append(randNumGenerator.uniform(lowerBound, upperBound))
        
        # Velocity: give random value between -1 and 1   --- maybe these are good bounds?  maybe not...
        velocity[particle].append(randNumGenerator.uniform(-1, 1))

    # STEP 2 (initial): Evaluate fitness value
    pCurrFitValue.append(evalFitnessVal(position[:][particle]))  # evaluate the current position's fitness value

# STEP 3 (initial): Log the individual and global bests
pBestPosition = position[:]       # initialize pBestPosition to the starting position
pBestFitValue = pCurrFitValue[:]  # initialize pBestPosition to the starting position's value


## Global best position and value ---------------------------------------------

# Returns the 2 element list with [0] min value and [1] associate index of an element
def getMinValueAndIndex(fitnessValues, positions):
    minValue = np.min(fitnessValues)
    minIndex = fitnessValues.index(minValue)
    
    minPosition = positions[minIndex][:]
    
    return [minValue, minPosition]

# From above output for later indexing
VALUE_IDX    = 0
POSITION_IDX = 1

# Get the Global best fitness value and position
gBestFitValue, gBestPosition = getMinValueAndIndex(pBestFitValue[:], pBestPosition[:]) 


# =============================================================================
# UPDATE VELOCITY AND POSITION 
# =============================================================================

# Velocity --------------------------------------------------------------------

## random weights of r for random velocity adjustment
r1, r2 = randNumGenerator.random(), randNumGenerator.random() 

## Calculations of updating velocity, separated by intertia + cognitive + social (for simplicity)
vInertia   = np.multiply(intertiaWeight, velocity[:])                      # Interia   component of updated velocity
vCognitive = np.multiply(phi1*r1, np.subtract(pBestPosition[:], position[:])) # Cognitive component of ""
vSocial    = np.multiply(phi2*r2, np.subtract(gBestPosition[:], position[:])) # Social    component of ""

## Actually update the velocity
velocity =  vInertia[:] + vCognitive[:] + vSocial[:]

# Position --------------------------------------------------------------------

position = position[:] + velocity[:] # Update new position based on the updated velocity

# Convert back to list
position = position.tolist()
velocity = velocity.tolist()


# =============================================================================
# Compare current position fitness value to the current best (for each particle)
# =============================================================================

# Calculate the fitness of the new positions
for particle in range(swarmSize):
    for theDimension in range(numDimensions):
        
        # Get the current fitness value of the new positions
        pCurrFitValue[particle] = evalFitnessVal(position[:][particle])
        
        # Compare the current positions' value to their person best
        if pCurrFitValue[particle] < pBestFitValue[particle]:
        
            # If better, then set the best VALUE to the current value (as a copy [:])
            pBestFitValue[particle] = pCurrFitValue[:][particle]
            
            # If better, then set the best POSITION to the current position  (as a copy [:])
            pBestPosition[particle] = position[:][particle]
        
        
# Get the Global best fitness value and position
gBestFitValue, gBestPosition = getMinValueAndIndex(pBestFitValue[:], pBestPosition[:]) 


# Rerun velocity




## TODO - Track particle best position and value

## TODO - Track global best position and value
    

## TODO - Limits on guidence of the feasible particle's position
## TODO - velocity max limitations
## TODO - stopping criterion, etc.
## TODO - identifying the global best; 

## TODO - main loop, 



