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

numDimensions = 2   # number of dimensions of problem
swarmSize     = 5 # number of particles in swarm

# Velocity acceleration constants
phi1 = 2 # Cognitive weight
phi2 = 2 # Social weight 

# Constant Inertia weighting value
intertiaWeight = 0.1


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
# MIN VALUE AND POSITION SEARCH FUNCTION
# Returns the 2 element list with [0] min value and [1] associate index of an element
# =============================================================================
def getGlobalBest(fitnessValues, positions):
    minValue = np.min(fitnessValues)
    minIndex = fitnessValues.index(minValue)
    
    minPosition = positions[minIndex][:]
    
    return [minValue, minPosition]

# From above output for later indexing
VALUE_IDX    = 0
POSITION_IDX = 1


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
# STEP 1 - SWARM INITIALIZATION / EVALUATION
# Randomly initialize a swarm instance
# Set the partical's best to it's starting position
# =============================================================================
def initializeSwarm():
    
    for particle in range(swarmSize):
        for theDimension in range(numDimensions):
            
            # Position: give random value between lower/upper bounds (-500, 500 for schwefel)
            position[particle].append(randNumGenerator.uniform(lowerBound, upperBound))
            
            # Velocity: give random value between -1 and 1   --- maybe these are good bounds?  maybe not...
            velocity[particle].append(randNumGenerator.uniform(-1, 1))
    
        # 1.1 - Evaluate fitness value
        pCurrFitValue.append(evalFitnessVal(position[:][particle]))  # evaluate the current position's fitness value
    
    # 1.2 - Log the individual and global bests
    pBestPosition = position[:]       # initialize pBestPosition to the starting position
    pBestFitValue = pCurrFitValue[:]  # initialize pBestPosition to the starting position's value


    # 1.3 - Log the Global best fitness value and position
    gBestFitValue, gBestPosition = getGlobalBest(pBestFitValue[:], pBestPosition[:]) 
    
    return [pBestPosition, pBestFitValue, gBestFitValue, gBestPosition]


# =============================================================================
# UPDATE VELOCITY AND POSITION 
# =============================================================================
def updateVelocityAndPosition(intertiaWeight, velocity, position, phi1, phi2, pBestPosition, gBestPosition):
# Velocity --------------------------------------------------------------------
    
    ## random weights of r for random velocity adjustment
    r1, r2 = randNumGenerator.random(), randNumGenerator.random() 
    
    ## Calculations of updating velocity, separated by 
    ## intertia + cognitive + social (for simplicity)
    vInertia   = np.multiply(intertiaWeight, velocity[:])                      # Interia   component of updated velocity
    vCognitive = np.multiply(phi1*r1, np.subtract(pBestPosition[:], position[:])) # Cognitive component of ""
    vSocial    = np.multiply(phi2*r2, np.subtract(gBestPosition[:], position[:])) # Social    component of ""
    
    ## Update the new velocity to the summation of intertia, cognitive, and social
    newVelocity =  vInertia[:] + vCognitive[:] + vSocial[:]
    
    ## Limit the velocity between the upper and lower bound limits
    for particle in range(swarmSize):
        for theDimension in range(numDimensions):
        
            # If the new velocity of particle i is > the limit, then reduce to the limit
            if newVelocity[particle][theDimension] > upperBound:
                newVelocity[particle][theDimension] = upperBound
                
            # If the new velocity of particle i is < the limit, then increase to the limit
            if newVelocity[particle][theDimension] < lowerBound:
                newVelocity[particle][theDimension] = lowerBound
        
    # Position ----------------------------------------------------------------
    
    ## Update new position based on the updated velocity
    newPosition = position[:] + newVelocity[:] 
    
    ## Make sure that the position is within the bounds ------------------------
    for particle in range(swarmSize):
        for theDimension in range(numDimensions):
            
            # Check to see if position in bounds
            while (newPosition[particle][theDimension] > upperBound) or (newPosition[particle][theDimension] < lowerBound):

                # Stocastically put the position in bounds
                newPosition[particle][theDimension] = randNumGenerator.uniform(lowerBound, upperBound)
    
    # Convert position and velocity back to list
    newPosition = newPosition.tolist()
    newVelocity = newVelocity.tolist()
    
    return [newPosition, newVelocity]



# =============================================================================
# Compare current position fitness value to the current best (for each particle)
# =============================================================================

def calculateParticleBests(position):
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
    
    return [pCurrFitValue, pBestPosition, pBestFitValue]


# Stopping criteria = the total number of iterations
totalIterations = 10000

# Step 1: Initialize swarm and get the particles' and global best
pBestPosition, pBestFitValue, gBestFitValue, gBestPosition = initializeSwarm()

positionIterations = []
velocityIterations = []
gBestPositionIterations = []

# Main Loop 
for iteration in range(totalIterations):
    
    # Keep track of the position iterations
    velocityIterations.append(velocity) # Swarm velocity
    positionIterations.append(position) # Swarm position
    gBestPositionIterations.append(gBestPosition) # Best Position
    
    # Step 2: Update the velocity and position
    velocity, position = updateVelocityAndPosition(intertiaWeight, velocity, position, 
                                                   phi1, phi2, pBestPosition, gBestPosition)
    
    # Step 3: Recalculate the current and global bests
    pCurrFitValue, pBestPosition, pBestFitValue = calculateParticleBests(position)
            
    # Step 4: Get the Global best fitness value and position
    gBestFitValue, gBestPosition = getGlobalBest(pBestFitValue[:], pBestPosition[:]) 

# Print the global optima
print('\nGlobal Best Value:\t % 0.4f' % gBestFitValue, '\n',
      'For each [dimension], Global Best Position:', 
      sep='')

# Print the position of each dimension
for theDimension in range(numDimensions):
    print('[', theDimension, ']\t % 0.4f' % gBestPosition[theDimension], sep='')



# Write to file if the dimensions are 2D
if numDimensions == 2:
    
    iterBreak     = 1             # Show every n iterations  
    maxIterToView = iterBreak * 5 # Max iterations to write

    
    # Print the first 5 best positions of the swarm, while highlighting global best
    f = open('output.csv', 'w')  #---uncomment this line to create a file for saving output
    
    # Column names
    f.write('iteration,particle,position1,position2,globalBest1,globalBest2,velocity1,velocity2\n')  #write to file
    
    # Write the data to a CSV for plotting and summary table
    for iteration in range(maxIterToView):
        thisIter = ''
        for particle in range(swarmSize):
            
            if iteration % iterBreak == 0:
                
                # Get the Iteration, Particle, position1/2 and velocity 1/2
                theVelocities = velocityIterations[iteration][particle]
                thePositions  = positionIterations[iteration][particle]
                globalBest    = gBestPositionIterations[iteration]
                
                # Convert the positions to flat text
                velDims    = ','.join(['{:.4f}'.format(positionVal) for positionVal in theVelocities])
                posDims    = ','.join(['{:.4f}'.format(positionVal) for positionVal in thePositions])
                globalDims = ','.join(['{:.4f}'.format(positionVal) for positionVal in globalBest])
                
                # Write tp the file
                f.write(str(iteration+1) + ',' + str(particle) + ',' + str(posDims) + ',' + 
                        str(globalDims) + ',' + str(velDims) + '\n')  
                
    f.close()  # close the file for saving output

            
# TODO: Do the local best implementation, form into a class, then run everything






























    