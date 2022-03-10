# Galaxy Industries Linear Programming Problem
reset;

# Set up options and the solver
option solver cplex;

# PARAMETERS -----------------------------------------------------
# param M := 100000000; # Big M scaler

# DECISION VARIABLES ---------------------------------------------
var spaceRays >= 0; # Number of Space Ray Products
var zappers >= 0;   # Number of Zapper Products
# var z binary; # Determines whether or not constraints are active or not.

# OBJECTIVE -----------------------------------------------------
maximize profit: (8*spaceRays) + (5*zappers);

# CONSTRAINTS -----------------------------------------------------
s.t. plastic:    (2*spaceRays) + (1*zappers) <= 1000;
s.t. labor:      (3*spaceRays) + (4*zappers) <= 2400;
s.t. production:   (spaceRays) +   (zappers) <= 700;
s.t. management:   (spaceRays) -   (zappers) <= 350;
# s.t. spaceRays + zappers >= 400 + M*z;
# s.t. zappers >= 70 * (spaceRays + zappers) + M*z;

# SOLVE ---------------------------------------------------------

## Solve the model
solve;

print;
print 'Produce this amount of Space Rays and Zappers';
display spaceRays,zappers;
