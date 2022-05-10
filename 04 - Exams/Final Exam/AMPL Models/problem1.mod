# Daniel Carpenter
# Final Exam
# Problem 1

reset;                  # Reset globals
options solver cplex;   # Using cplex for simplex alg

# SETS ============================================================
set NewBuildTypes; # Set of new build types

# PARAMETERS =======================================================
param budget           >= 0; # federal budget 
param maxBuildingDemod >= 0; # max buildings can be demo'd
param demoCost         >= 0; # Cost of each demolition
param freedUpSpace     >= 0; # Freed up space from demolition

param newBuildSpace    {NewBuildTypes} >= 0; # new build acreage
param newBuildTax      {NewBuildTypes} >= 0; # n.b. tax generation
param newBuildCost     {NewBuildTypes} >= 0; # n.b. cost
param newBuildPercShare{NewBuildTypes} >= 0; # n.b. min % share

# DECISION VARIABLES ===============================================
var numOldBuildsDemod                >= 0; # Num old builds to demo
var numNewBuilds      {NewBuildTypes} >= 0; # Num new builds to create

# OBJECTIVE FUNCTION ===============================================
maximize taxRevenue: sum{b in NewBuildTypes}( numNewBuilds[b] * newBuildTax[b] )

# CONSTRAINTS ======================================================

# C1  Spend less than or equal to the federal budget
s.t. meetTheBudget: 
    sum{b in NewBuildTypes} ( 
        (numNewBuilds[b] * newBuildCost[b]) + (numOldBuildsDemod * demoCost) 
    ) <= budget ;

# C2 Can only produce new builds using the demolished buildings land
s.t. useAvailLand: 
    sum{b in NewBuildTypes}( numNewBuilds[b] * newBuildSpace[b] )
    <= numOldBuildsDemod * freedUpSpace ;

# C3 Can only clear a certain amount of old buildings
s.t. maxBuildingsCleared: numOldBuildsDemod <= maxBuildingDemod ;

# C4 For each new build type (b ∈ NewBuildTypes), 
#    the percentage share of the new build type must meet the minimum required
s.t. share {b in Businesses}: 
    numNewBuilds[b] >= newBuildPercShare[b] * sum{b in NewBuildTypes}( numNewBuilds[b] ) ;

# CONTROLS ==========================================================
    data problem1.dat; # retreive data file with sets/param. values
    solve;

    print;
    print "Tax Revenue generated, num. new builds, num. old builds demolished:";
    display taxRevenue, numOldBuildsDemod, numNewBuilds;
