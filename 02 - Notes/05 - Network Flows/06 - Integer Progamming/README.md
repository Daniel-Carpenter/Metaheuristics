# Integer Programming
> 

## Overview

### General Overview
* More complex
* Medium or Large size could take a long time
* Cannot do sensativity analysis!
* Small problems are usually fine
* Min Cost Flow Network Problem naturally Integer
* Can round to the nearest integer for an LP problem with large siginificant digits. DOn't do this for small number problems like choose 1 or 2 cars.


### Examples of Integer Programs
* Capital budgeting
* Facility Location
* Warehouse Location
* Sequencing

### Some Problems can only be formed as Integer Problems
* Yes/No Decisions (Investments, etc)
* Continguint Decisions (if x, then y)
* Disjunctive (Either/Or)
* Restrictive set or range of decision variables (x = 0, or x > 15)
* Fixed Costs
* Piecewise linear cors (economies of scale)

## Yes/No Decisions
> W=Deciside to engage in something or not

### Example of Yes/No Decisions:
Select only one of the following:
1. To build a new plant
2. Take an advertising campaign, or
3. DEvelope a new product

#### The Decision Variables
Sum of the decision variables (the three above) must be 1

#### Types of Restrictions (Constraints)
* Select at least one option (k of n)
* Select at most some options (k of n)
* Select exactly one options (k of n)

<img src = "Images/cons.png" width = 550> <br>
<!-- <img src = "Images/.png" width = 550> <br> -->