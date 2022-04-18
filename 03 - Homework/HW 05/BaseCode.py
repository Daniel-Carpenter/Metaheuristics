#the intial framework for a binary GA
#author: Charles Nicholson
#for ISE/DSA 5113

#need some python libraries
import copy
import math
from random import Random
import numpy as np

#to setup a random number generator, we will specify a "seed" value
seed = 5113
myPRNG = Random(seed)

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

#Student name(s):
#Date:

#monitor the number of solutions evaluated
solutionsChecked = 0


populationSize = 150 #size of GA population
Generations = 100   #number of GA generations

crossOverRate = 0.8  #currently not used in the implementation; neeeds to be used.
mutationRate = 0.05  #currently not used in the implementation; neeeds to be used.
eliteSolutions = 10  #currently not used in the implementation; neeed to use some type of elitism     


#create an continuous valued chromosome 
def createChromosome(d):   
    #this code as-is expects chromosomes to be stored as a list, e.g., x = []
    #write code to generate chromosomes, most likely want this to be randomly generated
    
    x = []   #i recommend creating the solution as a list
        
    return x    
    

#create initial population by calling the "createChromosome" function many times and adding each to a list of chromosomes (a.k.a., the "population")
def initializePopulation(): #n is size of population; d is dimensions of chromosome
    
    population = []
    populationFitness = []
    
    for i in range(populationSize):
        population.append(createChromosome(n))
        populationFitness.append(evaluate(population[i]))
        
    tempZip = zip(population, populationFitness)
    popVals = sorted(tempZip, key=lambda tempZip: tempZip[1], reverse = True)
    
    #the return object is a reversed sorted list of tuples: 
    #the first element of the tuple is the chromosome; the second element is the fitness value
    #for example:  popVals[0] is represents the best individual in the population
    #popVals[0] for a 2D problem might be  ([-70.2, 426.1], 483.3)  -- chromosome is the list [-70.2, 426.1] and the fitness is 483.3
    
    return popVals    

#implement a crossover
def crossover(x1,x2):
    
        #with some probability (i.e., crossoverRate) perform breeding via crossover, 
        #i.e. two parents (x1 and x2) should produce two offsrping (offspring1 and offspring2) 
        # --- the first part of offspring1 comes from x1, and the second part of offspring1 comes from x2
        # --- the first part of offspring2 comes from x2, and the second part of offspring2 comes from x1
      
        #if no breeding occurs, then offspring1 and offspring2 can simply be copies of x1 and x2, respectively
      

    
    return offspring1, offspring2  #two offspring are returned 


#function to compute the weight of chromosome x
def calcWeight(x):
    
    a=np.array(x)
    c=np.array(weights)
    
    totalWeight = np.dot(a,c)    #compute the weight value of the knapsack selection

    return totalWeight   #returns total weight    
    

#function to determine how many items have been selected in a particular chromosome x
def itemsSelected(x):
    
    a=np.array(x)
    return np.sum(a)   #returns total number of items selected 



#function to evaluate a solution x
def evaluate(x):
          
    a=np.array(x)
    b=np.array(value)
    
    totalValue = np.dot(a,b)     #compute the value of the knapsack selection
       
    #you will VERY LIKELY need to add some penalties or sometype of modification of the totalvalue to compute the chromosome fitness
    #for instance, you may include penalties if the knapsack weight exceeds the maximum allowed weight

    fitness  = totalValue 

    return fitness   #returns the chromosome fitness




#performs tournament selection; k chromosomes are selected (with repeats allowed) and the best advances to the mating pool
#function returns the mating pool with size equal to the initial population
def tournamentSelection(pop,k):
    
    #randomly select k chromosomes; the best joins the mating pool
    matingPool = []
    
    while len(matingPool)<populationSize:
        
        ids = [myPRNG.randint(0,populationSize-1) for i in range(k)]
        competingIndividuals = [pop[i][1] for i in ids]
        bestID=ids[competingIndividuals.index(max(competingIndividuals))]
        matingPool.append(pop[bestID][0])

    return matingPool


def rouletteWheel(pop):
    
  
    #create sometype of rouletteWheel selection -- can be based on fitness function or fitness rank
    #(remember the population is always ordered from most fit to least fit, so pop[0] is the fittest chromosome in the population, and pop[populationSize-1] is the least fit!
    
      
    return matingPool
    
    
#function to mutate solutions
def mutate(x):
    
    #create some mutation logic  -- make sure to incorporate "mutationRate" somewhere and dont' do TOO much mutation
    
    return x
        
            
    

#breeding -- uses the "mating pool" and calls "crossover" function    
def breeding(matingPool):
    #the parents will be the first two individuals, then next two, then next two and so on
    
    children = []
    childrenFitness = []
    for i in range(0,populationSize-1,2):
        child1,child2=crossover(matingPool[i],matingPool[i+1])
        
        child1=mutate(child1)
        child2=mutate(child2)
        
        children.append(child1)
        children.append(child2)
        
        childrenFitness.append(evaluate(child1))
        childrenFitness.append(evaluate(child2))
        
    tempZip = zip(children, childrenFitness)
    popVals = sorted(tempZip, key=lambda tempZip: tempZip[1], reverse = True)
        
    #the return object is a sorted list of tuples: 
    #the first element of the tuple is the chromosome; the second element is the fitness value
    #for example:  popVals[0] is represents the best individual in the population
    #popVals[0] for a 2D problem might be  ([-70.2, 426.1], 483.3)  -- chromosome is the list [-70.2, 426.1] and the fitness is 483.3
    
    return popVals


#insertion step
def insert(pop,kids):
    
    #this is not a good solution here... essentially this is replacing the previous generation with the offspring and not implementing any type of elitism
    #at the VERY LEAST evaluate the best solution from "pop" to make sure you are not losing a very good chromosome from last generation
    #maybe want to keep the top 5? 10? solutions from pop -- it's up to you.
    
    return kids 
    
    
    
#perform a simple summary on the population: returns the best chromosome fitness, the average population fitness, and the variance of the population fitness
def summaryFitness(pop):
    a=np.array(list(zip(*pop))[1])
    return np.max(a), np.mean(a), np.min(a), np.std(a)


#the best solution should always be the first element... 
def bestSolutionInPopulation(pop):
    print ("Best solution: ", pop[0][0])
    print ("Items selected: ", itemsSelected(pop[0][0]))
    print ("Value: ", pop[0][1])
    print ("Weight: ", calcWeight(pop[0][0]))

    
    
def main():
    #GA main code
    Population = initializePopulation()


    #optional: you can output results to a file -- i've commented out all of the file out put for now
    #f = open('out.txt', 'w')  #---uncomment this line to create a file for saving output    


    for j in range(Generations):
                    
        mates=tournamentSelection(Population,10)  #<--need to replace this with roulette wheel selection, e.g.:  mates=rouletteWheel(Population)
        Offspring = breeding(mates)
        Population = insert(Population, Offspring)
    
        #end of GA main code
        
        maxVal, meanVal, minVal, stdVal=summaryFitness(Population)          #check out the population at each generation
        print("Iteration: ", j, summaryFitness(Population))                 #print to screen; turn this off for faster results
        
        #f.write(str(minVal) + " " + str(meanVal) + " " + str(varVal) + "\n")  #---uncomment this line to write to  file
        
    #f.close()   #---uncomment this line to close the file for saving output
    
    print (summaryFitness(Population))
    bestSolutionInPopulation(Population)
    

if __name__ == "__main__":
    main()    
    


