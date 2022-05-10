
# Problem 2 Final Exam self check

reset;

# Set up options and the solver
option solver cplex;


var x >= 0 integer;
var y >= 0 integer;

maximize theSolution: 2.5*x + 6*y;

s.t. first:  3*x + 5*y <= 26;
s.t. second:   x       >= 4;


solve;
display theSolution, x,y;

# Answers ----------------

# theSolution = 24.5
# x = 5
# y = 2