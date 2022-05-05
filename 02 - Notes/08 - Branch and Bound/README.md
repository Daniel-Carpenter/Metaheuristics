# Branch and Bound Overview

Key Question | Answer
-------------|--------
Explain `LP relaxation` for IP problems | Solve as LP and relax the integer requirement. Then round the values? If rounded, not a good solution.
Explain `complete enumeration` for IP problems | systematically consider all possible values of the decision variables (not good - solve with valid inequalities and branch n bound). This is `explicit exhaustive enumeration`
Use standard terminology to discuss the `branch-and-bound algorithm` | Formulate the IP with a tight LP relaxation, and Generate an incumbent solution even before beginning the branch and bound process if possible. Note still `implicitly` considering all feasible solutions
Use `branching on fractional solutions to create sub-problems` | Create sub problems (2 nodes) to find the optimal integer solution
Evaluate `incumbent solutions` and `LP relaxation solutions` to determine bounds in a `branch-and-bound tree` | If a new solution is better than the incumbent, the new solution is the potential optimal
Recognize the three conditions when a branch-and-bound node should be `fathomed` | LP[i] is integer feasible, LP[i] is infeasible, and LP[i] is feasible, but the relaxation objective is greater than the incumbent objective
Use `valid inequalities` to improve an IP formulation | A valid inequality eliminates known non-optimal solutions. For example if the treasure chest is certainly not inside a dense forest, why would you check through the forest at all? A valid inequality would protect from searching in the forest. 
