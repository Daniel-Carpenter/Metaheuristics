"""
Geneteic Algorithm
Problem 2

Student name: Daniel Carpenter
Date: April 2022
Class: ISE/DSA 5113
"""

# the intial framework for a binary GA
# author: Charles Nicholson
# for ISE/DSA 5113

# need some python libraries
import copy
import math
from random import Random
import numpy as np

# to setup a random number generator, we will specify a "seed" value
seed = 5113
myPRNG = Random(seed)

# to setup a random number generator, we will specify a "seed" value
# need this for the random number generation -- do not change
seed = 51132021
myPRNG = Random(seed)

# to get a random number between 0 and 1, use this:             myPRNG.random()
# to get a random number between lwrBnd and upprBnd, use this:  myPRNG.uniform(lwrBnd,upprBnd)
# to get a random integer between lwrBnd and upprBnd, use this: myPRNG.randint(lwrBnd,upprBnd)

# number of elements in a solution
n = 150

# create an "instance" for the knapsack problem
value = []
for i in range(0, n):
    # value.append(round(myPRNG.expovariate(1/500)+1,1))
    value.append(round(myPRNG.triangular(150, 2000, 500), 1))

weights = []
for i in range(0, n):
    weights.append(round(myPRNG.triangular(8, 300, 95), 1))

# define max weight for the knapsack
maxWeight = 2500

# =============================================================================

