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

# you may change anything below this line that you wish too -------------------

# note: for the more experienced Python programmers, 
# you might want to consider taking a more object-oriented approach to the PSO implementation, 
# i.e.: a particle class with methods to initialize itself, and update its own velocity and position; 
# a swarm class with a method to iterates through all particles to call update functions, etc.


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
# GLOBAL MIN VALUE AND POSITION SEARCH FUNCTION
# Returns the 2 element list (each containing a single value) with the global best particle's:
# ---- [0] min value and 
# ---- [1] associate position of 
# =============================================================================
def getGlobalBest(fitnessValues, positions, swarmSize):
    minValue = np.min(fitnessValues)         # Find the Minimum fitness value of all particles
    minIndex = fitnessValues.index(minValue) # Find the index of the position for the min. fit. value
    
    minPosition = positions[minIndex][:] # Now get a copy of the particle's position with min index
    
    # Returns: the global best particle's minimum fitness value and its position
    return [minValue, minPosition] 


# =============================================================================
# LOCAL MIN VALUE AND POSITION SEARCH FUNCTION
# Returns the 2 element list of lists with the each particle's local best within neighborhood
# ---- [0] min value and 
# ---- [1] associate position of 
# Can change numParticlesInNbrhood to consider more or less in particle's neighborhood
# =============================================================================
def getLocalBest(fitnessValues, positions, swarmSize,
                  numParticlesInNbrhood = 2):  # Number of particles to compare to for local best

    lBestFitValue = [] # will hold the best VALUE    of the n surrounding particles, for each particle
    lBestPosition = [] # will hold the best POSITION of the n surrounding particles, for each particle
    
    
    # For every particle in the swarm, (starting at n less than index 0)
    for particle in range(-numParticlesInNbrhood, swarmSize - numParticlesInNbrhood):
        
        # Identify the two neighbors fitness value of this particle, 
        # which are the two precedng particles
        personalBestNeighbor1 = fitnessValues[particle]
        personalBestNeighbor2 = fitnessValues[particle + 1]
        
        # Identify the lowest fitness value of this particle's the two preciding neighbors
        minNeighValue = min(personalBestNeighbor1, personalBestNeighbor2)
        
        # Store the index of the particle
        minNeighIndex = fitnessValues.index(minNeighValue)
        
        # Store the particle's best neighbors fitness value and position
        lBestFitValue.append(fitnessValues[minNeighIndex])
        lBestPosition.append(positions[minNeighIndex])
        
    # Returns a list of particles and the min of their n best fit. valued neighbors
    return[lBestFitValue, lBestPosition]


# If you needed to index the list just returned for global or local best
VALUE_IDX    = 0
POSITION_IDX = 1


# =============================================================================
# STEP 1 - SWARM INITIALIZATION / EVALUATION
# Randomly initialize a swarm instance
# Set the partical's best to it's starting position
# =============================================================================
def initializeSwarm(swarmSize, numDimensions, functionToGetBest):
    
    # In the current time period, position[particle] and velocity[particle] of each particle i, 
    # Each particle contains n-dimensional list of the coordinate position & velocity 
    position = [[] for _ in range(swarmSize)] # X[particle]: position (2D: x, y) of particle i
    velocity = [[] for _ in range(swarmSize)] # V[particle]: velocity (2D: x, y) of particle i

    # Lists containing info related to each particle in swarm
    pCurrFitValue = []  # X[particle] The current position of particle i

    
    # For each particle and dimension, randomly initialize the...
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


    # 1.3 - Log the Global or local best (depends on chosen method) fitness value and position
    glBestFitValue, glBestPosition = functionToGetBest(pBestFitValue[:], pBestPosition[:], swarmSize) 
    
    return [position, velocity, pCurrFitValue, 
            pBestPosition, pBestFitValue, 
            glBestFitValue, glBestPosition]


# =============================================================================
# UPDATE VELOCITY AND POSITION 
# =============================================================================
def updateVelocityAndPosition(intertiaWeight, velocity, position, phi1, phi2, pBestPosition, glBestPosition,
                              swarmSize, numDimensions):
