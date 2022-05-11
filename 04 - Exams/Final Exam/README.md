Comprehensive Final Exam
================
Daniel Carpenter
May 2022

-   [1 - *Question `1`* (Version 1)](#1---question-1-version-1)
    -   [1.1 *Part (1):* Mathematical
        Formulation](#11-part-1-mathematical-formulation)
    -   [1.2 *Part (2)*: AMPL Code &
        Output](#12-part-2-ampl-code--output)
-   [2 - *Question `2`* (Version 6)](#2---question-2-version-6)
    -   [2.1 Code to get Root Node](#21-code-to-get-root-node)
    -   [2.2 Branch and Bound Diagram](#22-branch-and-bound-diagram)
-   [3 - *Question `3`* (Version 2)](#3---question-3-version-2)
    -   [3.1 *Part (i)*: Hill Climbing](#31-part-i-hill-climbing)
    -   [3.2 *Part (ii)*: Path Relinking](#32-part-ii-path-relinking)
    -   [3.3 *Part (iii)*: Simulated
        Annealing](#33-part-iii-simulated-annealing)
-   [4 - *Question `4`* (Version 3)](#4---question-4-version-3)
    -   [4.1 *Part (i)* - Roulette
        Probability](#41-part-i---roulette-probability)
    -   [4.2 *Part (ii/iii)* - Breed
        Offspring](#42-part-iiiii---breed-offspring)
-   [5 - *Question `5`* (Version 2)](#5---question-5-version-2)
    -   [5.1 *Part (i)* - Global Best](#51-part-i---global-best)
    -   [5.2 *Part (ii)* - Local Best
        w/Ring](#52-part-ii---local-best-wring)

# 1 - *Question `1`* (Version 1)

## 1.1 *Part (1):* Mathematical Formulation

### 1.1.1 Sets

![NewBuildTypes](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;NewBuildTypes "NewBuildTypes"):
Set of new build types
![b\\in (Homes, \\ Duplex, \\ MiniPark)](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;b%5Cin%20%28Homes%2C%20%5C%20Duplex%2C%20%5C%20MiniPark%29 "b\in (Homes, \ Duplex, \ MiniPark)")

### 1.1.2 Parameters

|                                                                                                                                      Parameter | Description                                                                                                                                                                                                     | Default Value                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                        ![budget](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;budget "budget") | Federal grant allocation to revitalize neighborhoods                                                                                                                                                            | $15MM total budget                                                                                                                                                                                                                                                                                                                                     |
|          ![maxBuildingDemod](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;maxBuildingDemod "maxBuildingDemod") | Max amount of buildings that can be demolished                                                                                                                                                                  | 300 total buildings                                                                                                                                                                                                                                                                                                                                    |
|                                  ![demoCost](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;demoCost "demoCost") | Cost of demolishing a building                                                                                                                                                                                  | $4,000 per building                                                                                                                                                                                                                                                                                                                                    |
|                      ![freedUpSpace](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;freedUpSpace "freedUpSpace") | Acreage generated from demolishing a building                                                                                                                                                                   | 0.25 per building                                                                                                                                                                                                                                                                                                                                      |
|             ![newBuildSpace_b](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;newBuildSpace_b "newBuildSpace_b") | Amount of acreage that a new build (![b \\in NewBuildTypes](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;b%20%5Cin%20NewBuildTypes "b \in NewBuildTypes")) consumes             | ![Homes](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;Homes "Homes"): 0.2, ![Duplex](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;Duplex "Duplex"): 0.4, ![MiniPark](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;MiniPark "MiniPark"): 1.0            |
|                   ![newBuildTax_b](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;newBuildTax_b "newBuildTax_b") | Amount of tax dollars generated from a new build (![b \\in NewBuildTypes](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;b%20%5Cin%20NewBuildTypes "b \in NewBuildTypes"))        | ![Homes](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;Homes "Homes"): 1,500, ![Duplex](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;Duplex "Duplex"): 2,750, ![MiniPark](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;MiniPark "MiniPark"): 500        |
|                ![newBuildCost_b](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;newBuildCost_b "newBuildCost_b") | Amount of dollars used to create a new build (![b \\in NewBuildTypes](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;b%20%5Cin%20NewBuildTypes "b \in NewBuildTypes"))            | ![Homes](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;Homes "Homes"): 150,000, ![Duplex](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;Duplex "Duplex"): 190,000, ![MiniPark](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;MiniPark "MiniPark"): 20,000 |
| ![newBuildPercShare_b](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;newBuildPercShare_b "newBuildPercShare_b") | Minimum required percentage share of new builds (![b \\in NewBuildTypes](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;b%20%5Cin%20NewBuildTypes "b \in NewBuildTypes")) created | ![Homes](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;Homes "Homes"): 20%, ![Duplex](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;Duplex "Duplex"): 10%, ![MiniPark](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;MiniPark "MiniPark"): 5%             |

### 1.1.3 Decision Variables

|                                                                                                                                 Variable | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![numOldBuildsDemod](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;numOldBuildsDemod "numOldBuildsDemod") | Number ![\\in \\mathbb{Z}](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5Cin%20%5Cmathbb%7BZ%7D "\in \mathbb{Z}") of old buildings to demolish                                                                                                                                                                                                                                                                                                                                                  |
|          ![numNewBuilds_b](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;numNewBuilds_b "numNewBuilds_b") | Number ![\\in \\mathbb{Z}](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5Cin%20%5Cmathbb%7BZ%7D "\in \mathbb{Z}") of new buildings (![b \\in NewBuildTypes](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;b%20%5Cin%20NewBuildTypes "b \in NewBuildTypes")) to produce                                                                                                                                                                                           |
| ![newBuildTotalCost](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;newBuildTotalCost "newBuildTotalCost") | Variables to hold total cost of new builds (![b \\in NewBuildTypes](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;b%20%5Cin%20NewBuildTypes "b \in NewBuildTypes")). Calculation: ![\\sum\_{b\\in NewBuildTypes} (numNewBuilds_b \\times newBuildCost_b)](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5Csum_%7Bb%5Cin%20NewBuildTypes%7D%20%28numNewBuilds_b%20%5Ctimes%20newBuildCost_b%29 "\sum_{b\in NewBuildTypes} (numNewBuilds_b \times newBuildCost_b)") |
|    ![oldDemoTotalCost](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;oldDemoTotalCost "oldDemoTotalCost") | Variables to hold total cost of old demolitions. Calculation: ![numOldBuildsDemod \\times demoCost](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;numOldBuildsDemod%20%5Ctimes%20demoCost "numOldBuildsDemod \times demoCost")                                                                                                                                                                                                                                                                    |
|          ![sumOfNewBuilds](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;sumOfNewBuilds "sumOfNewBuilds") | Variable to hold the number of all new build types over all New build types (![b \\in NewBuildTypes](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;b%20%5Cin%20NewBuildTypes "b \in NewBuildTypes")). Calculation: ![\\sum\_{b \\in NewBuildTypes} (numNewBuilds_b)](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5Csum_%7Bb%20%5Cin%20NewBuildTypes%7D%20%28numNewBuilds_b%29 "\sum_{b \in NewBuildTypes} (numNewBuilds_b)")                                    |

### 1.1.4 Objective

Maximize the total tax revenue from the new builds
(![b \\in NewBuildTypes](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;b%20%5Cin%20NewBuildTypes "b \in NewBuildTypes"))

![ maximize \\ taxRevenue: \\sum\_{b\\in NewBuildTypes} (numNewBuilds_b \\times newBuildTax_b)](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%20maximize%20%5C%20taxRevenue%3A%20%5Csum_%7Bb%5Cin%20NewBuildTypes%7D%20%28numNewBuilds_b%20%5Ctimes%20newBuildTax_b%29 " maximize \ taxRevenue: \sum_{b\in NewBuildTypes} (numNewBuilds_b \times newBuildTax_b)")

### 1.1.5 Constraints

**C1** Spend less than or equal to the federal budget (variable
definitions above define below)  

![
meetTheBudget: newBuildTotalCost + oldDemoTotalCost \\leq budget
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AmeetTheBudget%3A%20newBuildTotalCost%20%2B%20oldDemoTotalCost%20%5Cleq%20budget%0A "
meetTheBudget: newBuildTotalCost + oldDemoTotalCost \leq budget
")

**C2** Can only produce new builds using the demolished buildings’
generated land

![ 
useAvailLand: \\sum\_{b\\in NewBuildTypes} (numNewBuilds_b \\times newBuildSpace_b) 
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%20%0AuseAvailLand%3A%20%5Csum_%7Bb%5Cin%20NewBuildTypes%7D%20%28numNewBuilds_b%20%5Ctimes%20newBuildSpace_b%29%20%0A " 
useAvailLand: \sum_{b\in NewBuildTypes} (numNewBuilds_b \times newBuildSpace_b) 
")

![
\\leq numOldBuildsDemod \\times freedUpSpace
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0A%5Cleq%20numOldBuildsDemod%20%5Ctimes%20freedUpSpace%0A "
\leq numOldBuildsDemod \times freedUpSpace
")

**C3** Can only clear a certain amount of old buildings

![
maxBuildingsCleared: numOldBuildsDemod \\leq maxBuildingDemod
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AmaxBuildingsCleared%3A%20numOldBuildsDemod%20%5Cleq%20maxBuildingDemod%0A "
maxBuildingsCleared: numOldBuildsDemod \leq maxBuildingDemod
")

**C4** For each new build type
(![b\\in NewBuildTypes](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;b%5Cin%20NewBuildTypes "b\in NewBuildTypes")),
the percentage share of the new build type must meet the minimum
required (see variables)

![
share: numNewBuilds_b \\geq newBuildPercShare_b \\times sumOfNewBuilds, 
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0Ashare%3A%20numNewBuilds_b%20%5Cgeq%20newBuildPercShare_b%20%5Ctimes%20sumOfNewBuilds%2C%20%0A "
share: numNewBuilds_b \geq newBuildPercShare_b \times sumOfNewBuilds, 
")

![
\\forall \\ b \\in NewBuildTypes
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0A%5Cforall%20%5C%20b%20%5Cin%20NewBuildTypes%0A "
\forall \ b \in NewBuildTypes
")

**C5** Non-negativity and integer constraints  

![
numOldBuildsDemod \\in \\mathbb{Z}^{+}
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AnumOldBuildsDemod%20%5Cin%20%5Cmathbb%7BZ%7D%5E%7B%2B%7D%0A "
numOldBuildsDemod \in \mathbb{Z}^{+}
")

![
\\ numNewBuilds_b \\in \\mathbb{Z}^{+}, 
\\ \\forall \\ b \\in NewBuildTypes
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0A%5C%20numNewBuilds_b%20%5Cin%20%5Cmathbb%7BZ%7D%5E%7B%2B%7D%2C%20%0A%5C%20%5Cforall%20%5C%20b%20%5Cin%20NewBuildTypes%0A "
\ numNewBuilds_b \in \mathbb{Z}^{+}, 
\ \forall \ b \in NewBuildTypes
")

## 1.2 *Part (2)*: AMPL Code & Output

### 1.2.1 AMPL Code

**Data
![problem1.dat](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;problem1.dat "problem1.dat")**

``` python
data;

# SETS =============================================================

# Set of new build types
set NewBuildTypes := Homes Duplex MiniPark;

# PARAMETERS ========================================================

param budget           := 15000000; # federal budget 
param maxBuildingDemod := 300;      # max buildings can be demo'd
param demoCost         := 4000;     # Cost of each demolition
param freedUpSpace     := 0.25;     # Freed up space from demolition

# Amount of acreage that a new building (b in NewBuildTypes) consumes
param: newBuildSpace :=  
       Homes    0.2
       Duplex   0.4
       MiniPark 1.0
       ;
# Amount of tax dollars generated from a new building (b in NewBuildTypes)
param: newBuildTax :=  
       Homes    1500
       Duplex   2750
       MiniPark 500
       ;

# Amount of dollars used to create a new building (b in NewBuildTypes)
param: newBuildCost :=  
       Homes    150000
       Duplex   190000
       MiniPark 20000
       ;

# Minimum required percentage share of new buildings (b in NewBuildTypes) created
param: newBuildPercShare :=  
       Homes    0.20
       Duplex   0.10
       MiniPark 0.05
       ;
```

**Model
![problem1.mod](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;problem1.mod "problem1.mod")**

``` python
reset;                  # Reset globals
options solver cplex;   # Using cplex for simplex alg

# SETS ============================================================
set NewBuildTypes; # Set of new build types

# PARAMETERS =======================================================
param budget           >= 0; # federal budget 
param maxBuildingDemod >= 0; # max buildings can be demo'd
param demoCost         >= 0; # Cost of each demolition
param freedUpSpace     >= 0; # Freed up space from demolition

param newBuildSpace    {NewBuildTypes} >= 0; # new build acreage
param newBuildTax      {NewBuildTypes} >= 0; # n.b. tax generation
param newBuildCost     {NewBuildTypes} >= 0; # n.b. cost
param newBuildPercShare{NewBuildTypes} >= 0; # n.b. min % share

# DECISION VARIABLES ===============================================
var numOldBuildsDemod                 >= 0 integer; # Num old builds to demo
var numNewBuilds      {NewBuildTypes} >= 0 integer; # Num new builds to create

# Variables to hold total cost of new builds over all types
var newBuildTotalCost = sum{b in NewBuildTypes} ( (numNewBuilds[b] * newBuildCost[b]));

# Variables to hold total cost of old demolitions
var oldDemoTotalCost = (numOldBuildsDemod * demoCost) ;

# Variable to hold the sum of all new build types over all New build types
var sumOfNewBuilds =  sum{b in NewBuildTypes}( numNewBuilds[b] );

# OBJECTIVE FUNCTION ===============================================
maximize taxRevenue: sum{b in NewBuildTypes}( numNewBuilds[b] * newBuildTax[b] );

# CONSTRAINTS ======================================================

# C1  Spend less than or equal to the federal budget
s.t. meetTheBudget: 
    newBuildTotalCost + oldDemoTotalCost <= budget ;

# C2 Can only produce new builds using the demolished buildings land
s.t. useAvailLand: 
    sum{b in NewBuildTypes}( numNewBuilds[b] * newBuildSpace[b] )
    <= numOldBuildsDemod * freedUpSpace ;

# C3 Can only clear a certain amount of old buildings
s.t. maxBuildingsCleared: numOldBuildsDemod <= maxBuildingDemod ;

# C4 For each new build type (b in NewBuildTypes), 
#    the percentage share of the new build type must meet the minimum required
s.t. share {b in NewBuildTypes}: 
    numNewBuilds[b] >= newBuildPercShare[b] * sumOfNewBuilds ;

# CONTROLS ==========================================================
    data problem1.dat; # retreive data file with sets/param. values
    solve;

    print;

    print "Number of old buildings to demolish and cost (dollars):";
    display numOldBuildsDemod, oldDemoTotalCost ;
    
    print "Number of new buildings produced and cost (dollars):";
    display numNewBuilds , newBuildTotalCost ;
    
    print "Total Budget Used (dollars):";
    display newBuildTotalCost + oldDemoTotalCost ;
    
    print "Part 3: Max Tax Revenue generated (dollars):";
    display taxRevenue ;
```

### 1.2.2 *Part 2/3:* Solve AMPL Model and Display Solution w/Commentary

<img src="PDF Submission/Images/problem1.png" style="width:55.0%" />

# 2 - *Question `2`* (Version 6)

## 2.1 Code to get Root Node

*Root Node is Node 1 in the diagram*

### 2.1.1 Root Node AMPL Model ![problem2.mod](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;problem2.mod "problem2.mod")

-   Note code below also used/altered to test upper and lower bounds of
    child nodes.

``` python
reset;
option solver cplex; # Solver

var x >= 0; # Not integer because this is used to check the optimal when fixing a var
var y >= 0; # ""

# Original problem:
maximize theSolution: 2.5*x + 6*y;
    s.t. first:  3*x + 5*y <= 26;
    s.t. second:   x       >= 4;

# Used to check the BnB nodes
# Fixing x = 4 to solve for initial values of y
s.t. checkNode: x = 4;

# Solve and display
solve;
display theSolution, x,y;
```

### 2.1.2 Output of Root Node AMPL Model (fixing x=4 & solving for y)

<img src="PDF Submission/Images/problem2Output.png" style="width:50.0%" />

## 2.2 Branch and Bound Diagram

### 2.2.1 Summary of Diagram

-   Optimal solution reached at node 4 with integer feasible values of
    ![x = 5](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;x%20%3D%205 "x = 5"),
    and
    ![y = 2](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;y%20%3D%202 "y = 2"),
    `optimal of 24.5`
-   Checked 7 total nodes
-   Fathomed 3 nodes (see description of “why” in diagram)
-   Each “Round” label shows which variable is being checked and for
    what integer value (lower or upper bound of the parent node)
-   Please note that the AMPL model above was used as a calculator to
    test upper and lower bounds.

### 2.2.2 Branch and Bound Diagram

<img src="PDF Submission/Images/problem2Diagram.png" style="width:100.0%" />

# 3 - *Question `3`* (Version 2)

## 3.1 *Part (i)*: Hill Climbing

-   Please see the below snippet on rightmost comments about the
    algorithm
-   Ended at iteration 3 with minimum value of -1.9991 due to no change
    in best neighbor
    <img src="PDF Submission/Images/problem3i.png" style="height:80.0%" />

## 3.2 *Part (ii)*: Path Relinking

-   Below shows two images with the path re-linking process iterations
    (from initiation to guided solution).
-   Green arrow highlights the path to the guided solution
-   **Logic overview:** Evaluates neighbors of initiation solution, then
    moves along path of each neighbor. Makes best move for each
    neighbor, then checks difference between current and guided
    solution. Repeats until finding the guided solution
-   *`Iteration 3` duplicated for ease of viewing*

<img src="PDF Submission/Images/problem3ii_1.png">

<img src="PDF Submission/Images/problem3ii_2.png">

## 3.3 *Part (iii)*: Simulated Annealing

Using the evaluation function for this question (note language below is
`R`)

``` r
# Create an Evaluation function to evaluate fitness
evaluateFitness <- function(x1, x2) { x1*cos(x1)*sin(x2) + 0.5*x2 }
```

The probability `p` of accepting a move uses the following formula:
![p=e^{\\frac{-\\left(f\\left(s\_{1}\\right)-f\\left(s\_{2}\\right)\\right)}{T}}](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p%3De%5E%7B%5Cfrac%7B-%5Cleft%28f%5Cleft%28s_%7B1%7D%5Cright%29-f%5Cleft%28s_%7B2%7D%5Cright%29%5Cright%29%7D%7BT%7D%7D "p=e^{\frac{-\left(f\left(s_{1}\right)-f\left(s_{2}\right)\right)}{T}}").

Where
![f\\left(s\_{1}\\right)](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;f%5Cleft%28s_%7B1%7D%5Cright%29 "f\left(s_{1}\right)")
is the `current` solution, and
![f\\left(s\_{2}\\right)](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;f%5Cleft%28s_%7B2%7D%5Cright%29 "f\left(s_{2}\right)")
is the `candidate` solution since minimization. See calculation below
(using `evaluateFitness()` function)

``` r
# Uses the evaluation function to return the probability (see above formula)
calculateProb <- function(temperature, currentPosition, newPosition) {
  # Assuming minimization, evaluation of the Current and Candidate solutions:
  f_s1 = evaluateFitness(currentPosition[1], currentPosition[2]) # f(s[1]) current sol.
  f_s2 = evaluateFitness(newPosition[1],     newPosition[2]    ) # f(s[2]) candidate sol.
  
  # If Candidate evaluation is WORSE than the current, accept with prob. p 
  if (f_s2 < f_s1) { # '<' since minimization
    p = exp( ( -(f_s1-f_s2) / temperature ) )

  } else { p = 1 } # Else accept move since better
  
  return( round(p, 3) ) # Round to 3 decimal places
}
```

Now calculate the probability `p` from the `current` to the `candidate`
solutions

``` r
# What is the probability of accepting a move from 
# (4, 0) to candidate neighbor solution (4, 1)? 
paste('At temp. 3, the probability from (4, 0) to (4, 1) is', 
      calculateProb(temperature     = 3, 
                    currentPosition = c(4, 0), 
                    newPosition     = c(4, 1)) )
```

    ## [1] "At temp. 3, the probability from (4, 0) to (4, 1) is 0.567"

``` r
# What is the probability of accepting a move from 
# (4, 0) to candidate neighbor solution (4,-1)?
paste('At temp. 3, the probability from (4, 0) to (4, -1) is',
      calculateProb(temperature     = 3, 
                    currentPosition = c(4, 0), 
                    newPosition     = c(4, -1)) )
```

    ## [1] "At temp. 3, the probability from (4, 0) to (4, -1) is 1"

# 4 - *Question `4`* (Version 3)

## 4.1 *Part (i)* - Roulette Probability

-   Evaluates the fitness for each chromosome
    ![c \\in Chromosomes](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;c%20%5Cin%20Chromosomes "c \in Chromosomes")
    using
    ![f(x) = x_1 + 2x_2 + 3x_3 + 4x_4 + 5x_5](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;f%28x%29%20%3D%20x_1%20%2B%202x_2%20%2B%203x_3%20%2B%204x_4%20%2B%205x_5 "f(x) = x_1 + 2x_2 + 3x_3 + 4x_4 + 5x_5")
    as evaluation function.  
-   Then computes the probability based on the following equation:
    ![\\frac{f\_{c}}{\\sum\_{c\\in Chromosomes} f_c}](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5Cfrac%7Bf_%7Bc%7D%7D%7B%5Csum_%7Bc%5Cin%20Chromosomes%7D%20f_c%7D "\frac{f_{c}}{\sum_{c\in Chromosomes} f_c}")  
-   See yellow highlighted cells for final roulette wheel probabilities
    for each chromosome

<img src="PDF Submission/Images/problem4i.png" style="width:60.0%" />

## 4.2 *Part (ii/iii)* - Breed Offspring

-   Select the highest `(Chrom. 3)` and lowest `(Chrom. 4)` fitness
    valued chromosomes, then split at crossover point to produce
    offspring
-   Offspring split between the second and third bit (highlighted for
    ease)
-   Highest fitness valued offspring: `Offspring 2` with fitness value
    of `12`

<img src="PDF Submission/Images/problem4ii.png" style="width:60.0%" />

<!-- ## Part (iii) -->
# 5 - *Question `5`* (Version 2)

## 5.1 *Part (i)* - Global Best

### 5.1.1 Assumptions

-   Uses all calculations and parameter values from the problem
    question. See header in picture as well for the calculation
-   Parameters of interest highlighted in orange
-   See `global` best logic in picture below

### 5.1.2 Solution

-   Particle 1’s Next `Velocity: (-1.90, 3.55, 3.70)`
-   Particle 1’s Next `Position: (12.10, 8.55, 5.70)`

### 5.1.3 Relevant Work

<img src="PDF Submission/Images/problem5i.png" style="width:100.0%" />

## 5.2 *Part (ii)* - Local Best w/Ring

### 5.2.1 Assumptions

-   Local best paramaters highlighted in yellow
-   See `local` best logic with `ring` structure in picture below

### 5.2.2 Solution

-   Particle 1’s Next `Velocity: (-0.40, 4.30, 4.45)`
-   Particle 1’s Next `Position: (13.60, 9.30, 6.45)`

### 5.2.3 Relevant Work

<img src="PDF Submission/Images/problem5ii.png" style="width:100.0%" />