# Genetic Algorithm Fun    | Function defaults:
def geneticAlgorithmKnapsack(populationSize = n,    # size of GA population
                             Generations    = 1000, # number of GA generations
                             crossOverRate  = 0.9,  # 90% chance that two parents bred at some crossover point
                             mutationRate   = 0.10, # 10% chance an offspring is mutated between 1 and maxChangesAllowed
                             eliteSolutions = 10    # Number prior pop to keep from gen to gen
                             ):
    # monitor the number of solutions evaluated
    solutionsChecked = 0
    
    # =============================================================================
    # CREATE CHROMOSOME: Continuous Valued 
    # similar to initialSolution() logic for HC
    # Inputs: d is dimensions of chromosome
    # =============================================================================
    def createChromosome(d, prob=0.08): 
        # DEfault 8% Prob of appending item. 
        # Note 8% produces around 5 to 15 infeasible bags
        # this code as-is expects chromosomes to be stored as a list, e.g., x = []
        # write code to generate chromosomes, most likely want this to be randomly generated
    
        x = [] # empty list for x to hold binary values indicating if item i is in knapsack
        ITEM    = 1
        NO_ITEM = 0
        
        # Create a initial solution for knapsack (Could be infeasible), by 
        # randomly create a list of binary values from 0 to d. 1 if item is in the knapsack
        for item in range(0, d):
            if myPRNG.random() < prob:  
                x.append(ITEM)
            else:
                x.append(NO_ITEM)
        return x
    
    # =============================================================================
    # CREATE INITIAL POPULATION: 
    
    # Call "createChromosome" function many times, and 
    # Add each to a list of chromosomes (a.k.a., the "population")
    # Note Inputs: Technically none, but pulls `n` from the preset inputs
    # Returns:
    # the return object is a reversed sorted list of tuples:
    # [1] the first element of the tuple is the chromosome; 
    # [2] the second element is the fitness value
    # for example:  popVals[0] is represents the best individual in the population
    # popVals[0] for a 2D problem might be  ([-70.2, 426.1], 483.3)  -- chromosome is the list [-70.2, 426.1] and the fitness is 483.3
    # =============================================================================
    def initializePopulation():  # n is size of population; d is dimensions of chromosome
    
        population = []
        populationFitness = []
    
        for i in range(populationSize): # (from inputs popSize)
            population.append(createChromosome(n))
            populationFitness.append(evaluate(population[i]))
    
        tempZip = zip(population, populationFitness)
        popVals = sorted(tempZip, key=lambda tempZip: tempZip[1], reverse=True)
    
        return popVals
    
    # Indces of the above created chromosome
    ITEMS_IDX         = 0
    FITNESS_VALUE_IDX = 1
    
    # =============================================================================
    # CROSSOVER
    
    # with some probability (i.e., crossoverRate) perform breeding via crossover,
    # i.e. two parents (x1 and x2) should produce two offsrping (offspring1 and offspring2)
    # --- the first part of offspring1 comes from x1, and the second part of offspring1 comes from x2
    # --- the first part of offspring2 comes from x2, and the second part of offspring2 comes from x1
    # =============================================================================
    def crossover(parent1, parent2, prob=crossOverRate):
    
        # Breeding occurs since probability met    
        if myPRNG.random() < prob:  
            
            # Get the crossover point
            crossOverPoint = myPRNG.randint(0, n-1) # Random point in array
            
            def splitParentAtCrossOverPoint(parent):
                
                # Split parent at crossover point and return the pieces
                return (
                    parent[:crossOverPoint ], # First piece
                    parent[ crossOverPoint:]  # Second piece
                )
        
            # Get two pieces of each parent at cross over points
            par1_piece1, par1_piece2 = splitParentAtCrossOverPoint(parent1) # Parent 1
            par2_piece1, par2_piece2 = splitParentAtCrossOverPoint(parent2) # Parent 2
            
            # Swap pieces from the parents and put into the offspring
            offspring1 = par1_piece1 + par2_piece2 # First piece of parent 1, second piece p2
            offspring2 = par2_piece1 + par1_piece2 # First piece of parent 2, second piece p1
    
        # if no breeding occurs, then offspring1 and offspring2 are copies of parent1 and parent2, respectively
        else:
            offspring1 = parent1[:]
            offspring2 = parent2[:]
    
        return offspring1, offspring2  # two offspring are returned
    
    
    # =============================================================================
    # COMPUTE WEIGHT OF CHROMOSOME x
    # =============================================================================
    def calcWeight(x):
    
        a = np.array(x)
        c = np.array(weights)
    
        # compute the weight value of the knapsack selection
        totalWeight = np.dot(a, c)
    
        return totalWeight  # returns total weight
    
    
    # =============================================================================
    # CALC. ITEMS SELECTED
    # function to determine how many items have been selected in a particular chromosome x
    # =============================================================================
    def itemsSelected(x):
    
        a = np.array(x)
        return np.sum(a)  # returns total number of items selected
    
    # =============================================================================
    # EVALUATE: function to evaluate a solution x
    # =============================================================================
    def evaluate(x): 
    
        a = np.array(x)
        b = np.array(value)
    
        totalValue = np.dot(a, b)  # compute the value of the knapsack selection
        totalWeight = calcWeight(x)
    
        # Penalize knapsacks that exceed the total weight (from HW 4 solution)
        if totalWeight > maxWeight:
            totalValue = 0.85*totalValue - 10*(totalWeight - maxWeight)**2
        fitness = totalValue
    
        return fitness  # returns the chromosome fitness
    
    
    # =============================================================================
    # TOURNAMENT SELECTION 
    # k chromosomes are selected (with repeats allowed) and the best advances to the mating pool
    # function returns the mating pool with size equal to the initial population
    # =============================================================================
    def tournamentSelection(pop, k=2):
    
        # randomly select k chromosomes; the best joins the mating pool
        matingPool = []
    
        while len(matingPool) < populationSize:
    
            ids = [myPRNG.randint(0, populationSize-1) for i in range(k)]
            competingIndividuals = [pop[i][FITNESS_VALUE_IDX] for i in ids]
            bestID = ids[competingIndividuals.index(max(competingIndividuals))]
            matingPool.append(pop[bestID][ITEMS_IDX])
    
        return matingPool
    
    
    # =============================================================================
    # ROULETTE WHEEL
    # =============================================================================
    def rouletteWheel(pop):
    
        matingPool = []  # list of randomly selected parents to mate
        
        # Spin roulette wheel k times and add k number of random parents to pool
        while len(matingPool) < populationSize:
                
            # Implentation from: https://www.tutorialspoint.com/genetic_algorithms/genetic_algorithms_parent_selection.htm
            
            ## Calculate sum of a all fitnesses in pop.
            sumOfFitnessInPop = 0
            for chromosome in range(len(pop)):
                sumOfFitnessInPop += pop[chromosome][FITNESS_VALUE_IDX]
                                                   
            ## Spin the wheel ---------------------------------------------------------
            
            ### Generate a random number between 0 and sumOfFitnessInPop
            ### Landed random number will contain the chosen chromosome
            endedSpinValue = myPRNG.uniform(0, sumOfFitnessInPop)
        
        
            partialSumOfFitnessVal = 0 # to hold the current running sum of fitness for chromosomes
            chromosome = -1 # chromosome index (will start at 0)
            bestID = 0 # to hold the random selected chromosome idx
            
            # Get running sum of chromosome fitness values until reached the randomly chosen chromosome
            while partialSumOfFitnessVal < endedSpinValue:
                chromosome += 1 # Increment chromosome
                partialSumOfFitnessVal += pop[chromosome][FITNESS_VALUE_IDX] 
                
                # Spin finished - Get the best chromosome ID
                if partialSumOfFitnessVal > endedSpinValue:
                    bestID = chromosome
            
            ## Now add the chosen persone to the mating pool
            matingPool.append(pop[bestID][ITEMS_IDX])
        
        return matingPool # return list of k parents chosen to be in mating pool
    
    
    # =============================================================================
    # MUTATE SOLUTIONS
    # =============================================================================
    def mutate(x, prob=mutationRate, maxChangesAllowed=2): # The probability is the mutation rate
    
        # If probability met then mutate
        if myPRNG.random() < prob:  
            
            # Can change 1-max (random spread)
            numIdxsToChange = myPRNG.randint(1, maxChangesAllowed) 
            
            # Change k number of elements based on numIdxsToChange
            for change in range(numIdxsToChange):
                mutatedElementIdx = myPRNG.randint(0, n-1)
                
                # Mutate the index by flipping from 0 to 1 or 1 to 0
                if x[mutatedElementIdx] == 1:
                    x[mutatedElementIdx] = 0
                else:
                    x[mutatedElementIdx] = 1
        
        return x
    
    
    # =============================================================================
    # BREEDING
    # uses the "mating pool" and calls "crossover" function
    # =============================================================================
    def breeding(matingPool):
        # the parents will be the first two individuals, then next two, then next two and so on
    
        children = []
        childrenFitness = []
        for i in range(0, populationSize-1, 2):
            child1, child2 = crossover(matingPool[i], matingPool[i+1])
    
            child1 = mutate(child1)
            child2 = mutate(child2)
    
            children.append(child1)
            children.append(child2)
    
            childrenFitness.append(evaluate(child1))
            childrenFitness.append(evaluate(child2))
    
        tempZip = zip(children, childrenFitness)
        popVals = sorted(tempZip, key=lambda tempZip: tempZip[1], reverse=True)
    
        # the return object is a sorted list of tuples:
        # the first element of the tuple is the chromosome; the second element is the fitness value
        # for example:  popVals[0] is represents the best individual in the population
        # popVals[0] for a 2D problem might be  ([-70.2, 426.1], 483.3)  -- chromosome is the list [-70.2, 426.1] and the fitness is 483.3
    
        return popVals
    
    
    # =============================================================================
    # INSERTION
    # =============================================================================
    def insert(pop, kids, k=eliteSolutions): # k is the number of past pop to keep
    
        newPop = [] # The new population list
        
        # Calculate the parents and children to insert, based on k
        # will insert k prior population members and the n minus k top ranking kids
        parentsToInsert  = k
        childrenToInsert = len(pop)-k
    
        # Insert the top ranking k parents
        for chromosome in range(parentsToInsert):
            newPop.append(pop[chromosome]) 
        
        # Insert the top ranking n minus k kids
        for chromosome in range(childrenToInsert):
            newPop.append(kids[chromosome]) 
    
        return newPop
    
    
    # =============================================================================
    # GET SUMMARY OF POPULATION
    # perform a simple summary on the population:
    #   1. returns the best chromosome fitness, 
    #   2. the average population fitness, and 
    #   3. the variance of the population fitness
    # =============================================================================
    def summaryFitness(pop):
        a = np.array(list(zip(*pop))[1])
        return np.max(a), np.mean(a), np.min(a), np.std(a)
    
        
    # =============================================================================
    # Simple head function - print top n chromosomes for a population
    # =============================================================================
    def head(population, n=6): # note sorted by value desc
        print('Top %g Chromosomes of given Population:\n' % n,
              'Chrom.\t Value\t\t Weight\t\t Num. Items')
        for chromosome in range(1, n+1):
            print(' [%g]\t' % chromosome,
                  '%.1f'  %            population[chromosome-1][FITNESS_VALUE_IDX], '\t',  # Value (note neg. penalty)
                  '%.1f'  % calcWeight(population[chromosome-1][ITEMS_IDX]), '\t', # Weight
                  '%g' % itemsSelected(population[chromosome-1][ITEMS_IDX]))       # Num. Items Selected
    
    
    # =============================================================================
    # GET BEST SOLUTIONS 
    # =============================================================================
    def bestSolutionInPopulation(pop):
        print("Best solution: ", pop[0][0]) # Best solution should be the FIRST element! (sorting)
        print("Items selected: ", itemsSelected(pop[0][0]))
        print("Value: ", pop[0][1])
        print("Weight: ", calcWeight(pop[0][0]))
    
    
    # =============================================================================
    # MAIN
    # =============================================================================
    
    def main():
        # GA main code
        Population = initializePopulation()
    
        # optional: you can output results to a file -- i've commented out all of the file out put for now
        # f = open('out.txt', 'w')  #---uncomment this line to create a file for saving output
    
        for j in range(Generations):
    
            # <--need to replace this with roulette wheel selection, e.g.:  mates=rouletteWheel(Population)
            mates=rouletteWheel(Population)
            Offspring = breeding(mates)
            Population = insert(Population, Offspring)
    
            # end of GA main code
    
            maxVal, meanVal, minVal, stdVal = summaryFitness(
                Population)  # check out the population at each generation
            # print to screen; turn this off for faster results
            # print("Iteration: ", j, summaryFitness(Population))
    
            # f.write(str(minVal) + " " + str(meanVal) + " " + str(varVal) + "\n")  #---uncomment this line to write to  file
    
        # f.close()   #---uncomment this line to close the file for saving output
    
        print(summaryFitness(Population))
        bestSolutionInPopulation(Population)
    
        # Output a list for the summary output
        solutionOutput = [
            Generations, populationSize, crossOverRate, mutationRate, eliteSolutions,
            itemsSelected(Population[0][ITEMS_IDX]), calcWeight(Population[0][ITEMS_IDX]), 
            Population[0][FITNESS_VALUE_IDX]
        ]
        
        return solutionOutput
    
    if __name__ == "__main__":
        main()