# Velocity --------------------------------------------------------------------
    
    ## random weights of r for random velocity adjustment
    r1, r2 = randNumGenerator.random(), randNumGenerator.random() 
    
    ## Calculations of updating velocity, separated by 
    ## intertia + cognitive + social (for simplicity)
    vInertia   = np.multiply(intertiaWeight, velocity[:])                          # Interia   component of updated velocity
    vCognitive = np.multiply(phi1*r1, np.subtract( pBestPosition[:], position[:])) # Cognitive component of ""
    vSocial    = np.multiply(phi2*r2, np.subtract(glBestPosition[:], position[:])) # Social    component of ""
    
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
    
    ## Make sure that the position is within the bounds -----------------------
    for particle in range(swarmSize):
        for theDimension in range(numDimensions):
            
            # Check to see if position in bounds
            while (newPosition[particle][theDimension] > upperBound) or (newPosition[particle][theDimension] < lowerBound):

                # Stocastically put the position in bounds
                newPosition[particle][theDimension] = randNumGenerator.uniform(lowerBound, upperBound)
    
    # Convert position and velocity back to list ------------------------------
    newPosition = newPosition.tolist()
    newVelocity = newVelocity.tolist()
    
    return [newPosition, newVelocity]


# =============================================================================
# Compare current position fitness value to the current best (for each particle)
# =============================================================================
def calculateParticleBests(position, swarmSize, numDimensions,
                           pCurrFitValue, pBestPosition, pBestFitValue):
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


# =============================================================================
# DISPLAY GLOBAL BEST AND DIMENSIONS FUNCTION
# Function for displaying the global best and its dimensions
# =============================================================================
def displayGlobalBest(glBestFitValue, glBestPosition, numDimensions):
    # Print the global optima
    print('\nGlobal Best Value:\t % 0.4f' % glBestFitValue, '\n',
          'For each [dimension], Global Best Position:', 
          sep='')
    
    # Print the position of each dimension in markdown table format
    print('\n',
          '| Dimension | Global Best |', sep ='')
    print('|-----------|-------------|')
    for theDimension in range(numDimensions):
        print('|' + str(theDimension).rjust(10, ' '), 
              '|' + '{:.4f}'.format(glBestPosition[theDimension]).rjust(12, ' ') + ' |'
              )


# =============================================================================
# WRITE TOP n SWARM ITERATIONS TO A CSV FUNCTION
# Basic function for writing to file
# =============================================================================
def writeIteratonsToCSV(numDimensions, # Number of dimensions in the swarm 
                        filename,
                        method,
                        velocityIterations, 
                        positionIterations, 
                        gBestPositionIterations, 
                        swarmSize):

    iterBreak     = 1 # Display every n iterations
    maxIterToView = 5 # Top iteration to display
    
    # Write to file if the dimensions are 2D and using Global best. 
    # (only global since list structure for each particle, not single value)
    if numDimensions == 2 and method == 'global': 
        
        # Print the first 5 best positions of the swarm, while highlighting global best
        f = open(filename + '.csv', 'w')  # Open CSV for writing
        
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


# =============================================================================
# SWARM OPTIMIZATION FUNCTION
# Parameters:
# ---- numDimensions:   The number of dimension in the schwefel function
# ---- swarmSize:       The number of particles within the swarm
# ---- intertiaWeight:  The weight assigned to the intertia component of the velocity eq.
# ---- phi1:            Cognitive weight of the velocity equation. Note phi1 + phi2 <= 4
# ---- phi2:            Social    weight of the velocity equation. Note phi1 + phi2 <= 4
# ---- totalIterations: The total number of iterations before stopping (Stopping criterion)
# ---- method:          Can use 'local' or 'global' best methods. 
# ----                  'local' uses Ring Structure with 2 neighbors by default 
# ---- filename:        Name of CSV file to export to working directory.
# ----                  If using 2D and 'global' best method, will export CSV.
# ----                  Reason for exporting is to read in data to R for plotting iterations
# =============================================================================

