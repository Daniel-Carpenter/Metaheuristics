# `Heuristics` Intro & `Local Search`

## Table of Contents
* Explain the differences between `exact`, `approximate`, and `heuristic methods`
* Encode solutions for heuristics
* Develop `neighborhoods` for `local search` techniques
* Develop `evaluation functions` for heuristics
* Solve problems using:
    * `hill climbing`, 
    * hill climbing with `random restarts`, 
    * hill climbing with `random walk`, 
    * local `beam search`, and 
    * `stochastic beam search`


---
<br>

## Overview of Optimization Techniques

Key Question | Answer
-------------|--------
What are `exact` methods? | Can find an exact optimal, like `simplex` or `Least-squares`, `branch-and-bound`, `complete enumeration`
What are `approximate` methods? | Do not gaurentee optimal, but give a bound for the optimal.
What are `metaheuristics`? | Subset of heuristics that are highly-generalizable. 
Explain the differences between `exact`, `approximate`, and `heuristic methods` | Hueristics are much faster but could give a non-optimal solution. 

---
<br>

# `Heuristic` Methods

## `Heuristics` Overview

### What are `heuristic` methods?
* Give an approximate solution to an EXACT model *(if model well formulated)*
* Do not gaurentee optimal
* DOES NOT give a range of potential solutions.
* They do well in practice. 


### What are `metaheuristics`? 
* Subset of heuristics that are highly-generalizable. 
 

### Types of Heuristics:
Num | Method Name | Explanation
----|-------------|--------------
1   | `generate and test`       | Guessing
2   | `gradient descent`        | Require differentiable objective
3   | `decomposition methods`   | Break down into sub problems then recombine to the oberall
4   | `reduction techniques`    | reduce the size of the solution space. Could remove the optimal
5   | `constructive heuristics` | Build solution from scratch
6   | `improving heuristics`    | Find an initial solution then improve it. Most techniques in the class are improving


### Potential problems with `heuristics`
* Could accidentally find local maximums or minimums
<img src = "Images/range.png" width = 550> <br>


---
<br>

## Important Terminology related to `heuristics`

### Important Terminology related to `heuristics`
<img src = "Images/terms1.png" width = 550> <br>
<img src = "Images/terms2.png" width = 550> <br>


### Changes in Terminology from Exact to `Heuristic` Methods
Old Term | New Term | Description
---------|----------|-------------
Decision    | `Decision encoding` | like valid ineqalities in the sense that you can realize that there are certain spaces that the solution cannot exist in.
Objective   | `Evaluation function`
COnstraints | Same |Still have constraints, need to figure out to handle them though


---
<br>

## Developing `Evalutation Functions`

### What are `Neighborhoods`?
* Grouping of potential solutions that are `near a the actual solution`
* It can be said to be an art to define the neighborhood
* Can measure from the point by using:
    1. Euclidean Distance
    2. Hamming Distance
    3. Jaccard Distance
    4. Mahalanobis Distance

<img src = "Images/neigh1.png" width = 550> <br>
<img src = "Images/2opt.png" width = 550> <br>


### What is the `Evaluation Fuction`?
* Use the original objective and see if it is feasible. 
* Important to define this function well since each move is based on the evaluation function 
<img src = "Images/eval.png" width = 550> <br>


---
<br>

## `Hill Climbing` Overview
> * Very efficient technique  
> * Iteratively climb up a hill  
> * Analogous to climbing a mountain with no map and in dense fog  
> ***Main problem with method is falling in a `local max/min`***

### Why is Hill Climbing a **greedy** technique?
* Could have many bad moves that increase time of the search
* ***Only based on the `local hill`***
* Has no memory of where it has been

### **Pros and Cons** to Hill Climbing
<img src = "Images/proConHill.png" width = 550> <br>


### Important Questions to Answer related to Hill Climbing
<img src = "Images/hillQ.png" width = 550> <br>

#### 1. False Solution to if no solutions are better
<img src = "Images/localMax.png" width = 550> <br>

#### 2. Treats each equal solution as indifferently


---
<br>

## `Hill Climbing` Methods

### `Steepest Ascent` Hill Climbing
> Ends once it finds the best local neighbor  

<img src = "Images/ascent.png" width = 550> <br>

### `First Accept` Hill Climbing
> Ends once it finds the first better neighbor  

<img src = "Images/first.png" width = 550> <br>


---
<br>

## Improving upon Hill Climbing

### Hill Climbing with `random walk`
* Allows to search the entire space (through random walk) 
* Overcomes local max/min
<img src = "Images/rw.png" width = 550> <br>


### `Stochastic` Hill Climbing
<img src = "Images/shill.png" width = 550> <br>

### ***`Best Method`***: Hill Climbing with `random restart`
<img src = "Images/randomRestart.png" width = 550> <br>


### Local `Beam Search`
* Simultaniously search multiple neighborhoods and iterate to around the best
* *Disadvantage*: Usually converges quickly which ends up being resource intensive and has little benefit

<img src = "Images/lbeam.png" width = 550> <br>


### `Stochastic Beam Search`
* Overcomes local beam search disadvantages
* Assigns higher probability to potentially better solutions 
<img src = "Images/sbeams.png" width = 550> <br>

## Metaheuristics

### What are Metaheuristics
> Goal to overcome issue with local min/max  

<img src = "Images/meta.png" width = 550> <br>

### Examples of Metaheuritics
> Many metaheuristics out there. Be careful as some are not good.  

<img src = "Images/metaExamples.png" width = 550> <br>
<img src = "Images/metaExamples2.png" width = 550> <br>