"""
Particle Swarm Optimization for Schwefel Minimization Problem
Daniel Carpenter
ISE/DSA 5113
"""

import copy
import math
from random import Random

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
pBestPostion  = []  # P[particle] Particle i's historical best position
pBestFitValue = []  # Associated evaluated fitness value for Particle i's historical best position


# =============================================================================
# SWARM INITIALIZATION 
# Randomly initialize a swarm instance
# Set the partical's best to it's starting position
# =============================================================================
for particle in range(swarmSize):
    for theDimension in range(numDimensions):
        
        # Position: give random value between lower/upper bounds (-500, 500 for schwefel)
        position[particle].append(randNumGenerator.uniform(lowerBound, upperBound))
        
        # Velocity: give random value between -1 and 1   --- maybe these are good bounds?  maybe not...
        velocity[particle].append(randNumGenerator.uniform(-1, 1))

    pCurrFitValue.append(evalFitnessVal(position[particle]))  # evaluate the current position's fitness value

pBestPosition = position[:]       # initialize pBestPosition to the starting position
pBestFitVal   = pCurrFitValue[:]  # initialize pBestPosition to the starting position's value


## TODO - Track particle best position and value
## TODO - Track global best position and value
## TODO - Velocity and Position update functions
## TODO - Limits on guidence of the feasible particle's position
## TODO - velocity max limitations
## TODO - stopping criterion, etc.
## TODO - identifying the global best; 

## TODO - main loop, 



