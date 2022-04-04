# Traveler Problem - (*Bridge and torch problem*)

## Problem Setup: 

* `Four` people come to a river in the night. 
* There is a narrow bridge, but it `can only hold two people at a time`. 
* They have one torch and, because it's night, the `torch has to be used when crossing the bridge`. 
* Person A can cross the bridge in 1 minute, B in 2 minutes, C in 5 minutes, and D in 10 minutes. 
* When two people cross the bridge together, they `must move at the slower person's pace`. 
* The question is, can they all get across the bridge if the torch lasts only 18 minutes?

## Problem Solution:
* [Solution explanation here](https://en.wikipedia.org/wiki/Bridge_and_torch_problem)
* Originally, I moved A over the bridge every time, but that totaled 19 minutes (infeasible). I then realized that moving C and D together in the second crossing would minimize total time. See below with a feasible solution:

    <img src = 'Solution 1.1.png' width = 600> <br>
    <img src = 'Solution 1.2.png' width = 600> <br>