# =============================================================================
# CALL FUNCTION
# =============================================================================

GA_1 = geneticAlgorithmKnapsack(populationSize = n,    # size of GA population
                                Generations    = 250,  # number of GA generations
                                crossOverRate  = 0.9,  # 90% chance that two parents bred at some crossover point
                                mutationRate   = 0.10, # 10% chance an offspring is mutated between 1 and maxChangesAllowed
                                eliteSolutions = 10    # Number prior pop to keep from gen to gen
                                )

GA_1 = geneticAlgorithmKnapsack(populationSize = n,    # size of GA population
                                Generations    = 500,  # number of GA generations
                                crossOverRate  = 0.9,  # 90% chance that two parents bred at some crossover point
                                mutationRate   = 0.05, # 5% chance an offspring is mutated between 1 and maxChangesAllowed
                                eliteSolutions = 20    # Number prior pop to keep from gen to gen
                                )

GA_1 = geneticAlgorithmKnapsack(populationSize = n,    # size of GA population
                                Generations    = 1000, # number of GA generations
                                crossOverRate  = 0.9,  # 90% chance that two parents bred at some crossover point
                                mutationRate   = 0.025,# 2.5% chance an offspring is mutated between 1 and maxChangesAllowed
                                eliteSolutions = 50    # Number prior pop to keep from gen to gen
                                )
