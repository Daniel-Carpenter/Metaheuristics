
reset;

# Set up options and the solver
option solver cplex;
option cplex_options 'sensitivity';


# Parameters
param budget >= 0;
param tvTime >= 0;

# DECISION VARIABLES
var tvMinsUsed >= 0;
var magsUsed   >= 0;


# Objective
maximize reach: (tvMinsUsed * 1800000) + (magsUsed * 1000000);

# Constraints

# Meet the budget
s.t. theBudget: (tvMinsUsed * 20000) + (magsUsed * 10000) <= budget;

# Must have certain amount of tv time
s.t. minTimeOfTV : tvMinsUsed >= tvTime;


# Get data and solve
data HW1_1.dat;

solve;

display reach, tvMinsUsed, magsUsed;