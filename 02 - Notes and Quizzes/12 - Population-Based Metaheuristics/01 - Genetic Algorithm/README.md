# Genetic Algorithm
> Use's Darwin's idea of survival of the fittest to obtain the best solution

<br>

## GA `Goals`
1. Design artifical software that retains natural environment that we try to emulate  
2. Better understand how natural environment evolves  

---
<br>

## GA `Benefits` and `Uses`
<img src = 'Images/ben.png'  width = 450> <br>
<img src = 'Images/use.png'  width = 450> <br>

---
<br>

## GA `Process` Overview
> Iteratively, randomly, but intelligently search population, while using many simulanious solutions per iteration  

### `Repeat the Following Process Many Times` until Highly Improved Solutions
1. *`Start with random population`* of solutions  
    <img src = 'Images/process1.png'  width = 300> <br>
2. *`Combine best solutions`*, producing better solutions (hopefully)  
    <img src = 'Images/process2.png'  width = 300> <br>
3. *`Mutation:`* small % of the combined solutions are *modified*  
    <img src = 'Images/process3.png'  width = 300> <br>
    * Changes can *improve* or *reduce* the solution's quality  

---
<br>

## GA `Terminology`
<img src = 'Images/terms.png'  width = 550> <br>
<img src = 'Images/terms1.png' width = 550> <br>

---
<br>
<br>

# GA Process Details

## GA Detailed Process - `Overview`
> Overall goal is to slighly evolve parents to enhance diversity of offspring while resembling the parents.   
> Accomplished through survival of the fittest methods


### High-Level Steps
1. Create a Random Population size `n`  
2. Randomly compare population fitness  
3. Create a new Population  
4. Rerun the algorithm with the new population  
5. Return best solution of the current population  
6. Loop back to step 2 and evaluate the fitness  

---
<br>

## GA Detailed Process - `Steps`

<img src = 'Images/overview.png'  width = 550> <br>

### 1. Create a Random Population (`n` depends on specific problem)  
* `n` Chromosomes (usually n-bit strings)  
<img src = 'Images/chrom.png' width = 300> <br>
<img src = 'Images/pop.png' width = 300> <br>
* Sometimes hard to get random feasible solution  
* Could seed a feasible solution  

<br>

### 2. Evaulate Fitness of Population  
* <img src = 'Images/eval.png' width = 300> <br>
* Start with low pressure on population comparison  
* Strictor evaluation at end  
<img src = 'Images/scale.png' width = 300> <br>
<img src = 'Images/rank.png' width = 300> <br>
<img src = 'Images/scales.png' width = 300> <br>

<br>

### 3. Create a new Population. Repeat steps below until complete  
* ` Select` two parents chromosomes `based on fitness`.   
    - Higher chance to be selected with higher ranking  
    - Accomplished with `roullete wheel selection`  
    <img src = 'Images/p(select).png' width = 300> <br>
    - Could also do with `tournament selection`  
    <img src = 'Images/tourney.png' width = 300> <br>
* `Breed` parents to form `offspring`  
    - Given a `crossover probability`  
    - Simple approach: randomly divide parents (`n`-bit string) into   two and swap latter halves
    <img src = 'Images/crossover.png' width = 300> <br>
    - Could be more complex (multiple divisions, etc.)  
    - Should be feasible  
* Randomly `mutate` small part of the offspring to create   population diversity 
    - Needs to be minor so the offspring looks like the parent  
    <img src = 'Images/mutate.png' width = 300> <br>
* Evalutate the offspring and `insert` new population  
    - Could keep the `k` best parent solutions  
    - Could accept some duplicates, none, or all.   

<br>

### 4. Rerun the algorithm with the new population that `replaces` the old   pop.
### 5. If conditions satisfied, return best solution of the current population  
### 6. `Loop` back to step 2 and evaluate the `fitness`  


<!-- <img src = 'Images/.png'  width = 550> <br> -->