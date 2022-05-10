# Daniel Carpenter
# Final Exam
# Problem 2 (Checking Nodes)

# README:
# I have left it in the state when solving for the initial node
# So you can see the solution 

reset;
option solver cplex; # Solver

var x >= 0; # Not integer because this is used to check the optimal when fixing a var
var y >= 0; # ""

# Original problem:
maximize theSolution: 2.5*x + 6*y;
	s.t. first:  3*x + 5*y <= 26;
	s.t. second:   x       >= 4;

# Used to check the BnB nodes - comment for optimal
s.t. checkNode: x = 4;

# Solve and display
solve;
display theSolution, x,y;

# Note Optimal Answers Hard Coded ----------------
# theSolution = 24.5
# x = 5
# y = 2