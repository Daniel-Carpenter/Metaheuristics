Homework 2 - Advanced LP & Network Flow Models
================
Daniel Carpenter and Christopher Ferguson
February 2022

-   [1 - Problem `1`](#1---problem-1)
    -   [1.1 Problems `a` and `b`](#11-problems-a-and-b)
    -   [1.2 Model Assumptions and
        Overview](#12-model-assumptions-and-overview)
    -   [1.3 Mathematical Formulation](#13-mathematical-formulation)
        -   [1.3.1 Sets](#131-sets)
        -   [1.3.2 Parameters](#132-parameters)
        -   [1.3.3 Decision Variables](#133-decision-variables)
        -   [1.3.4 Objective Function](#134-objective-function)
        -   [1.3.5 Constraints](#135-constraints)
    -   [1.4 Code and Output](#14-code-and-output)
        -   [1.4.1 Code](#141-code)
        -   [1.4.2 Output](#142-output)
    -   [1.5 Problems 1 `c (ii-vii)`](#15-problems-1-c-ii-vii)
    -   [1.6 Problems 1 `d`](#16-problems-1-d)
        -   [1.6.1 Output](#161-output)
        -   [1.6.2 Code](#162-code)
-   [2 - Problem `2`](#2---problem-2)
    -   [2.1 Model Overview](#21-model-overview)
    -   [2.2 Mathematical Formulation](#22-mathematical-formulation)
        -   [2.2.1 Objective, and
            Constraints](#221-objective-and-constraints)
    -   [2.3 Code and Output](#23-code-and-output)
        -   [2.3.1 Model
            `group12_HW2_p2.mod`](#231-model-group12_hw2_p2mod)
        -   [2.3.2 Data
            `group12_HW2_p2.dat`](#232-data-group12_hw2_p2dat)
        -   [2.3.3 Output](#233-output)
-   [3 - Problem `3`](#3---problem-3)
    -   [3.1 Model Overview](#31-model-overview)
        -   [3.1.1 Assumptions and Calculations for Network Flow
            Diagram](#311-assumptions-and-calculations-for-network-flow-diagram)
        -   [3.1.2 Network Flow Diagram](#312-network-flow-diagram)
    -   [3.2 Mathematical Formulation](#32-mathematical-formulation)
        -   [3.2.1 Sets, Parameters, Decision
            Vars](#321-sets-parameters-decision-vars)
        -   [3.2.2 Objective, and
            Constraints](#322-objective-and-constraints)
    -   [3.3 Code and Output](#33-code-and-output)
        -   [3.3.1 Model:
            `group12_HW2_p3.mod`](#331-model-group12_hw2_p3mod)
        -   [3.3.2 Data:
            `group12_HW2_p3.dat`](#332-data-group12_hw2_p3dat)
        -   [3.3.3 Output](#333-output)
-   [4 - Problem `4`](#4---problem-4)
    -   [4.1 Model Overview](#41-model-overview)
        -   [4.1.1 Assumptions and Calculations for Network Flow
            Diagram](#411-assumptions-and-calculations-for-network-flow-diagram)
        -   [4.1.2 Network Flow Diagram](#412-network-flow-diagram)
    -   [4.2 Mathematical Formulation](#42-mathematical-formulation)
        -   [4.2.1 Sets, Parameters, Decision
            Vars](#421-sets-parameters-decision-vars)
        -   [4.2.2 Objective, and
            Constraints](#422-objective-and-constraints)
    -   [4.3 Code and Output](#43-code-and-output)
        -   [4.3.1 Model:
            `group12_HW2_p4.mod`](#431-model-group12_hw2_p4mod)
        -   [4.3.2 Data:
            `group12_HW2_p4.dat`](#432-data-group12_hw2_p4dat)
        -   [4.3.3 Output](#433-output)

# 1 - Problem `1`

## 1.1 Problems `a` and `b`

-   Below shows how we get to the answer of Problems `a` and `b`  
    <img src="PDF Submission/Images/prob1aAndB.png">

## 1.2 Model Assumptions and Overview

-   This model calculates the maximum profit using varying models from
    the boards, for a set of products and inputs grades (See below
    sets).

## 1.3 Mathematical Formulation

### 1.3.1 Sets

| Set Name                                                                                                      | Description                                                             |
|:--------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------|
| ![FRUIT](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;FRUIT "FRUIT")          | Fruit grade levels of grapes, which are `Grade A` and `Grade B` grapes  |
| ![PRODUCTS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;PRODUCTS "PRODUCTS") | Types of products to be sold, which are `Raisins`, `Juice`, and `Jelly` |

### 1.3.2 Parameters

| Parameter Name                                                                                                                                 | Description                                                                                                                                                                                       |
|:-----------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![amountOfFruit_f](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;amountOfFruit_f "amountOfFruit_f")             | *Pounds* of fruit grade (![f\\in FRUIT](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;f%5Cin%20FRUIT "f\in FRUIT")) available to use                               |
| ![avgGradeOfFruit_f](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;avgGradeOfFruit_f "avgGradeOfFruit_f")       | Avg. point quality of fruit grade (![f\\in FRUIT](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;f%5Cin%20FRUIT "f\in FRUIT"))                                      |
| ![productLimit_p](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;productLimit_p "productLimit_p")                | Upper bound of number of products (![p\\in PRODUCTS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p%5Cin%20PRODUCTS "p\in PRODUCTS")) to produce                  |
| ![poundsPerProduct_p](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;poundsPerProduct_p "poundsPerProduct_p")    | The amount of pounds associated with a single unit of product (![p\\in PRODUCTS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p%5Cin%20PRODUCTS "p\in PRODUCTS")) |
| ![contrToProfit_p](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;contrToProfit_p "contrToProfit_p")             | The contribution to profit of product (![p\\in PRODUCTS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p%5Cin%20PRODUCTS "p\in PRODUCTS"))                         |
| ![netProfit_p](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;netProfit_p "netProfit_p")                         | The net profit (*net of OH allocation*) of product (![p\\in PRODUCTS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p%5Cin%20PRODUCTS "p\in PRODUCTS"))            |
| ![productGradeLimit_p](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;productGradeLimit_p "productGradeLimit_p") | Requirement of mean point quality of a product (![p\\in PRODUCTS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p%5Cin%20PRODUCTS "p\in PRODUCTS"))                |

### 1.3.3 Decision Variables

| Variable Name                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                    |
|:------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![produce\_{f,p}](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;produce_%7Bf%2Cp%7D "produce_{f,p}") | Number (*as integer*) of products (![p\\in PRODUCTS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p%5Cin%20PRODUCTS "p\in PRODUCTS")) to be produced by fruit grade (![f\\in FRUIT](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;f%5Cin%20FRUIT "f\in FRUIT")) |

### 1.3.4 Objective Function

![
Maximize \\ Net\\\_Profit: \\sum\_{f\\in FRUIT,p\\in PRODUCTS} produce\_{f,p} \\times netProfit_p
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AMaximize%20%5C%20Net%5C_Profit%3A%20%5Csum_%7Bf%5Cin%20FRUIT%2Cp%5Cin%20PRODUCTS%7D%20produce_%7Bf%2Cp%7D%20%5Ctimes%20netProfit_p%0A "
Maximize \ Net\_Profit: \sum_{f\in FRUIT,p\in PRODUCTS} produce_{f,p} \times netProfit_p
")

### 1.3.5 Constraints

**C1:** For each fruit grade
(![f\\in FRUIT](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;f%5Cin%20FRUIT "f\in FRUIT")),
the number of products produced
(![p\\in PRODUCTS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p%5Cin%20PRODUCTS "p\in PRODUCTS"))
must be equal to numbers of fruit provided

![
maxWeight: \\sum\_{p\\in PRODUCTS} (produce\_{f,p} \\times numbersPerProduct_p) = amountOfFruit_f
, \\ \\forall \\ f\\in FRUIT
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AmaxWeight%3A%20%5Csum_%7Bp%5Cin%20PRODUCTS%7D%20%28produce_%7Bf%2Cp%7D%20%5Ctimes%20numbersPerProduct_p%29%20%3D%20amountOfFruit_f%0A%2C%20%5C%20%5Cforall%20%5C%20f%5Cin%20FRUIT%0A "
maxWeight: \sum_{p\in PRODUCTS} (produce_{f,p} \times numbersPerProduct_p) = amountOfFruit_f
, \ \forall \ f\in FRUIT
")

**C2:** For each product produced
(![p\\in PRODUCTS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p%5Cin%20PRODUCTS "p\in PRODUCTS")),
limit the number of products
![p](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p "p")
produced to
![\\leq](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5Cleq "\leq")
to the demanded (product numbers)

![
demand: \\sum\_{f\\in FRUIT} produce\_{f,p} \\leq productLimit_p
, \\ \\forall \\ p\\in PRODUCTS
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0Ademand%3A%20%5Csum_%7Bf%5Cin%20FRUIT%7D%20produce_%7Bf%2Cp%7D%20%5Cleq%20productLimit_p%0A%2C%20%5C%20%5Cforall%20%5C%20p%5Cin%20PRODUCTS%0A "
demand: \sum_{f\in FRUIT} produce_{f,p} \leq productLimit_p
, \ \forall \ p\in PRODUCTS
")

**C3:** For each product
(![p\\in PRODUCTS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p%5Cin%20PRODUCTS "p\in PRODUCTS")),
the grade of fruit
(![f\\in FRUIT](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;f%5Cin%20FRUIT "f\in FRUIT"))
is greater than the minimum required grade of the product
(![p\\in PRODUCTS](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;p%5Cin%20PRODUCTS "p\in PRODUCTS")).  
![minAvgGrade:](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;minAvgGrade%3A "minAvgGrade:")

![
\\sum\_{f\\in FRUIT} (produce\_{f,p} \\times avgGradeOfFruit_f) \\geq productGradeLimit_p \\times \\sum\_{f\\in FRUIT} (produce\_{f,p}),
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0A%5Csum_%7Bf%5Cin%20FRUIT%7D%20%28produce_%7Bf%2Cp%7D%20%5Ctimes%20avgGradeOfFruit_f%29%20%5Cgeq%20productGradeLimit_p%20%5Ctimes%20%5Csum_%7Bf%5Cin%20FRUIT%7D%20%28produce_%7Bf%2Cp%7D%29%2C%0A "
\sum_{f\in FRUIT} (produce_{f,p} \times avgGradeOfFruit_f) \geq productGradeLimit_p \times \sum_{f\in FRUIT} (produce_{f,p}),
")

![
\\forall \\ p\\in PRODUCTS
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0A%5Cforall%20%5C%20p%5Cin%20PRODUCTS%0A "
\forall \ p\in PRODUCTS
")

**C4:** Non-negativity constraints

![
produce\_{\\ f,p} \\geq 0, \\ \\forall \\ f\\in FRUIT, \\ \\forall \\ p\\in PRODUCTS \\\\
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0Aproduce_%7B%5C%20f%2Cp%7D%20%5Cgeq%200%2C%20%5C%20%5Cforall%20%5C%20f%5Cin%20FRUIT%2C%20%5C%20%5Cforall%20%5C%20p%5Cin%20PRODUCTS%20%5C%5C%0A "
produce_{\ f,p} \geq 0, \ \forall \ f\in FRUIT, \ \forall \ p\in PRODUCTS \\
")

## 1.4 Code and Output

### 1.4.1 Code

<img src="PDF Submission/Images/prob1CodeAndData.png" style="width:90.0%" />

### 1.4.2 Output

<img src="PDF Submission/Images/prob1Output.png">

Optimal profit is `$107,600`. `74,996` `Raisins` produced using
`Grade A`, `24,988` of `Grade B`, and so on for each product. See
validation of the weighted-average point constraint below.

<img src="PDF Submission/Images/prob1OutputValidation.png">

## 1.5 Problems 1 `c (ii-vii)`

`i.`

<img src="PDF Submission/Images/probl1ci.jpg)

Product total = (Amount of Grade A product + Amount of Grade B product)
Raisins - 74996 + 24988 = 99984 Raisins  
Juice - 31609 + 94827 = 126436 Juice  
Jelly - 0 + 210000 = 210000 Jelly

`ii.` Max contribution of profit = Sum of all products (Product total \*
contribution to profit of product)

Raisins - 99984 \* 1.40 = $139977.60  
+ Juice - 126436 \* 2.46 = $311032.56  
+ Jelly - 210000 \* 2.35 = $493500  
= Total - $944510.16

The maximum contribution to profit will be $944510.16

`iii.` Grade A grapes left over = Total Grade A - sum of Grade A grapes
in products:  
930000- ((74996\* 6.5)+(31609\*14)+0) = 0

Grade B grapes left over = Total Grade B - sum of Grade B grapes in
products:  
5270000 - ((24988\* 6.5)+(94827 \* 14)+(210000\*18)) = 0

There are no grapes left over according to the optimal solution.

`iv.` Product total points = ( \# of Grade A in Product \* 9 + \# of
Grade B \* 5) / Total Product

Raisins - (74996 \* 9 + 24988 \* 5) / (99984) = 8  
Juice - (31609 \* 9 + 94827 \* 5) / (126436) = 6  
Jelly - (0 \* 9 + 210000 \* 5) / (210000) = 5

`v.`  
<img src="PDF Submission/Images/probl1cv.jpg)

(option display_precision 8): puts the answer in decimal using 8 digits

(Total profit of model + 1 additional pound of Grade A grapes) - (Total
profit of original)  
107592.52 - 107593.36 = .16

`vi.` No, they should not buy the additional 300,000 pounds of A-grade
grapes at .50 per pound.

`vii.` The maximum price that Grapes of Wrath should pay for an extra
pound of A-grade product would be .16.

The maximum price that Grapes of Wrath should pay for an extra pound of
B-grade product would be 2.96. Our model will not show the upper bound
on the price per product that can serve the model.

(Total profit of model + 1 additional pound of Grade B grapes) - (Total
profit of original)  
107596.28 - 107593.36= 2.92

## 1.6 Problems 1 `d`

`i.` The product mix that would be made by using Thomas’s contribution
figures are  
gradeA raisins 40760  
gradeA juice 47503  
gradeA jelly 1  
gradeB raisins 13582  
gradeB juice 142496  
gradeB jelly 177043

Thomas’s profit contribution is $959,529.74 The maximum that they should
pay for an additional pound of A-grade grapes is .16.

`ii.`

<img src="PDF Submission/Images/prob1dCode.png" style="width:90.0%" />

### 1.6.1 Output

<img src="PDF Submission/Images/prob1dOutput.png" style="width:80.0%" />

-   The maximum to pay per pound would be equal to the dual variable of
    the active constraint, which does not show any values.

`iii.`

### 1.6.2 Code

-   The model who should be used is Thomas’ method, which yields the
    highest profit. An enhancement would be to be only compare net
    profit or contribution margins.

<br>

# 2 - Problem `2`

## 2.1 Model Overview

<img src="PDF Submission/Images/prob2.Network.png" style="width:100.0%" />

## 2.2 Mathematical Formulation

![NODES](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;NODES "NODES"):
Set of all nodes in above network flow diagram resembling a time period.

<img src="PDF Submission/Images/prob4Math1.png" style="width:50.0%" />

### 2.2.1 Objective, and Constraints

<img src="PDF Submission/Images/prob4Math2.png" style="width:50.0%" />

## 2.3 Code and Output

### 2.3.1 Model `group12_HW2_p2.mod`

-   Used `mcnfp.txt` from course website and renamed to
    `group12_HW2_p2.mod`.
-   Added `data group12_HW2_p2.dat;` `solve;` and `display x;`

### 2.3.2 Data `group12_HW2_p2.dat`

<img src="PDF Submission/Images/prob2.2.jpg)

### 2.3.3 Output

-   The lowest total cost over the `5 years` will be `$14,500` by
    traveling from nodes `(1,2)`, `(2,4)`, `(4,6)`.

<img src="PDF Submission/Images/prob2.Answer.jpg" style="width:35.0%" />

<br>

# 3 - Problem `3`

## 3.1 Model Overview

### 3.1.1 Assumptions and Calculations for Network Flow Diagram

-   Below shows how we decided to balance the network with supply and
    dummy nodes
-   In order to obtain a balanced network (i.e. supply equals demand),
    we must allow for all possible routes to have enough supply.
-   Excess supply allowed on certain days is captured by dummy nodes so
    that the business does not actually produce the tires.

<img src="PDF Submission/Images/prob3Overview2.png" style="width:90.0%" />

### 3.1.2 Network Flow Diagram

<img src="PDF Submission/Images/prob3Overview.png" style="width:100.0%" />

## 3.2 Mathematical Formulation

### 3.2.1 Sets, Parameters, Decision Vars

| Set Name                                                                                             | Description                                                                                                                                                                                                |
|:-----------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![NODES](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;NODES "NODES") | Set of all nodes in above network flow diagram:                                                                                                                                                            |
| `p1` `p2` `p3` `p4`                                                                                  | Number of tires to *purchase* on day ![\\in](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5Cin "\in")(1-4)                                                                |
| `n1` `n2` `n3` `n4`                                                                                  | Number of tires to reshape using the *normal* service on day ![\\in](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5Cin "\in")(1-4)                                        |
| `q1` `q2` `q3` `q4`                                                                                  | Number of tires to reshape using the *quick* service on day ![\\in](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5Cin "\in")(1-4)                                         |
| `d1` `d2` `d3` `d4`                                                                                  | Demand of tires on each day ![\\in](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5Cin "\in")(1-4)                                                                         |
| `dum2` `dum3` `dum4`                                                                                 | Dummy nodes to balance excess supply for days 2 3 and 4 ![\\in](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5Cin "\in")(2-4). Do not need one for day 1 since purchasing |

<img src="PDF Submission/Images/prob4Math1.png" style="width:70.0%" />

### 3.2.2 Objective, and Constraints

<img src="PDF Submission/Images/prob4Math2.png" style="width:70.0%" />

-   Upper and lower bounds use to direct the flow of tires from
    *purchasing* to *quick* or *normal* service

## 3.3 Code and Output

### 3.3.1 Model: `group12_HW2_p3.mod`

-   Used `mcnfp.txt` from course website and renamed to
    `group12_HW2_p3.mod`.
-   Added `data group12_HW2_p3.dat;` `solve;` and `display x;`

### 3.3.2 Data: `group12_HW2_p3.dat`

<img src="PDF Submission/Images/prob3Data1.png" style="width:70.0%" />

*Data Continued:*  
<img src="PDF Submission/Images/prob3Data2.png" style="width:70.0%" />

### 3.3.3 Output

-   Total minimized cost: `396,720`
-   Interpretation of the tires purchased on each day:
    1.  `320` tires purchased
    2.  `240` tires reshaped with Quick Service from previous day
    3.  `80` Reshaped with quick service from previous day. `320` tires
        used from reshaping via Normal service from day 1.
    4.  `280` Reshaped with quick service from previous day. `240` tires
        used from reshaping via Normal service from day 2.

<img src="PDF Submission/Images/prob3Output.png" style="width:70.0%" />

# 4 - Problem `4`

## 4.1 Model Overview

### 4.1.1 Assumptions and Calculations for Network Flow Diagram

-   Goal of below tables are to put all data on a *per unit of product*
    basis
-   Need to be on per unit basis so that we can effectively minimize the
    cost
-   *Color of tables* correspond to the network nodes on the next page

<img src="PDF Submission/Images/prob4Overview2.png" style="width:100.0%" />

### 4.1.2 Network Flow Diagram

<img src="PDF Submission/Images/prob4Overview.png" style="width:100.0%" />

## 4.2 Mathematical Formulation

### 4.2.1 Sets, Parameters, Decision Vars

| Set Name                                                                                             | Description                                                                        |
|:-----------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
| ![NODES](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;NODES "NODES") | Set of all nodes in above network flow diagram:                                    |
| `Specialist`, `Generalist`                                                                           | The two types of Supply of Labor                                                   |
| `ScranMult1x`, `UticaMult1x`, `StamMult1x`                                                           | Passed through if *did not* use overtime                                           |
| `ScranMultOT`, `UticaMultOT`, `StamMultOT`                                                           | Passed through if *did* use overtime                                               |
| `Scranton`, `Utica`, `Stamford`                                                                      | Transshipment nodes which are the plants                                           |
| `dumPlant`, `dumBus`                                                                                 | Dummy nodes that account for excess supply from unbalanced supply from labor nodes |

<img src="PDF Submission/Images/prob4Math1.png" style="width:70.0%" />

### 4.2.2 Objective, and Constraints

<img src="PDF Submission/Images/prob4Math2.png" style="width:70.0%" />

-   Upper and lower bounds use to direct the flow of the product

## 4.3 Code and Output

### 4.3.1 Model: `group12_HW2_p4.mod`

-   Used `mcnfp.txt` from course website and renamed to
    `group12_HW2_p4.mod`.
-   Added `data group12_HW2_p4.dat;` `solve;` and `display x;`

### 4.3.2 Data: `group12_HW2_p4.dat`

<img src="PDF Submission/Images/prob4Data1.png" style="width:85.0%" />

*Data Continued:*  
<img src="PDF Submission/Images/prob4Data2.png" style="width:100.0%" />

### 4.3.3 Output

-   Total minimized cost: `$806,192.95`
-   Scranton, Utica, and Stamford produce `0`, `430`, and `170` units of
    product for **Faceblock**, respectively.
-   Scranton, Utica, and Stamford produce `605`, `0`, and `395` units of
    product for **Goggle**, respectively.
-   All possible products produced (using a portion of the available
    regular and overtime hours). `200` products produced by Specialists
    using OT, and `100` from generalists using OT.

<img src="PDF Submission/Images/prob4Output.png" style="width:100.0%" />