def swarmOptimizationSchwefel( # -------------------- Defaults --------------------
    numDimensions   = 2,       # number of dimensions of problem
    swarmSize       = 5,       # number of particles in swar
    phi1            = 2,       # Cognitive weight
    phi2            = 2,       # Social weight
    intertiaWeight  = 0.1,     # Constant Inertia weighting value
    totalIterations = 100,     # Stopping criteria = the total number of iterations
    method          = 'local', # 'local' or 'global' best function name
    filename        = 'output' # Name of the ouput csv file to write first 5 iterations
    ):
    
    # Initialize to global best function by default
    functionToGetBest = getGlobalBest
    
    # If not using the global best, then switch to the local best method
    if method != 'global':
        functionToGetBest = getLocalBest    
    
    
    # -----------------------------------------------------------------------------
    # INITIALIZE POSITION AND VELOCITY, and INITIAL BESTS
    # the swarm will be represented as a list of positions, velocities, values, 
    # pBestPosition, and pBestPosition values
    # Note: position[0] and velocity[0] provides the position and velocity of particle 0; 
    # position[1] and velocity[1] provides the position and velocity of particle 1; and so on.
    # -----------------------------------------------------------------------------
    
    
    # Step 1: Initialize swarm and get the particles' and global best (and current position)
    position, velocity, pCurrFitValue, pBestPosition, pBestFitValue, glBestFitValue, glBestPosition = initializeSwarm(swarmSize, numDimensions, functionToGetBest)
    
    # Create empty lists for holding the swarm iterations
    positionIterations      = [] # Each particle's velocity
    velocityIterations      = [] # Each particle's position
    gBestPositionIterations = [] # The current Global Best Position
    
    
    # -----------------------------------------------------------------------------
    # Main Loop 
    # -----------------------------------------------------------------------------
    for iteration in range(totalIterations):
        
        # Step 0: Keep track of each iterations/dimension for velocity, position, and current global best
        velocityIterations.append(velocity)           
        positionIterations.append(position)           
        gBestPositionIterations.append(glBestPosition) 
        
        # Step 2: Update the velocity and position
        velocity, position = updateVelocityAndPosition(intertiaWeight, velocity, position, 
                                                       phi1, phi2, pBestPosition, glBestPosition,
                                                       swarmSize, numDimensions)
        
        # Step 3: Recalculate the particle and global bests
        pCurrFitValue, pBestPosition, pBestFitValue = calculateParticleBests(position, 
                                                                             swarmSize, numDimensions,
                                                                             pCurrFitValue, 
                                                                             pBestPosition, 
                                                                             pBestFitValue)
                
        # Step 4: Get the Global or local best (depends on chosen method) fitness value and position
        glBestFitValue, glBestPosition = functionToGetBest(pBestFitValue[:], pBestPosition[:], swarmSize) 
    
    
    
    
    # -----------------------------------------------------------------------------
    # Global Best
    # -----------------------------------------------------------------------------
    
    # Finally, if using the local best method, get the absolute best from the local bests
    if method == 'local':
        gBestFitValue, gBestPosition = getGlobalBest(glBestFitValue, glBestPosition, swarmSize)
    
    else: # if not local best, then change the gl best is the global best
        gBestFitValue, gBestPosition = glBestFitValue, glBestPosition
        
        
    # -----------------------------------------------------------------------------
    # Print and Export
    # -----------------------------------------------------------------------------
    
    # Print the global (or local best) and each dimensions' position
    displayGlobalBest(gBestFitValue, gBestPosition, numDimensions)
    
    # If 2D, then write to a csv for plotting in R
    writeIteratonsToCSV(numDimensions, filename, method, velocityIterations,
                        positionIterations, gBestPositionIterations, swarmSize)
        
# Call the function given the key parameters
swarmOptimizationSchwefel(
    numDimensions   = 2,        # number of dimensions of problem
    swarmSize       = 5,        # number of particles in swar
    phi1            = 2,        # Cognitive weight
    phi2            = 2,        # Social weight
    intertiaWeight  = 0.1,      # Constant Inertia weighting value
    totalIterations = 10000,    # Stopping criteria = the total number of iterations
    method          = 'global', # 'local' or 'global' best function name
    filename        = 'output'  # Name of the ouput csv file to write first 5 iterations
    )