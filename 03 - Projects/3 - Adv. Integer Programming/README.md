Homework 3 - Integer Programming
================
Daniel Carpenter
March 2022

-   [1 - Problem `1`](#1---problem-1)
    -   [1.1 Mathematical Formulation](#11-mathematical-formulation)
        -   [1.1.1 Sets](#111-sets)
        -   [1.1.2 Parameters](#112-parameters)
        -   [1.1.3 Decision Variables](#113-decision-variables)
        -   [1.1.4 Objective Function](#114-objective-function)
        -   [1.1.5 Constraints](#115-constraints)
    -   [1.2 Code and Output](#12-code-and-output)
        -   [1.2.1 Code](#121-code)
        -   [1.2.2 Output](#122-output)
-   [2 - Problem `2`](#2---problem-2)
    -   [2.1 Mathematical Formulation (Part
        `a`)](#21-mathematical-formulation-part-a)
        -   [2.1.1 Sets](#211-sets)
        -   [2.1.2 Parameters](#212-parameters)
        -   [2.1.3 Decision Variables](#213-decision-variables)
        -   [2.1.4 Objective Function](#214-objective-function)
        -   [2.1.5 Constraints](#215-constraints)
    -   [2.2 Code and Output (Part `a`)](#22-code-and-output-part-a)
        -   [2.2.1 Code](#221-code)
        -   [2.2.2 Output (Part `a`)](#222-output-part-a)
    -   [2.3 Problem `2 b`](#23-problem-2-b)
    -   [2.4 Code and Output (Part `b`)](#24-code-and-output-part-b)
        -   [2.4.1 Code](#241-code)
        -   [2.4.2 Output (Part `b`)](#242-output-part-b)
-   [3 - Problem `3`](#3---problem-3)
    -   [3.1 Mathematical Formulation](#31-mathematical-formulation)
        -   [3.1.1 Parameters](#311-parameters)
        -   [3.1.2 Decision Variables](#312-decision-variables)
        -   [3.1.3 Objective Function](#313-objective-function)
        -   [3.1.4 Constraints (*grouped by production
            variable*)](#314-constraints-grouped-by-production-variable)
    -   [3.2 Code and Output](#32-code-and-output)
        -   [3.2.1 Code](#321-code)
        -   [3.2.2 Output](#322-output)

# 1 - Problem `1`

## 1.1 Mathematical Formulation

### 1.1.1 Sets

| Set Name                                                                                                            | Description                                                                                                                                  |
|:--------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------|
| ![GENERATORS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;GENERATORS "GENERATORS") | Set of generators ![i](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;i "i") that can be used (`A`,`B`,`C`)    |
| ![PERIODS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;PERIODS "PERIODS")          | 2 possible periods ![p](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p "p") (`1`, `2`) in the production day |

### 1.1.2 Parameters

| Parameter Name                                                                                                | Description                                                                                                                                                                                                     |
|:--------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![S_i](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;S_i "S_i")                | Fixed cost to start a generator (![i \\in GENERATORS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;i%20%5Cin%20GENERATORS "i \in GENERATORS")) in the entire day                |
| ![F_i](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;F_i "F_i")                | Fixed cost to operate a generator (![i \\in GENERATORS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;i%20%5Cin%20GENERATORS "i \in GENERATORS")) in any period                  |
| ![C_i](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;C_i "C_i")                | Variable cost per megawatt to operator a generator (![i \\in GENERATORS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;i%20%5Cin%20GENERATORS "i \in GENERATORS")) in any period |
| ![U_i](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;U_i "U_i")                | Max. megawatts generated for generator (![i \\in GENERATORS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;i%20%5Cin%20GENERATORS "i \in GENERATORS")) in any period             |
| ![demand_p](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;demand_p "demand_p") | Total demanded megawatts for period (![p \\in PERIODS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p%20%5Cin%20PERIODS "p \in PERIODS"))                                       |
| ![M](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;M "M")                      | Large constant to map watts used by each generator (![i \\in GENERATORS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;i%20%5Cin%20GENERATORS "i \in GENERATORS"))               |

### 1.1.3 Decision Variables

| Variable Name                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|:------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![watts\_{i,p}](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;watts_%7Bi%2Cp%7D "watts_{i,p}") | *Integer variable*: Number of watts to produce per generator (![i \\in GENERATORS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;i%20%5Cin%20GENERATORS "i \in GENERATORS")) per period (![p \\in PERIODS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p%20%5Cin%20PERIODS "p \in PERIODS"))                                                                                                  |
| ![x\_{i,p}](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;x_%7Bi%2Cp%7D "x_{i,p}")             | *Binary variable*: `1` if a generator (![i \\in GENERATORS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;i%20%5Cin%20GENERATORS "i \in GENERATORS")) is in period ![p](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p "p") (![p \\in PERIODS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p%20%5Cin%20PERIODS "p \in PERIODS")), `0` if not turned on at all |
| ![y_i](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;y_i "y_i")                                | *Binary variable*: `1` if a generator (![i \\in GENERATORS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;i%20%5Cin%20GENERATORS "i \in GENERATORS")) is used, `0` if not turned on at all                                                                                                                                                                                                                                     |

### 1.1.4 Objective Function

![
minimize \\ cost: \\ 
\\sum\_{i \\in GENERATORS} 
\\begin{pmatrix} 
  (\\sum\_{p \\in PERIODS}(watts\_{i,p}) \\times C_i) + (F_i \\times \\sum\_{p \\in PERIODS} x\_{i,p} ) + (S_i \\times y_i)
\\end{pmatrix} 
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0Aminimize%20%5C%20cost%3A%20%5C%20%0A%5Csum_%7Bi%20%5Cin%20GENERATORS%7D%20%0A%5Cbegin%7Bpmatrix%7D%20%0A%20%20%28%5Csum_%7Bp%20%5Cin%20PERIODS%7D%28watts_%7Bi%2Cp%7D%29%20%5Ctimes%20C_i%29%20%2B%20%28F_i%20%5Ctimes%20%5Csum_%7Bp%20%5Cin%20PERIODS%7D%20x_%7Bi%2Cp%7D%20%29%20%2B%20%28S_i%20%5Ctimes%20y_i%29%0A%5Cend%7Bpmatrix%7D%20%0A "
minimize \ cost: \ 
\sum_{i \in GENERATORS} 
\begin{pmatrix} 
  (\sum_{p \in PERIODS}(watts_{i,p}) \times C_i) + (F_i \times \sum_{p \in PERIODS} x_{i,p} ) + (S_i \times y_i)
\end{pmatrix} 
")

### 1.1.5 Constraints

**C1:** For each period, meet the demanded megawatts

![
requiredWatts: \\ \\sum\_{i \\in GENERATORS}(watts\_{i,p}) = demand_p, 
\\forall \\ p \\in PERIODS
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0ArequiredWatts%3A%20%5C%20%5Csum_%7Bi%20%5Cin%20GENERATORS%7D%28watts_%7Bi%2Cp%7D%29%20%3D%20demand_p%2C%20%0A%5Cforall%20%5C%20p%20%5Cin%20PERIODS%0A "
requiredWatts: \ \sum_{i \in GENERATORS}(watts_{i,p}) = demand_p, 
\forall \ p \in PERIODS
")

**C2:** For each generator, don’t surpass the allowable megawatts

![
upperBound: \\ \\sum\_{p \\in PERIODS}(watts\_{i,p}) \\leq U_i, 
\\forall \\ i \\in GENERATORS
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AupperBound%3A%20%5C%20%5Csum_%7Bp%20%5Cin%20PERIODS%7D%28watts_%7Bi%2Cp%7D%29%20%5Cleq%20U_i%2C%20%0A%5Cforall%20%5C%20i%20%5Cin%20GENERATORS%0A "
upperBound: \ \sum_{p \in PERIODS}(watts_{i,p}) \leq U_i, 
\forall \ i \in GENERATORS
")

**C3:** For each generator, map decision variables together to account
for the fixed costs in a given day
![S_i](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;S_i "S_i")

![
mapVars: \\ \\sum\_{p \\in PERIODS}(watts\_{i,p}) \\leq M_i \\times y_i,
\\forall \\ i \\in GENERATORS
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AmapVars%3A%20%5C%20%5Csum_%7Bp%20%5Cin%20PERIODS%7D%28watts_%7Bi%2Cp%7D%29%20%5Cleq%20M_i%20%5Ctimes%20y_i%2C%0A%5Cforall%20%5C%20i%20%5Cin%20GENERATORS%0A "
mapVars: \ \sum_{p \in PERIODS}(watts_{i,p}) \leq M_i \times y_i,
\forall \ i \in GENERATORS
")

**C4:** For each generator and period, map decision variables
![y](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;y "y")
and
![watts](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;watts "watts")
together to account for the fixed costs in a per period
![p](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p "p")

![
mapVars2: watts\_{i,p} \\leq M_i \\times x\_{i,p}
, \\forall \\ i \\in GENERATORS, \\ p \\in PERIODS
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AmapVars2%3A%20watts_%7Bi%2Cp%7D%20%5Cleq%20M_i%20%5Ctimes%20x_%7Bi%2Cp%7D%0A%2C%20%5Cforall%20%5C%20i%20%5Cin%20GENERATORS%2C%20%5C%20p%20%5Cin%20PERIODS%0A "
mapVars2: watts_{i,p} \leq M_i \times x_{i,p}
, \forall \ i \in GENERATORS, \ p \in PERIODS
")

**C5** Non-negativity or Binary restraints of decision variables

![
watts\_{i,p} \\geq 0
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0Awatts_%7Bi%2Cp%7D%20%5Cgeq%200%0A "
watts_{i,p} \geq 0
")

![
x\_{i,p}, \\ y_i \\in (0,1)
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0Ax_%7Bi%2Cp%7D%2C%20%5C%20y_i%20%5Cin%20%280%2C1%29%0A "
x_{i,p}, \ y_i \in (0,1)
")

## 1.2 Code and Output

### 1.2.1 Code

<img src="PDF Submission/Images/prob1CodeAndData.png" style="width:100.0%" />

### 1.2.2 Output

<img src="PDF Submission/Images/prob1Output.png" style="width:80.0%" />

#### 1.2.2.1 Analysis of the Output

-   The minimized cost is
    ![\\$46,100](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5C%2446%2C100 "\$46,100")
-   Generator
    ![A](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;A "A"),
    ![B](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;B "B"),
    and
    ![C](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;C "C")
    run
-   Generator
    ![C](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;C "C")
    runs in period
    ![1](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;1 "1").
    Generator
    ![A](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;A "A")
    and
    ![B](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;B "B")
    run in period
    ![2](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;2 "2")
-   Generator
    ![A](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;A "A")
    produces
    ![2,100](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;2%2C100 "2,100")
    megawatts in total
-   Generator
    ![B](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;B "B")
    produces
    ![1,800](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;1%2C800 "1,800")
    megawatts in total
-   Generator
    ![C](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;C "C")
    produces
    ![2,900](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;2%2C900 "2,900")
    megawatts in total

# 2 - Problem `2`

## 2.1 Mathematical Formulation (Part `a`)

### 2.1.1 Sets

| Set Name                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                        |
|:--------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![PRODUCTS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;PRODUCTS "PRODUCTS") | 5 types of landscaping and construction products (e.g., cement, sand, etc.) labeled product (![p](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p "p")) ![A, B, C, D,\\text{ and } E](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;A%2C%20B%2C%20C%2C%20D%2C%5Ctext%7B%20and%20%7D%20E "A, B, C, D,\text{ and } E") |
| ![SILOS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;SILOS "SILOS")          | 8 different silos ![s](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;s "s") that each product must be stored in ![(1,2,\\dots,8)](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%281%2C2%2C%5Cdots%2C8%29 "(1,2,\dots,8)")                                                                                           |

### 2.1.2 Parameters

| Parameter Name                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                             |
|:---------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![cost\_{s,p}](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;cost_%7Bs%2Cp%7D "cost_{s,p}") | Cost of storing *one ton* of product ![p \\in PRODUCTS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p%20%5Cin%20PRODUCTS "p \in PRODUCTS") in silo ![s \\in SILOS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;s%20%5Cin%20SILOS "s \in SILOS")                                       |
| ![supply_p](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;supply_p "supply_p")              | Total supply *in tons* available of product ![p \\in PRODUCTS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p%20%5Cin%20PRODUCTS "p \in PRODUCTS")                                                                                                                                                                      |
| ![capacity_s](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;capacity_s "capacity_s")        | Total capacity *in tons* of silo ![s \\in SILOS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;s%20%5Cin%20SILOS "s \in SILOS"). Can store products.                                                                                                                                                                     |
| ![M](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;M "M")                                   | Variable to map *decision variable* ![tonsOfProduct\_{p,s}](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;tonsOfProduct_%7Bp%2Cs%7D "tonsOfProduct_{p,s}") to ![isStored\_{p,s}](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;isStored_%7Bp%2Cs%7D "isStored_{p,s}"). Uses big M method. |

### 2.1.3 Decision Variables

| Variable Name                                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                     |
|:------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![tonsOfProduct\_{p,s}](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;tonsOfProduct_%7Bp%2Cs%7D "tonsOfProduct_{p,s}") | *Tons* of product ![p \\in PRODUCTS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p%20%5Cin%20PRODUCTS "p \in PRODUCTS") to store in silo ![s \\in SILOS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;s%20%5Cin%20SILOS "s \in SILOS"). Non-negative.          |
| ![isStored\_{p,s}](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;isStored_%7Bp%2Cs%7D "isStored_{p,s}")                | *Binary variable* indicating if product ![p \\in PRODUCTS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p%20%5Cin%20PRODUCTS "p \in PRODUCTS") is stored in silo ![s \\in SILOS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;s%20%5Cin%20SILOS "s \in SILOS"). |

### 2.1.4 Objective Function

![
minimize \\ costOfStorage: \\sum\_{p \\in PRODUCTS}\\sum\_{s \\in SILOS} tonsOfProduct\_{p,s} \\times cost\_{p,s} 
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0Aminimize%20%5C%20costOfStorage%3A%20%5Csum_%7Bp%20%5Cin%20PRODUCTS%7D%5Csum_%7Bs%20%5Cin%20SILOS%7D%20tonsOfProduct_%7Bp%2Cs%7D%20%5Ctimes%20cost_%7Bp%2Cs%7D%20%0A "
minimize \ costOfStorage: \sum_{p \in PRODUCTS}\sum_{s \in SILOS} tonsOfProduct_{p,s} \times cost_{p,s} 
")

### 2.1.5 Constraints

**C1:** For each silo
![s](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;s "s"),
the *tons* of the supplied product
![p](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p "p")
must be less than or equal to the capacity limit of silo
![s](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;s "s")

![
meetCapacity: \\sum\_{p \\in PRODUCTS} tonsOfProduct\_{p,s} \\leq capacity_s
, \\ \\forall \\ s \\in SILOS
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AmeetCapacity%3A%20%5Csum_%7Bp%20%5Cin%20PRODUCTS%7D%20tonsOfProduct_%7Bp%2Cs%7D%20%5Cleq%20capacity_s%0A%2C%20%5C%20%5Cforall%20%5C%20s%20%5Cin%20SILOS%0A "
meetCapacity: \sum_{p \in PRODUCTS} tonsOfProduct_{p,s} \leq capacity_s
, \ \forall \ s \in SILOS
")

**C2:** For each product
![p](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p "p"),
must use all of the total product that is available

![
useAllProduct: \\sum\_{s \\in SILOS} tonsOfProduct\_{p,s} = supply_p
, \\ \\forall \\ p \\in PRODUCTS
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AuseAllProduct%3A%20%5Csum_%7Bs%20%5Cin%20SILOS%7D%20tonsOfProduct_%7Bp%2Cs%7D%20%3D%20supply_p%0A%2C%20%5C%20%5Cforall%20%5C%20p%20%5Cin%20PRODUCTS%0A "
useAllProduct: \sum_{s \in SILOS} tonsOfProduct_{p,s} = supply_p
, \ \forall \ p \in PRODUCTS
")

**C3:** For each silo
![s](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;s "s")
and product
![p](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p "p"),

![
oneProductInSilo: \\sum\_{p in PRODUCTS} isStored\_{p,s} = 1
, \\ \\forall \\ s \\in SILOS
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AoneProductInSilo%3A%20%5Csum_%7Bp%20in%20PRODUCTS%7D%20isStored_%7Bp%2Cs%7D%20%3D%201%0A%2C%20%5C%20%5Cforall%20%5C%20s%20%5Cin%20SILOS%0A "
oneProductInSilo: \sum_{p in PRODUCTS} isStored_{p,s} = 1
, \ \forall \ s \in SILOS
")

**C4:** Map the decision variables together using the Big M method

![
mapVars: tonsOfProduct\_{p,s} \\leq M \\times isStored\_{p,s}
, \\ \\forall \\ p \\in PRODUCTS, \\ \\forall \\ s \\in SILOS
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AmapVars%3A%20tonsOfProduct_%7Bp%2Cs%7D%20%5Cleq%20M%20%5Ctimes%20isStored_%7Bp%2Cs%7D%0A%2C%20%5C%20%5Cforall%20%5C%20p%20%5Cin%20PRODUCTS%2C%20%5C%20%5Cforall%20%5C%20s%20%5Cin%20SILOS%0A "
mapVars: tonsOfProduct_{p,s} \leq M \times isStored_{p,s}
, \ \forall \ p \in PRODUCTS, \ \forall \ s \in SILOS
")

**C5** Non-negativity or Binary restraints of decision variables

![
tonsOfProduct\_{p,s} \\geq 0
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AtonsOfProduct_%7Bp%2Cs%7D%20%5Cgeq%200%0A "
tonsOfProduct_{p,s} \geq 0
")

![
isStored\_{p,s} \\in (0, 1)
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AisStored_%7Bp%2Cs%7D%20%5Cin%20%280%2C%201%29%0A "
isStored_{p,s} \in (0, 1)
")

## 2.2 Code and Output (Part `a`)

### 2.2.1 Code

<img src="PDF Submission/Images/prob2CodeAndData.png" style="width:100.0%" />

### 2.2.2 Output (Part `a`)

<img src="PDF Submission/Images/prob2Output.png" style="width:70.0%" />

#### 2.2.2.1 Analysis of the Output

-   Minimized loading cost for 250 tons of 5 products over the 8 silos
    is
    ![320](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;320 "320")
    (problem does not state cost units).
-   Product
    ![A](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;A "A")
    stores
    ![25 \\ tons](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;25%20%5C%20tons "25 \ tons")
    in
    ![silo \\ 1](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;silo%20%5C%201 "silo \ 1")
    and
    ![50 \\ tons](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;50%20%5C%20tons "50 \ tons")
    in
    ![silo \\ 4](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;silo%20%5C%204 "silo \ 4")
-   Product
    ![B](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;B "B")
    stores
    ![50 \\ tons](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;50%20%5C%20tons "50 \ tons")
    in
    ![silo \\ 5](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;silo%20%5C%205 "silo \ 5")
-   Product
    ![C](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;C "C")
    stores
    ![25 \\ tons](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;25%20%5C%20tons "25 \ tons")
    in
    ![silo \\ 3](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;silo%20%5C%203 "silo \ 3")
-   Product
    ![D](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;D "D")
    stores
    ![25 \\ tons](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;25%20%5C%20tons "25 \ tons")
    in
    ![silo \\ 2](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;silo%20%5C%202 "silo \ 2"),
    ![5 tons](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;5%20tons "5 tons")
    in
    ![silo \\ 7](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;silo%20%5C%207 "silo \ 7"),
    and and
    ![50 \\ tons](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;50%20%5C%20tons "50 \ tons")
    in
    ![silo \\ 8](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;silo%20%5C%208 "silo \ 8")
-   Product
    ![E](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;E "E")
    stores
    ![20 \\ tons](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;20%20%5C%20tons "20 \ tons")
    in
    ![silo \\ 6](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;silo%20%5C%206 "silo \ 6")

## 2.3 Problem `2 b`

-   Create a new objective that also minimizes the distance between
    capacity and stored tons of product
-   *For each silo, minimize the variance between the total capacity and
    the tons of product*

![
minimize \\ capacityActualVariance: capacity_s - \\sum\_{p \\in PRODUCTS} tonsOfProduct\_{p,s} 
, \\ \\forall s \\in SILOS
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0Aminimize%20%5C%20capacityActualVariance%3A%20capacity_s%20-%20%5Csum_%7Bp%20%5Cin%20PRODUCTS%7D%20tonsOfProduct_%7Bp%2Cs%7D%20%0A%2C%20%5C%20%5Cforall%20s%20%5Cin%20SILOS%0A "
minimize \ capacityActualVariance: capacity_s - \sum_{p \in PRODUCTS} tonsOfProduct_{p,s} 
, \ \forall s \in SILOS
")

## 2.4 Code and Output (Part `b`)

### 2.4.1 Code

<img src="PDF Submission/Images/prob2.2CodeAndData.png" style="width:100.0%" />

### 2.4.2 Output (Part `b`)

<img src="PDF Submission/Images/prob2.2Output.png" style="width:70.0%" />

#### 2.4.2.1 Analysis of the Output

-   The optimal cost actually stays the same, but the amount of
    iterations to get to that solution is much more.
-   The values of the decision variables are the same.

# 3 - Problem `3`

## 3.1 Mathematical Formulation

### 3.1.1 Parameters

| Parameter Name                                                                                                         | Description                                                                                                                                                                                                                                        |
|:-----------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![theDemand](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;theDemand "theDemand")       | The demanded amount of products                                                                                                                                                                                                                    |
| ![M](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;M "M")                               | Large scaler that is not inf, used for logical constraints via Big M Method                                                                                                                                                                        |
| ![mcWII](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;mcWII "mcWII")                   | Marginal cost component of ![WII](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WII "WII"). Set to $4.95                                                                                                            |
| ![mcWRS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;mcWRS "mcWRS")                   | Marginal cost component of ![WRS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WRS "WRS"). Set to $2.30                                                                                                            |
| ![mcWE1](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;mcWE1 "mcWE1")                   | If we buy from ![WRS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WRS "WRS"), then Marg. cost for ![WE](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WE "WE") set to $3.95        |
| ![mcWE2](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;mcWE2 "mcWE2")                   | If we do not buy from ![WRS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WRS "WRS"), then Marg. cost for ![WE](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WE "WE") set to $4.10 |
| ![mcWU](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;mcWU "mcWU")                      | Marginal cost component of ![WU](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WU "WU"). Set to 4.25                                                                                                                |
| ![mcWOW1](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;mcWOW1 "mcWOW1")                | Marginal cost of 9.50 for ![WOW](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WOW "WOW") 3000 upper bound                                                                                                          |
| ![mcWOW1Upper](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;mcWOW1Upper "mcWOW1Upper") | ![WOW](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WOW "WOW") 3000 upper bound                                                                                                                                    |
| ![mcWOW2](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;mcWOW2 "mcWOW2")                | Marginal cost of 4.90 for ![WOW](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WOW "WOW") 3000 + 6000 = 9000 upper bound                                                                                            |
| ![mcWOW2Upper](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;mcWOW2Upper "mcWOW2Upper") | ![WOW](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WOW "WOW") 3000 + 6000 = 9000 upper bound                                                                                                                      |
| ![mcWOW3](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;mcWOW3 "mcWOW3")                | Marginal cost of 2.75 for ![WOW](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WOW "WOW") Cannot exceed 25000 due to supply                                                                                         |
| ![mcWOW3Upper](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;mcWOW3Upper "mcWOW3Upper") | ![WOW](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WOW "WOW") Cannot exceed 25000 due to supply 25000                                                                                                             |
| ![fixWRS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;fixWRS "fixWRS")                | Fixed Cost component of ![WRS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WRS "WRS"). Set to 20,000                                                                                                              |
| ![availWII](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;availWII "availWII")          | Amount of ![WII](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WII "WII") that is available. Set to 18,000                                                                                                          |
| ![availWRS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;availWRS "availWRS")          | Amount of ![WRS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WRS "WRS") that is available. Set to 14,000                                                                                                          |
| ![availWE](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;availWE "availWE")             | Amount of ![WE](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WE "WE") that is available. Set to 7,000                                                                                                              |
| ![availWU](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;availWU "availWU")             | Amount of ![WU](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WU "WU") that is available. Set to 22,000                                                                                                             |
| ![minBuyAmt](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;minBuyAmt "minBuyAmt")       | Must buy at least 15k of ![WU](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WU "WU"). Set to 15,000                                                                                                                |

### 3.1.2 Decision Variables

#### 3.1.2.1 Main Decision Variables:

| Variable Name | Description                                                                                                                                                                                                                                       |
|:--------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WII           | Amount of product ![WII](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WII "WII") to produce                                                                                                                       |
| WRS           | Amount of product ![WRS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WRS "WRS") to produce                                                                                                                       |
| WU            | Amount of product ![WU](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WU "WU") to produce                                                                                                                          |
| WE            | Amount of product ![WE](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WE "WE") to produce                                                                                                                          |
| WOW           | Amount of product ![WOW](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WOW "WOW") to produce                                                                                                                       |
| WE1           | Decision variable associated with ![3.95](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;3.95 "3.95") marginal cost for ![WE](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WE "WE") |
| WE2           | Decision variable associated with ![4.10](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;4.10 "4.10") marginal cost for ![WE](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WE "WE") |
| d1WOW         | Piece wise component 1 of var ![WOW](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WOW "WOW")                                                                                                                      |
| d2WOW         | Piece wise component 2 of var ![WOW](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WOW "WOW")                                                                                                                      |
| d3WOW         | Piece wise component 3 of var ![WOW](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WOW "WOW")                                                                                                                      |

#### 3.1.2.2 Binary Helper Decision Variables:

| Variable Name | Description                                                                                                                          |
|:--------------|:-------------------------------------------------------------------------------------------------------------------------------------|
| yWRS          | Used if ![WRS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WRS "WRS") is selected                   |
| yWRS1         | Used for fixed ![WRS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WRS "WRS") cost if used           |
| yWII          | Used if ![WII](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WII "WII") is selected                   |
| yWE1          | Used if ![WE1](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WE1 "WE1") is selected                   |
| yWE2          | Used if ![WE2](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WE2 "WE2") is selected                   |
| yWU           | Used for fixed cost if ![WU](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WU "WU") used              |
| y1WOW         | To model piece wise cost for var ![WOW](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WOW "WOW")      |
| y2WOW         | To model piece wise cost for var ![WOW](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WOW "WOW")      |
| z             | Used to activate only one constraint for ![WE](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WE "WE") |

### 3.1.3 Objective Function

![minimize cost:](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;minimize%20cost%3A "minimize cost:")

      ![mcWII\*WII](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;mcWII%2AWII "mcWII*WII")

    ![+ fixWRS\*yWRS1 + mcWRS\*WRS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%2B%20fixWRS%2AyWRS1%20%2B%20mcWRS%2AWRS "+ fixWRS*yWRS1 + mcWRS*WRS")

    ![+ mcWE1\*WE1 + mcWE2\*WE2](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%2B%20mcWE1%2AWE1%20%2B%20mcWE2%2AWE2 "+ mcWE1*WE1 + mcWE2*WE2")

    ![+ mcWU\*WU](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%2B%20mcWU%2AWU "+ mcWU*WU")

    ![+ mcWOW1\*d1WOW + mcWOW2\*d2WOW + mcWOW3\*d3WOW](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%2B%20mcWOW1%2Ad1WOW%20%2B%20mcWOW2%2Ad2WOW%20%2B%20mcWOW3%2Ad3WOW "+ mcWOW1*d1WOW + mcWOW2*d2WOW + mcWOW3*d3WOW")

### 3.1.4 Constraints (*grouped by production variable*)

#### 3.1.4.1 Upper Bound Constraints

| Description                                                                                                                     | Constraint                                                                                                                                                                                                                                |
|:--------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Upper bound on ![WII](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WII "WII") production        | ![upperBoundWII: WII \\leq availWII](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;upperBoundWII%3A%20WII%20%5Cleq%20availWII "upperBoundWII: WII \leq availWII")                                          |
| Upper bound on ![WU](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WU "WU") production           | ![upperBoundWU: WU \\leq availWU](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;upperBoundWU%3A%20WU%20%5Cleq%20availWU "upperBoundWU: WU \leq availWU")                                                   |
| Upper bound on ![WE](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WE "WE") production           | ![upperBoundWE: WE \\leq availWE](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;upperBoundWE%3A%20WE%20%5Cleq%20availWE "upperBoundWE: WE \leq availWE")                                                   |
| Upper bound and map to ![WRS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WRS "WRS") via Big M | ![map\\\_yWRS1: WRS \\leq availWRS \\times yWRS1](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;map%5C_yWRS1%3A%20WRS%20%5Cleq%20availWRS%20%5Ctimes%20yWRS1 "map\_yWRS1: WRS \leq availWRS \times yWRS1") |

#### 3.1.4.2 WE Constraints

| Description                                                                                                                                                                                                                                                                                                                                   | Constraint                                                                                                                                                                                                                                                                               |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Map the ![WE](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WE "WE") vars to the ![y](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;y "y") binary                                                                                                                               | ![mapWE1: WE1 \\leq M \\times yWE1](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;mapWE1%3A%20WE1%20%5Cleq%20M%20%5Ctimes%20yWE1 "mapWE1: WE1 \leq M \times yWE1")                                                                                        |
| “”                                                                                                                                                                                                                                                                                                                                            | ![mapWE2: WE2 \\leq M \\times yWE2](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;mapWE2%3A%20WE2%20%5Cleq%20M%20%5Ctimes%20yWE2 "mapWE2: WE2 \leq M \times yWE2")                                                                                        |
| Map the ![WRS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WRS "WRS") vars to the ![y](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;y "y") binary                                                                                                                            | ![mapWRS: WRS \\leq M \\times yWRS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;mapWRS%3A%20WRS%20%5Cleq%20M%20%5Ctimes%20yWRS "mapWRS: WRS \leq M \times yWRS")                                                                                        |
| Map the ![WII](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WII "WII") vars to the ![y](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;y "y") binary                                                                                                                            | ![mapWII: WII \\leq M \\times yWII](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;mapWII%3A%20WII%20%5Cleq%20M%20%5Ctimes%20yWII "mapWII: WII \leq M \times yWII")                                                                                        |
| If buy from ![WRS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WRS "WRS"), then can do ![WE1](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WE1 "WE1"). (Use of Mz to choose one constraint)                                                                                  | ![ifWRS\\\_ThenWE1: yWRS \\leq yWE1 + M\\times z](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;ifWRS%5C_ThenWE1%3A%20yWRS%20%5Cleq%20yWE1%20%2B%20M%5Ctimes%20z "ifWRS\_ThenWE1: yWRS \leq yWE1 + M\times z")                                            |
| If ![WE2](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WE2 "WE2"), cannot do ![WII](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WII "WII"). (Use of ![Mz](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;Mz "Mz") to choose one constraint)    | ![ifWRS\\\_thenNotWII: yWE2 + yWII \\leq 1 + M\\times (1-z)](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;ifWRS%5C_thenNotWII%3A%20yWE2%20%2B%20yWII%20%5Cleq%201%20%2B%20M%5Ctimes%20%281-z%29 "ifWRS\_thenNotWII: yWE2 + yWII \leq 1 + M\times (1-z)") |
| If ![WE1](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WE1 "WE1"), then cannot do ![WE2](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WE2 "WE2"), Must choose one                                                                                                             | ![only1WE: yWE1 + yWE2 \\leq 1](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;only1WE%3A%20yWE1%20%2B%20yWE2%20%5Cleq%201 "only1WE: yWE1 + yWE2 \leq 1")                                                                                                  |
| Finally, set ![WE](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WE "WE") to the sum of ![WE1](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WE1 "WE1") and ![WE2](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WE2 "WE2") for the final output | ![setWE: WE = WE1 + WE2](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;setWE%3A%20WE%20%3D%20WE1%20%2B%20WE2 "setWE: WE = WE1 + WE2")                                                                                                                     |

#### 3.1.4.3 WU Constraints

| Description             | Constraint                                                                                                                                                                                                                         |
|:------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Buy at least min amount | ![buyAtLeastMin: WU \\leq availWU \\times yWU](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;buyAtLeastMin%3A%20WU%20%5Cleq%20availWU%20%5Ctimes%20yWU "buyAtLeastMin: WU \leq availWU \times yWU") |
| Under the upper bound   | ![map\\\_yWU: WU \\geq minBuyAmt \\times yWU](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;map%5C_yWU%3A%20WU%20%5Cgeq%20minBuyAmt%20%5Ctimes%20yWU "map\_yWU: WU \geq minBuyAmt \times yWU")      |

#### 3.1.4.4 WOW Constraints

| Description                                                                                                                                                                                                                                                                                                                                                                                                                      | Constraint                                                                                                                                                                                                                                  |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Connect ![WOW](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WOW "WOW") with ![d1WOW](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;d1WOW "d1WOW"), ![d2WOW](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;d2WOW "d2WOW"), and ![d3WOW](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;d3WOW "d3WOW") | ![X\\\_WOW: WOW = d1WOW + d2WOW + d3WOW](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;X%5C_WOW%3A%20WOW%20%3D%20d1WOW%20%2B%20d2WOW%20%2B%20d3WOW "X\_WOW: WOW = d1WOW + d2WOW + d3WOW")                    |
| Ensure that the piece wise costs are used correctly                                                                                                                                                                                                                                                                                                                                                                              | ![piece1a: mcWOW1Upper \\times y1WOW \\leq d1WOW](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;piece1a%3A%20mcWOW1Upper%20%5Ctimes%20y1WOW%20%5Cleq%20d1WOW "piece1a: mcWOW1Upper \times y1WOW \leq d1WOW") |
| First Piece (Between 0 and Upper)                                                                                                                                                                                                                                                                                                                                                                                                | ![piece1b: d1WOW \\leq mcWOW1Upper](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;piece1b%3A%20d1WOW%20%5Cleq%20mcWOW1Upper "piece1b: d1WOW \leq mcWOW1Upper")                                               |
| Second Piece (Between last piece and Upper)                                                                                                                                                                                                                                                                                                                                                                                      | ![piece2a: mcWOW2Upper \\times y2WOW \\leq d2WOW](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;piece2a%3A%20mcWOW2Upper%20%5Ctimes%20y2WOW%20%5Cleq%20d2WOW "piece2a: mcWOW2Upper \times y2WOW \leq d2WOW") |
| Second Piece (Between last piece and Upper)                                                                                                                                                                                                                                                                                                                                                                                      | ![piece2b: d2WOW \\leq mcWOW2Upper \\times y1WOW](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;piece2b%3A%20d2WOW%20%5Cleq%20mcWOW2Upper%20%5Ctimes%20y1WOW "piece2b: d2WOW \leq mcWOW2Upper \times y1WOW") |
| Third Piece (Between last piece and Upper)                                                                                                                                                                                                                                                                                                                                                                                       | ![piece3: d3WOW \\leq mcWOW3Upper \\times y2WOW](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;piece3%3A%20d3WOW%20%5Cleq%20mcWOW3Upper%20%5Ctimes%20y2WOW "piece3: d3WOW \leq mcWOW3Upper \times y2WOW")    |
| Cannot go over upper                                                                                                                                                                                                                                                                                                                                                                                                             | ![upperBoundWOW: WOW \\leq mcWOW3Upper](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;upperBoundWOW%3A%20WOW%20%5Cleq%20mcWOW3Upper "upperBoundWOW: WOW \leq mcWOW3Upper")                                   |

#### 3.1.4.5 Meet the total demand

![
meetTheDemand: WII + WRS + WE + WU + WOW \\geq theDemand
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AmeetTheDemand%3A%20WII%20%2B%20WRS%20%2B%20WE%20%2B%20WU%20%2B%20WOW%20%5Cgeq%20theDemand%0A "
meetTheDemand: WII + WRS + WE + WU + WOW \geq theDemand
")

#### 3.1.4.6 Non-negatitvity or Binary Constraints of Decision Vars

| Description  | Constraint                                                                                                                                                                                                                     |
|:-------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Non-Negative | ![WII, WRS, WU, WE, WOW,](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WII%2C%20WRS%2C%20WU%2C%20WE%2C%20WOW%2C "WII, WRS, WU, WE, WOW,")                                                      |
| \-           | ![WE1, WE2, d1WOW, d2WOW, d3WOW \\geq 0](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;WE1%2C%20WE2%2C%20d1WOW%2C%20d2WOW%2C%20d3WOW%20%5Cgeq%200 "WE1, WE2, d1WOW, d2WOW, d3WOW \geq 0")       |
| Binary       | ![yWRS, yWRS1, yWII, yWE1,](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;yWRS%2C%20yWRS1%2C%20yWII%2C%20yWE1%2C "yWRS, yWRS1, yWII, yWE1,")                                                    |
| \-           | ![yWE2, yWU, y1WOW, y2WOW, z \\in (1,0)](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;yWE2%2C%20yWU%2C%20y1WOW%2C%20y2WOW%2C%20z%20%5Cin%20%281%2C0%29 "yWE2, yWU, y1WOW, y2WOW, z \in (1,0)") |

## 3.2 Code and Output

### 3.2.1 Code

<img src="PDF Submission/Images/prob3CodeAndData1.png" style="width:70.0%" />

<img src="PDF Submission/Images/prob3CodeAndData2.png" style="width:100.0%" />

<img src="PDF Submission/Images/prob3CodeAndData3.png" style="width:100.0%" />

### 3.2.2 Output

> Below shows the amount to produce of each tupe of wigit and its
> respective cost, given the demand

**Summary table of Output**

| Demand | WII  | WRS   | WE   | WU    | WOW   | Total Cost    |
|:-------|:-----|:------|:-----|:------|:------|:--------------|
| 5000   | 0    | 0     | 5000 | 0     | 0     | 19750.000000  |
| 10000  | 3000 | 0     | 7000 | 0     | 0     | 42500.000000  |
| 25000  | 4000 | 14000 | 7000 | 0     | 0     | 99650.000000  |
| 35000  | 0    | 14000 | 6000 | 15000 | 0     | 139650.000000 |
| 45000  | 0    | 14000 | 6000 | 0     | 25000 | 177800.000000 |
| 50000  | 4000 | 14000 | 7000 | 0     | 25000 | 201550.000000 |
| 55000  | 0    | 14000 | 1000 | 15000 | 25000 | 221800.000000 |

**Snapshots of Compilation**

<br>

<img src="PDF Submission/Images/prob3Output1.png">

<img src="PDF Submission/Images/prob3Output2.png">

<img src="PDF Submission/Images/prob3Output3.png">

<img src="PDF Submission/Images/prob3Output4.png">

<img src="PDF Submission/Images/prob3Output5.png">

<img src="PDF Submission/Images/prob3Output6.png">

<img src="PDF Submission/Images/prob3Output7.png">
