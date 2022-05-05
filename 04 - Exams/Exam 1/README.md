Exam 1
================
Daniel Carpenter
March 2022

-   [1 - Problem `1`](#1---problem-1)
    -   [1.1 Mathematical Formulation](#11-mathematical-formulation)
    -   [1.2 Code and Output](#12-code-and-output)
-   [2 - Problem `2`](#2---problem-2)
    -   [2.1 Additions to Model](#21-additions-to-model)
    -   [2.2 Code and Output](#22-code-and-output)
-   [3 - Problem `3`](#3---problem-3)
    -   [3.1 Model Overview](#31-model-overview)
    -   [3.2 Mathematical Formulation](#32-mathematical-formulation)
    -   [3.3 Code and Output](#33-code-and-output)

# 1 - Problem `1`

## 1.1 Mathematical Formulation

### 1.1.1 Sets

| Set Name                                                                                 | Description                                                   |
|:-----------------------------------------------------------------------------------------|:--------------------------------------------------------------|
| ![P](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;P "P") | The three types of products, High-Gloss, Semi-Gloss, and Flat |

### 1.1.2 Parameters

| Parameter Name                                                                                                | Description                                                                                                                                                                                                                                                       |
|:--------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![rawA_p](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;rawA_p "rawA_p")       | The amount of raw ingredient ![A](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;A "A") needed to produce product ![p \\in P](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p%20%5Cin%20P "p \in P") |
| ![rawB_p](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;rawB_p "rawB_p")       | The amount of raw ingredient ![B](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;B "B") needed to produce product ![p \\in P](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p%20%5Cin%20P "p \in P") |
| ![demand_p](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;demand_p "demand_p") | The minimum demand to be met for product ![p \\in P](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p%20%5Cin%20P "p \in P")                                                                                                        |
| ![profit_p](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;profit_p "profit_p") | The associated profit for product ![p \\in P](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p%20%5Cin%20P "p \in P")                                                                                                               |

### 1.1.3 Decision Variables

| Variable Name                                                                                                                   | Description                                                                                                                                                                       |
|:--------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![amtToProduce_p](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;amtToProduce_p "amtToProduce_p") | The amount of product ![p \\in P](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p%20%5Cin%20P "p \in P") to produce and is ion the set of integers |

### 1.1.4 Objective Function

![
maximize \\ theProfit: \\sum_p amtToProduce_p \\times profit_p
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0Amaximize%20%5C%20theProfit%3A%20%5Csum_p%20amtToProduce_p%20%5Ctimes%20profit_p%0A "
maximize \ theProfit: \sum_p amtToProduce_p \times profit_p
")

### 1.1.5 Constraints

**C1:** Meet the minimum demand for each product

![
meetMinDemand: amtToProduce_p \\geq demand_p
, \\ \\forall \\ p \\in P
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AmeetMinDemand%3A%20amtToProduce_p%20%5Cgeq%20demand_p%0A%2C%20%5C%20%5Cforall%20%5C%20p%20%5Cin%20P%0A "
meetMinDemand: amtToProduce_p \geq demand_p
, \ \forall \ p \in P
")

**C2:** Cannot exceed the supply of Raw Material A

![
rawSupplyA: \\sum_p amtToProduce_p \\times rawA_p \\leq 4,000
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0ArawSupplyA%3A%20%5Csum_p%20amtToProduce_p%20%5Ctimes%20rawA_p%20%5Cleq%204%2C000%0A "
rawSupplyA: \sum_p amtToProduce_p \times rawA_p \leq 4,000
")

**C3:** Cannot exceed the supply of Raw Material B

![
rawSupplyB: \\sum_p amtToProduce_p \\times rawB_p \\leq 6,000
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0ArawSupplyB%3A%20%5Csum_p%20amtToProduce_p%20%5Ctimes%20rawB_p%20%5Cleq%206%2C000%0A "
rawSupplyB: \sum_p amtToProduce_p \times rawB_p \leq 6,000
")

**C4:** Ratio of 3:2 for High and Semi Gloss, respectively

-   Since
    ![\\frac{3}{2} = 1.5](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5Cfrac%7B3%7D%7B2%7D%20%3D%201.5 "\frac{3}{2} = 1.5"),
    the amount of high gloss produced must always be
    ![1.5 \\times](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;1.5%20%5Ctimes "1.5 \times")
    semi gloss

    ![
    highToSemiRatio: 1.5 \\times amtToProduce\_{Semi\\in P} = amtToProduce\_{High\\in P}
    ](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AhighToSemiRatio%3A%201.5%20%5Ctimes%20amtToProduce_%7BSemi%5Cin%20P%7D%20%3D%20amtToProduce_%7BHigh%5Cin%20P%7D%0A "
    highToSemiRatio: 1.5 \times amtToProduce_{Semi\in P} = amtToProduce_{High\in P}
    ")

**C5:** Non-Negativity Constraints and is Integer

![
amtToProduce \\geq 0, \\in \\mathbb{Z}
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AamtToProduce%20%5Cgeq%200%2C%20%5Cin%20%5Cmathbb%7BZ%7D%0A "
amtToProduce \geq 0, \in \mathbb{Z}
")

## 1.2 Code and Output

### 1.2.1 Code

<img src="%22Images/prob1CodeAndData.png%22" style="width:90.0%" />

### 1.2.2 Output

-   Not High to Semi is a 3:2 ratio and all demand and supply
    constraints are satisfied.

![](%22Images/prob1Output.png%22)

# 2 - Problem `2`

## 2.1 Additions to Model

> Please assume that the mathematical formulation in the course videos
> are present as well (see code), just named objects are named
> differently but hopefully are convienent to interpret

### 2.1.1 Parameters

| Name                                                                                     | Description                                                                 |
|:-----------------------------------------------------------------------------------------|:----------------------------------------------------------------------------|
| ![M](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;M "M") | “Big M,” which is a large scaler used to help model disjunctive constraints |

### 2.1.2 New Decision Vars

| Name                                                                                                                               | Description                                 |
|:-----------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------|
| ![z](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;z "z")                                           | Determines which constraint to activate.    |
| ![totalProduction](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;totalProduction "totalProduction") | Simple variable that is Zappers + Spacerays |

### 2.1.3 New Constraints

| Description                                                                                                                     | Constraint                                                                                                                                                                                                                                                                                                                                |
|:--------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Set Total Production to Zappers + Spacerays                                                                                     | ![setTotalProd: totalProduction = spaceRays + zappers](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;setTotalProd%3A%20totalProduction%20%3D%20spaceRays%20%2B%20zappers "setTotalProd: totalProduction = spaceRays + zappers")                                                                            |
| If total production is ![\\geq](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5Cgeq "\geq") 400 | ![isGreaterThan400: totalProduction \\geq 400 + M \\times z](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;isGreaterThan400%3A%20totalProduction%20%5Cgeq%20400%20%2B%20M%20%5Ctimes%20z "isGreaterThan400: totalProduction \geq 400 + M \times z")                                                        |
| then zappers must be 70% of total                                                                                               | ![zappersAre70Perc: zappers \\geq 0.70 \\times totalProduction + M \\times z](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;zappersAre70Perc%3A%20zappers%20%5Cgeq%200.70%20%5Ctimes%20totalProduction%20%2B%20M%20%5Ctimes%20z "zappersAre70Perc: zappers \geq 0.70 \times totalProduction + M \times z") |
| If total Production is ![\\leq](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5Cleq "\leq") 400 | ![isLessThan400: totalProduction \\leq 400 + M \\times (1 - z)](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;isLessThan400%3A%20totalProduction%20%5Cleq%20400%20%2B%20M%20%5Ctimes%20%281%20-%20z%29 "isLessThan400: totalProduction \leq 400 + M \times (1 - z)")                                       |
| then no zappers at all                                                                                                          | ![noZappers: spaceRays \\geq totalProduction - M \\times (1 - z)](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;noZappers%3A%20spaceRays%20%5Cgeq%20totalProduction%20-%20M%20%5Ctimes%20%281%20-%20z%29 "noZappers: spaceRays \geq totalProduction - M \times (1 - z)")                                   |

## 2.2 Code and Output

### 2.2.1 Code

<img src="%22Images/prob2CodeAndData.png%22" style="width:85.0%" />

### 2.2.2 Output

-   Optimal solution included more than 400, so zappers are 70% of
    production

![](%22Images/prob2Output.png%22)

# 3 - Problem `3`

## 3.1 Model Overview

### 3.1.1 Assumptions and Calculations for Network Flow Diagram

-   Starting/Ending inventory is 2,000
-   In period 1, can only use inventory to meet demand since it takes a
    period to produce the chemicals. Hence, we can not manufacture in
    period 1.
-   ![\\mu](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5Cmu "\mu")
    used to either show:
    -   The 85:100 ratio when converting raw materials in production
        (seen as 0.85)
    -   Converting the final product into dollars when selling, or
    -   Showing the 8% degradation when storing the final product in
        inventory that did not sell (seen as 0.92, which is 1 minus 8%)
-   To balance the network, a virtual node is used (the black node) and
    its dependent arcs use multipliers of 0.
    -   Note many nodes send through here because there must be minimum
        demand and maximum, therefore we cannot send all unused product
        through the demand and then to the balance node
    -   So, some products must be zeroed out in the final product stage.
    -   Period 4 assumes that some products are produced, but are zeroed
        out. This assumption is made since it takes a period in advance
        to manufacture the product. Node shown nonetheless.
-   End of period 4 shown like another period for simplicity

### 3.1.2 Network Flow Diagram

<img src="%22Images/network.png%22" style="width:100.0%" />

## 3.2 Mathematical Formulation

### 3.2.1 Sets, Parameters, Decision Vars

| Description                                                                                          | Nodes in the actual model                                                                                                                                            |
|:-----------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![NODES](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;NODES "NODES") | Set of all nodes in above network flow diagram:                                                                                                                      |
| Inventory, plus ending i in period 4                                                                 | ![i1, i2, i3, i4, i4end](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;i1%2C%20i2%2C%20i3%2C%20i4%2C%20i4end "i1, i2, i3, i4, i4end") |
| Produce the chemicals                                                                                | ![p1, p2, p3, p4](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p1%2C%20p2%2C%20p3%2C%20p4 "p1, p2, p3, p4")                          |
| Manufacture the Product                                                                              | ![m2, m3, m4](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;m2%2C%20m3%2C%20m4 "m2, m3, m4")                                          |
| The Final Product is made                                                                            | ![f1, f2, f3, f4](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;f1%2C%20f2%2C%20f3%2C%20f4 "f1, f2, f3, f4")                          |
| Meet the demand                                                                                      | ![d1, d2, d3, d4](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;d1%2C%20d2%2C%20d3%2C%20d4 "d1, d2, d3, d4")                          |
| Flow balance zero out node                                                                           | ![z4](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;z4 "z4")                                                                          |

<img src="%22Images/glm1.png%22" style="width:70.0%" />

### 3.2.2 Objective, and Constraints

<img src="%22Images/glm2.png%22" style="width:70.0%" />

-   Upper and lower bounds use to direct the flow of the product

## 3.3 Code and Output

### 3.3.1 Model: `Problem3.mod`

-   Used `gmcnfp.txt` from course website and renamed to `Problem3.mod`.
-   Added `Problem3.dat;` `solve;` and `display x;`

### 3.3.2 Data: `Problem3.dat`

<img src="%22Images/prob3CodeAndData.png%22" style="width:80.0%" />

### 3.3.3 Output

-   Below shows how much of product is sent from node i to node j
-   i is displayed on each row, and j is on each column
-   For example, f3 sent 2,800 gallons to d3, interpreted as follows:
    -   In period 3, 2,800 gallons of product were demanded.
-   Note that values sent to virtual node means that nothing those
    values were not produced.

![](%22Images/prob3Output.png%22)
