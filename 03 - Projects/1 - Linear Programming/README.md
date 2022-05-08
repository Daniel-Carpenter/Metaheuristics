Homework 1 - Truth Tables & Linear Programming with AMPL
================
Daniel Carpenter and Effouehi Moody
January 2022

<!-- -   [1 Problem `1`](#1-problem-1)
-   [2 Problem `2`](#2-problem-2) -->
-   [3 Problem `3`](#3-problem-3)
    -   [3.1 Task `a`](#31-task-a)
        -   [3.1.1 Decision Variables](#311-decision-variables)
        -   [3.1.2 Objective Function](#312-objective-function)
        -   [3.1.3 Constraints](#313-constraints)
        -   [3.1.4 Code](#314-code)
        -   [3.1.5 Output](#315-output)
-   [4 Problem `4`](#4-problem-4)
    -   [4.1 Task `a`](#41-task-a)
        -   [4.1.1 Decision Variables](#411-decision-variables)
        -   [4.1.2 Objective Function](#412-objective-function)
        -   [4.1.3 Constraints](#413-constraints)
        -   [4.1.4 Code](#414-code)
        -   [4.1.5 Output](#415-output)
        -   [4.1.6 Solving Problem `4(a)` Graphically by
            Hand](#416-solving-problem-4a-graphically-by-hand)
    -   [4.2 Task `b`](#42-task-b)
        -   [4.2.1 Additional Constraint: Labor
            Time](#421-additional-constraint-labor-time)
        -   [4.2.2 Code](#422-code)
        -   [4.2.3 Output](#423-output)
    -   [4.3 Task `c`](#43-task-c)
        -   [4.3.1 Additional Constraint: Radio Advertising
            Medium](#431-additional-constraint-radio-advertising-medium)
        -   [4.3.2 Decision Variables](#432-decision-variables)
        -   [4.3.3 Objective Function](#433-objective-function)
        -   [4.3.4 New Constraints](#434-new-constraints)
        -   [4.3.5 Code](#435-code)
        -   [4.3.6 Output](#436-output)
    -   [4.4 Task `d`](#44-task-d)
        -   [4.4.1 Additional Constraints: Miminum Magazine and Maximum
            Radio
            Requirements](#441-additional-constraints-miminum-magazine-and-maximum-radio-requirements)
        -   [4.4.2 Code](#442-code)
        -   [4.4.3 Output](#443-output)
-   [5 Problem `5`](#5-problem-5)
    -   [5.1 Base Mathematical Formulation and
        Code](#51-base-mathematical-formulation-and-code)
        -   [5.1.1 Mathematical
            Formulation](#511-mathematical-formulation)
        -   [5.1.2 Code for Model `.mod` and Input Data
            `.dat`](#512-code-for-model-mod-and-input-data-dat)
    -   [5.2 Task `a`](#52-task-a)
        -   [5.2.1 Changed Constraint for Total
            Hours](#521-changed-constraint-for-total-hours)
        -   [5.2.2 Code](#522-code)
        -   [5.2.3 Output](#523-output)
    -   [5.3 Task `b`](#53-task-b)
        -   [5.3.1 New Constraint for Max
            Weight](#531-new-constraint-for-max-weight)
        -   [5.3.2 Code](#532-code)
        -   [5.3.3 Output](#533-output)
    -   [5.4 Task `c`](#54-task-c)
        -   [5.4.1 Changed Objective
            Function](#541-changed-objective-function)
        -   [5.4.2 Code](#542-code)
        -   [5.4.3 Output](#543-output)
    -   [5.5 Task `d`](#55-task-d)
        -   [5.5.1 New Constraint](#551-new-constraint)
        -   [5.5.2 Code (Part I)](#552-code-part-i)
        -   [5.5.3 Output (Part I)](#553-output-part-i)
        -   [5.5.4 Code (Part II)](#554-code-part-ii)
        -   [5.5.5 Output (Part II)](#555-output-part-ii)
    -   [5.6 Task `e`](#56-task-e)
        -   [5.6.1 Changing Input Data via `.dat`
            File](#561-changing-input-data-via-dat-file)
        -   [5.6.2 Output](#562-output)
-   [6 Problem `6`](#6-problem-6)
    -   [6.1 Task `a` - `c`](#61-task-a---c)
        -   [6.1.1 Decision Variables](#611-decision-variables)
        -   [6.1.2 Objective Function](#612-objective-function)
        -   [6.1.3 Constraints](#613-constraints)
        -   [6.1.4 Code](#614-code)
        -   [6.1.5 Output](#615-output)
    -   [6.2 Task `d`:](#62-task-d)
    -   [6.3 Task `e`:](#63-task-e)

<!-- # 1 Problem `1`

<img src="PDF Submission/Output_Images/problem1.1.jpg">

<img src="PDF Submission/Output_Images/problem1.2.jpg">

<br>

# 2 Problem `2`

<img src="PDF Submission/Output_Images/problem2.jpg"> -->

<br>

# 3 Problem `3`

## 3.1 Task `a`

### 3.1.1 Decision Variables

`bondA`: dollars
![\\in \\mathbb{R}](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5Cin%20%5Cmathbb%7BR%7D "\in \mathbb{R}")
to invest in bond A  
`bondB`: dollars
![\\in \\mathbb{R}](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5Cin%20%5Cmathbb%7BR%7D "\in \mathbb{R}")
to invest in bond B  
`bondC`: dollars
![\\in \\mathbb{R}](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5Cin%20%5Cmathbb%7BR%7D "\in \mathbb{R}")
to invest in bond C  
`bondD`: dollars
![\\in \\mathbb{R}](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5Cin%20%5Cmathbb%7BR%7D "\in \mathbb{R}")
to invest in bond D  
`bondE`: dollars
![\\in \\mathbb{R}](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5Cin%20%5Cmathbb%7BR%7D "\in \mathbb{R}")
to invest in bond E

### 3.1.2 Objective Function

-   Maximize the Expected Earnings of the portfolio

![
Maximize \\ Z = (0.043 \\times bondA) + (0.027 \\times bondB) + (0.025 \\times bondC) + (0.022 \\times bondD) + (0.045 \\times bondE)
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AMaximize%20%5C%20Z%20%3D%20%280.043%20%5Ctimes%20bondA%29%20%2B%20%280.027%20%5Ctimes%20bondB%29%20%2B%20%280.025%20%5Ctimes%20bondC%29%20%2B%20%280.022%20%5Ctimes%20bondD%29%20%2B%20%280.045%20%5Ctimes%20bondE%29%0A "
Maximize \ Z = (0.043 \times bondA) + (0.027 \times bondB) + (0.025 \times bondC) + (0.022 \times bondD) + (0.045 \times bondE)
")

### 3.1.3 Constraints

**C1:** Budget to invest is $10 MM or less

![
budget: bondA + bondB + bondC + bondD + bondE \\leq 10
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0Abudget%3A%20bondA%20%2B%20bondB%20%2B%20bondC%20%2B%20bondD%20%2B%20bondE%20%5Cleq%2010%0A "
budget: bondA + bondB + bondC + bondD + bondE \leq 10
")

**C2:** At least $4 million must be invested in government and agency
bonds

![
govtAndAgency: bondB + bondC + bondD \\geq 4
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AgovtAndAgency%3A%20bondB%20%2B%20bondC%20%2B%20bondD%20%5Cgeq%204%0A "
govtAndAgency: bondB + bondC + bondD \geq 4
")

**C3:** Average Quality of the Portfolio must not exceed 1.4

![
avgQuality: (0.6 \\times bondA) + (0.6 \\times bondB) - (0.4 \\times bondC) 
- (0.4 \\times bondD) + (3.6 \\times bondE) \\leq 0
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AavgQuality%3A%20%280.6%20%5Ctimes%20bondA%29%20%2B%20%280.6%20%5Ctimes%20bondB%29%20-%20%280.4%20%5Ctimes%20bondC%29%20%0A-%20%280.4%20%5Ctimes%20bondD%29%20%2B%20%283.6%20%5Ctimes%20bondE%29%20%5Cleq%200%0A "
avgQuality: (0.6 \times bondA) + (0.6 \times bondB) - (0.4 \times bondC) 
- (0.4 \times bondD) + (3.6 \times bondE) \leq 0
")

**C4:** The Average Maturity must not Exceed Five Years

![
avgMaturity: (4 \\times bondA) + (10 \\times bondB) - (1 \\times bondC) 
- (2 \\times bondD) - (3 \\times bondE) \\leq 0
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AavgMaturity%3A%20%284%20%5Ctimes%20bondA%29%20%2B%20%2810%20%5Ctimes%20bondB%29%20-%20%281%20%5Ctimes%20bondC%29%20%0A-%20%282%20%5Ctimes%20bondD%29%20-%20%283%20%5Ctimes%20bondE%29%20%5Cleq%200%0A "
avgMaturity: (4 \times bondA) + (10 \times bondB) - (1 \times bondC) 
- (2 \times bondD) - (3 \times bondE) \leq 0
")

<br>

### 3.1.4 Code

<img src="PDF Submission/Output_Images/codeProblem3.png">

### 3.1.5 Output

<img src="PDF Submission/Output_Images/outputProblem3.png">

<br>

# 4 Problem `4`

## 4.1 Task `a`

### 4.1.1 Decision Variables

`tv` = the number of minutes
![\\in \\mathbb{R}](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5Cin%20%5Cmathbb%7BR%7D "\in \mathbb{R}")
to air advertising on the *television* medium  
`magazine` = the number of pages
![\\in \\mathbb{I}](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5Cin%20%5Cmathbb%7BI%7D "\in \mathbb{I}")
to to advertise on the *magazine* medium

### 4.1.2 Objective Function

-   Maximize the total audience reach

![
Maximize \\ Z = (1.8\\times tv) + (1.0 \\times magazine)
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AMaximize%20%5C%20Z%20%3D%20%281.8%5Ctimes%20tv%29%20%2B%20%281.0%20%5Ctimes%20magazine%29%0A "
Maximize \ Z = (1.8\times tv) + (1.0 \times magazine)
")

### 4.1.3 Constraints

**C1**: Must not Exceed Budget of 1 Million dollars  

![
budget: (20,000 \\times tv) + (10,000 \\times magazine) \\leq 1,000,000
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0Abudget%3A%20%2820%2C000%20%5Ctimes%20tv%29%20%2B%20%2810%2C000%20%5Ctimes%20magazine%29%20%5Cleq%201%2C000%2C000%0A "
budget: (20,000 \times tv) + (10,000 \times magazine) \leq 1,000,000
")

**C2**: Must have at least 10 minutes of air time on the TV medium  

![
minTimeTV: tv \\geq 10
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AminTimeTV%3A%20tv%20%5Cgeq%2010%0A "
minTimeTV: tv \geq 10
")

<br>

### 4.1.4 Code

<img src="PDF Submission/Output_Images/codeProblem4a.png">

### 4.1.5 Output

<img src="PDF Submission/Output_Images/group10_HW1_p4a.txt%20OUTPUT.png">

<br>

### 4.1.6 Solving Problem `4(a)` Graphically by Hand

<img src="PDF Submission/Output_Images/problem4a.1.jpg">

<br>

## 4.2 Task `b`

### 4.2.1 Additional Constraint: Labor Time

**C3**: Only 100 person weeks available, given it takes three weeks and
one week to create a `magazine` page and `tv` minute for advertisement,
respectively.  

![
personWeeks: (1 \\times tv) + (3 \\times magazine) \\leq 100
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0ApersonWeeks%3A%20%281%20%5Ctimes%20tv%29%20%2B%20%283%20%5Ctimes%20magazine%29%20%5Cleq%20100%0A "
personWeeks: (1 \times tv) + (3 \times magazine) \leq 100
")

<br>

### 4.2.2 Code

<img src="PDF Submission/Output_Images/codeProblem4b.png">

### 4.2.3 Output

<img src="PDF Submission/Output_Images/group10_HW1_p4b.txt%20OUTPUT.png">

<br>

## 4.3 Task `c`

### 4.3.1 Additional Constraint: Radio Advertising Medium

### 4.3.2 Decision Variables

`tv` = the number of minutes
![\\in \\mathbb{R}](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5Cin%20%5Cmathbb%7BR%7D "\in \mathbb{R}")
to air advertising on the *television* medium  
`magazine` = the number of pages
![\\in \\mathbb{I}](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5Cin%20%5Cmathbb%7BI%7D "\in \mathbb{I}")
to to advertise on the *magazine* medium `radio` = the number of minutes
![\\in \\mathbb{R}](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5Cin%20%5Cmathbb%7BR%7D "\in \mathbb{R}")
to air advertising on the *radio* medium

### 4.3.3 Objective Function

-   Maximize the total audience reach

![
Maximize \\ Z = (1.80\\times tv) + (1.00 \\times magazine) + (0.25 \\times radio)
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AMaximize%20%5C%20Z%20%3D%20%281.80%5Ctimes%20tv%29%20%2B%20%281.00%20%5Ctimes%20magazine%29%20%2B%20%280.25%20%5Ctimes%20radio%29%0A "
Maximize \ Z = (1.80\times tv) + (1.00 \times magazine) + (0.25 \times radio)
")

### 4.3.4 New Constraints

**C1**: Must not Exceed Budget of 1 Million dollars

![
budget: (20,000 \\times tv) + (10,000 \\times magazine) + (2,000 \\times radio) \\leq 1,000,000
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0Abudget%3A%20%2820%2C000%20%5Ctimes%20tv%29%20%2B%20%2810%2C000%20%5Ctimes%20magazine%29%20%2B%20%282%2C000%20%5Ctimes%20radio%29%20%5Cleq%201%2C000%2C000%0A "
budget: (20,000 \times tv) + (10,000 \times magazine) + (2,000 \times radio) \leq 1,000,000
")

**C2**: Must have at least 10 minutes of air time on the TV medium  

![
minTimeTV: tv \\geq 10
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AminTimeTV%3A%20tv%20%5Cgeq%2010%0A "
minTimeTV: tv \geq 10
")

**C3**: Only 100 person weeks available, given it takes three weeks and
one week to create a `tv` and `magazine` minute for advertisement,
respectively. It only takes one day for `radio`.  

![
personWeeks: (3 \\times tv) + (1 \\times magazine) + (\\frac{1}{7} \\times radio) \\leq 100
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0ApersonWeeks%3A%20%283%20%5Ctimes%20tv%29%20%2B%20%281%20%5Ctimes%20magazine%29%20%2B%20%28%5Cfrac%7B1%7D%7B7%7D%20%5Ctimes%20radio%29%20%5Cleq%20100%0A "
personWeeks: (3 \times tv) + (1 \times magazine) + (\frac{1}{7} \times radio) \leq 100
")

<br>

### 4.3.5 Code

<img src="PDF Submission/Output_Images/codeProblem4c.png">

### 4.3.6 Output

<img src="PDF Submission/Output_Images/group10_HW1_p4c.txt%20OUTPUT.png">

<br>

## 4.4 Task `d`

### 4.4.1 Additional Constraints: Miminum Magazine and Maximum Radio Requirements

**C4**: Must sign up for at least 2 magazine pages

![
minMagazines: magazine \\geq 2
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AminMagazines%3A%20magazine%20%5Cgeq%202%0A "
minMagazines: magazine \geq 2
")

**C5**: Must to exceed 120 minutes of radio

![
maxRadio: radio \\leq 120
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AmaxRadio%3A%20radio%20%5Cleq%20120%0A "
maxRadio: radio \leq 120
")

<!-- <br> -->
<!-- \newpage -->

### 4.4.2 Code

<img src="PDF Submission/Output_Images/codeProblem4d.png" style="width:90.0%" />

### 4.4.3 Output

<img src="PDF Submission/Output_Images/group10_HW1_p4d.txt%20OUTPUT.png">

<br>

# 5 Problem `5`

## 5.1 Base Mathematical Formulation and Code

-   *Each task shows a separate change to the base model. Therefore,
    each change should not accumulate.*

### 5.1.1 Mathematical Formulation

<img src="PDF Submission/Output_Images/mathProblem5.png">

### 5.1.2 Code for Model `.mod` and Input Data `.dat`

<img src="PDF Submission/Output_Images/codeProblem5base.png">

## 5.2 Task `a`

### 5.2.1 Changed Constraint for Total Hours

-   *Change the constraints so that total hours used by all products
    must equal the total hours available for each stage*

<br>

### 5.2.2 Code

<img src="PDF Submission/Output_Images/codeProblem5a.png">

### 5.2.3 Output

> There is no difference in the optimal solution because the range of
> Time before there is a change in optimal remains the same, and the
> hours available have not changed.  
> <img src="PDF Submission/Output_Images/outputProblem5a.png">

<br>

## 5.3 Task `b`

### 5.3.1 New Constraint for Max Weight

-   *Restrict the total weight of all products to be less than a new
    parameter, max_weight = 6,500*

![
totalWeight: \\sum\_{p \\ \\in \\ PROD} Make\_{p} \\leq max\\\_weight
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AtotalWeight%3A%20%5Csum_%7Bp%20%5C%20%5Cin%20%5C%20PROD%7D%20Make_%7Bp%7D%20%5Cleq%20max%5C_weight%0A "
totalWeight: \sum_{p \ \in \ PROD} Make_{p} \leq max\_weight
")

<br>

### 5.3.2 Code

<img src="PDF Submission/Output_Images/codeProblem5b.png">

### 5.3.3 Output

> The total number of tons has reduced from 7,000 to 6,500 per week
> <img src="PDF Submission/Output_Images/outputProblem5b.png">

<br>

## 5.4 Task `c`

### 5.4.1 Changed Objective Function

-   *Change the objective function to maximize total tons*

![
maximize \\ Total\\\_Tons = \\sum\_{p \\ \\in \\ PROD} Make\_{p}
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0Amaximize%20%5C%20Total%5C_Tons%20%3D%20%5Csum_%7Bp%20%5C%20%5Cin%20%5C%20PROD%7D%20Make_%7Bp%7D%0A "
maximize \ Total\_Tons = \sum_{p \ \in \ PROD} Make_{p}
")

<br>

### 5.4.2 Code

<img src="PDF Submission/Output_Images/codeProblem5c.png">

### 5.4.3 Output

> The data file does not make a diference in the optimal (assuming that
> is what the question is asking). Please note that the total number of
> tons produced are the same as in the `base` model; however, the
> allocation of tons have shifted among each of the products.
> <img src="PDF Submission/Output_Images/outputProblem5c.png">

<br>

## 5.5 Task `d`

### 5.5.1 New Constraint

-   *Minimum Share of Tons for each Product*

![
Share\\\_of\\\_Products: Make\_{j} \\geq share\_{j} \\times 
\\sum\_{k \\ \\in \\ PROD} Make\_{k}, \\ \\  \\forall \\ j \\ \\in \\ PROD
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AShare%5C_of%5C_Products%3A%20Make_%7Bj%7D%20%5Cgeq%20share_%7Bj%7D%20%5Ctimes%20%0A%5Csum_%7Bk%20%5C%20%5Cin%20%5C%20PROD%7D%20Make_%7Bk%7D%2C%20%5C%20%5C%20%20%5Cforall%20%5C%20j%20%5C%20%5Cin%20%5C%20PROD%0A "
Share\_of\_Products: Make_{j} \geq share_{j} \times 
\sum_{k \ \in \ PROD} Make_{k}, \ \  \forall \ j \ \in \ PROD
")

<!-- <br> -->
### 5.5.2 Code (Part I)

<img src="PDF Submission/Output_Images/codeProblem5d.png">

### 5.5.3 Output (Part I)

> Note that bands represent \~49.99%, coils: 40%, and plates: 10%
> <img src="PDF Submission/Output_Images/outputProblem5d.png">

<!-- <br> -->
### 5.5.4 Code (Part II)

<img src="PDF Submission/Output_Images/codeProblem5d1.png">

### 5.5.5 Output (Part II)

> Profit is zero because it is impossible for bands to reach 50% of the
> share. <img src="PDF Submission/Output_Images/outputProblem5d1.png">

<br>

## 5.6 Task `e`

### 5.6.1 Changing Input Data via `.dat` File

> Simply add the new item within the set called `finishing`, then add
> the its the associate values to the `rate` and `avail` parameters.
> <img src="PDF Submission/Output_Images/codeProblem5e.png">

### 5.6.2 Output

<img src="PDF Submission/Output_Images/outputProblem5e.png">

<br>

# 6 Problem `6`

## 6.1 Task `a` - `c`

### 6.1.1 Decision Variables

`bondA`: dollars
![\\in \\mathbb{R}](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5Cin%20%5Cmathbb%7BR%7D "\in \mathbb{R}")
to invest in bond A  
`bondB`: dollars
![\\in \\mathbb{R}](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5Cin%20%5Cmathbb%7BR%7D "\in \mathbb{R}")
to invest in bond B  
`bondC`: dollars
![\\in \\mathbb{R}](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5Cin%20%5Cmathbb%7BR%7D "\in \mathbb{R}")
to invest in bond C  
`bondD`: dollars
![\\in \\mathbb{R}](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5Cin%20%5Cmathbb%7BR%7D "\in \mathbb{R}")
to invest in bond D  
`bondE`: dollars
![\\in \\mathbb{R}](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%5Cin%20%5Cmathbb%7BR%7D "\in \mathbb{R}")
to invest in bond E

### 6.1.2 Objective Function

-   Maximize the Expected Earnings of the portfolio

![
Maximize \\ Z = (0.043 \\times bondA) + (0.027 \\times bondB) + (0.025 \\times bondC) + (0.022 \\times bondD) + (0.045 \\times bondE)
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AMaximize%20%5C%20Z%20%3D%20%280.043%20%5Ctimes%20bondA%29%20%2B%20%280.027%20%5Ctimes%20bondB%29%20%2B%20%280.025%20%5Ctimes%20bondC%29%20%2B%20%280.022%20%5Ctimes%20bondD%29%20%2B%20%280.045%20%5Ctimes%20bondE%29%0A "
Maximize \ Z = (0.043 \times bondA) + (0.027 \times bondB) + (0.025 \times bondC) + (0.022 \times bondD) + (0.045 \times bondE)
")

### 6.1.3 Constraints

**C1:** Budget to invest is $10 MM or less

![
budget: bondA + bondB + bondC + bondD + bondE \\leq 10
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0Abudget%3A%20bondA%20%2B%20bondB%20%2B%20bondC%20%2B%20bondD%20%2B%20bondE%20%5Cleq%2010%0A "
budget: bondA + bondB + bondC + bondD + bondE \leq 10
")

**C2:** At least $4 million must be invested in government and agency
bonds

![
govtAndAgency: bondB + bondC + bondD \\geq 4
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AgovtAndAgency%3A%20bondB%20%2B%20bondC%20%2B%20bondD%20%5Cgeq%204%0A "
govtAndAgency: bondB + bondC + bondD \geq 4
")

**C3:** Average Quality of the Portfolio must not exceed 1.4

![
avgQuality: (0.6 \\times bondA) + (0.6 \\times bondB) - (0.4 \\times bondC) 
- (0.4 \\times bondD) + (3.6 \\times bondE) \\leq 0
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AavgQuality%3A%20%280.6%20%5Ctimes%20bondA%29%20%2B%20%280.6%20%5Ctimes%20bondB%29%20-%20%280.4%20%5Ctimes%20bondC%29%20%0A-%20%280.4%20%5Ctimes%20bondD%29%20%2B%20%283.6%20%5Ctimes%20bondE%29%20%5Cleq%200%0A "
avgQuality: (0.6 \times bondA) + (0.6 \times bondB) - (0.4 \times bondC) 
- (0.4 \times bondD) + (3.6 \times bondE) \leq 0
")

**C4:** The Average Maturity must not Exceed Five Years

![
avgMaturity: (4 \\times bondA) + (10 \\times bondB) - (1 \\times bondC) 
- (2 \\times bondD) - (3 \\times bondE) \\leq 0
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AavgMaturity%3A%20%284%20%5Ctimes%20bondA%29%20%2B%20%2810%20%5Ctimes%20bondB%29%20-%20%281%20%5Ctimes%20bondC%29%20%0A-%20%282%20%5Ctimes%20bondD%29%20-%20%283%20%5Ctimes%20bondE%29%20%5Cleq%200%0A "
avgMaturity: (4 \times bondA) + (10 \times bondB) - (1 \times bondC) 
- (2 \times bondD) - (3 \times bondE) \leq 0
")

**C5:** Only select Bonds A and D (Don’t select B, C, or E)

![
onlyAandB: bondB + bondC + bondE = 0;
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0AonlyAandB%3A%20bondB%20%2B%20bondC%20%2B%20bondE%20%3D%200%3B%0A "
onlyAandB: bondB + bondC + bondE = 0;
")

**C6:** Municipal Bonds must be less than or equal to $3 MM

![
municipal: bondA \\leq 3;
](https://latex.codecogs.com/png.image?%5Cdpi%7B110%7D&space;%5Cbg_white&space;%0Amunicipal%3A%20bondA%20%5Cleq%203%3B%0A "
municipal: bondA \leq 3;
")

<!-- <br> -->

### 6.1.4 Code

<img src="PDF Submission/Output_Images/codeProblem6.png" style="width:90.0%" />

### 6.1.5 Output

<img src="PDF Submission/Output_Images/outputProblem6.png">

## 6.2 Task `d`:

You may not borrow more than 2.83%, since that is the expected  
yield to maturity (30% of bondA \* 4.3%) + (70% of bondD \* 2.2%)

## 6.3 Task `e`:

If you borrowed at a rate greater than the expected YTM, then the  
venture would not be profitable.
