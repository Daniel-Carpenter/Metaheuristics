# Daniel Carpenter
# Exam 1
# Problem 2

reset;

# Set up options and the solver
option solver cplex;

# PARAMETERS -----------------------------------------------------
param M := 100000000; # Big M scaler

# DECISION VARIABLES ---------------------------------------------
var spaceRays >= 0; # Number of Space Ray Products
var zappers >= 0;   # Number of Zapper Products
var totalProduction >= 0; # Zappers + Spacerays
var z binary; # Determines whether or not constraints are active or not.

# OBJECTIVE -----------------------------------------------------
maximize profit: (8*spaceRays) + (5*zappers);

# CONSTRAINTS -----------------------------------------------------
s.t. plastic:    (2*spaceRays) + (1*zappers) <= 1000;
s.t. labor:      (3*spaceRays) + (4*zappers) <= 2400;
s.t. production:   (spaceRays) +   (zappers) <= 700;
s.t. management:   (spaceRays) -   (zappers) <= 350;


# New Constraints

    ## Set totalProduction = Zappers + Spacerays
    s.t. setTotalProd: totalProduction == spaceRays + zappers;

    ## If total Production is >= 400, 
    s.t. isGreaterThan400: totalProduction  >= 400                   + M*z;     
    s.t. zappersAre70Perc: zappers          >= 0.70*totalProduction  + M*z;     

    ## If total Production is <= 400, then no zappers
    s.t. isLessThan400:    totalProduction  <= 400                   + M*(1 - z);
    s.t. noZappers:        spaceRays        >= totalProduction       - M*(1 - z);

# SOLVE ---------------------------------------------------------

## Solve the model
solve;

print;
print 'Produce this amount of Space Rays and Zappers';
display spaceRays,zappers, totalProduction;

print 'If Zappers used, then must be 70% of total prod:';
display zappers / totalProduction;
