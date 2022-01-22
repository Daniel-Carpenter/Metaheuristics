# Mathematical Optimization Overview

## Resources
* [Truth Table Calculator Tool](https://web.stanford.edu/class/cs103/tools/truth-table-tool/)

## Unit Objectives
1. Analyze logic problems using a mathematical model
2. Identify a variety of optimization problem types
3. Distinguish linear, integer, and non-linear programming problems
4. Differentiate between precise modeling and precise solutions as a problem-solving approach


---

<br>

## 1. `Logic Problems using a Mathematical Model`
* [Truth Table Calculator Tool](https://web.stanford.edu/class/cs103/tools/truth-table-tool/)

---

<br>

## 2. `Optimization Problem Types`

* Can have hard and soft constraints. Hard is a must, but soft is nice to have.

### Comparing Infeasible Models
> Model that satisfies that most constraints

* Maybe there is not a feasible solution space, but we want to know which model satisfies the most contraints
* Can compare with this type of modeling

---

<br>

## 3. `Linear, Integer, and Non-Linear Programming Problems`

### 3.1 - `Linear Programming`
* Optimal solution only exists at `corner points` (intersection of contraints), so very few possible optimal solutions
* <img src = "Images/lp.png" width = 250> <br>

<br>

### 3.2 - `Integer Programming`
* Must be an integer as solution
* Optimal may not be a corner point anymore (but in the feasible space), so calculating is *not efficient compared to LP*.
* <img src = "Images/int.png" width = 250> <br>
* <img src = "Images/intGraph.png" width = 250> <br>

<br>

### 3.3 - `Non-Linear Programming`
> Optimal does not have to exist on a corner point

#### **Could be Non-Linear in `Constraints`**
* <img src = "Images/nonLinCons.png" width = 250> <br>

#### **Could be Non-Linear in `Objective Function`**

#### **Optimal Could be Inside Feasible Space**
* Not on Corner Point
* <img src = "Images/nonLinInside.png" width = 250> <br>

<br>

---

## 4. Problem-Solving Approaches: Precise *Modeling* vs. Precise *Solutions*
> Generally, `Approximate *solutions* to a precise *model* are better` than exact solutions to an approximate model.

<br>

### 4.1 - Overview of Precise Modeling vs. Precise Solutions

<img src = "Images/preciseOverview.png" width = 400> <br>

---

### 4.2 - Model `Setup` for Below Descriptions
* Objective Function for model setup below  
* <img src = "Images/setup.png" width = 400> <br>


### 4.3 - `Precise Modeling` resulting in *Approximate Solution* **`(BEST CASE)`**
* Precise `Modeling` yeilds an approximate solution, but it resembles to real world solution best  
* Solution will be *close to the actual solution*
* Takes *much less time to solve*
* <img src = "Images/realSol.png" width = 400> <br>

### 4.4 - `Precise Solutions` via *Approximate Model*
* Approximate `Modeling` yields an precise solution, but it ***does not*** resemble real world solutions best  
* Example being Linear Regression. However, we could use linear algebra to solve this very quickly.
* <img src = "Images/approxSol.png" width = 400> <br>