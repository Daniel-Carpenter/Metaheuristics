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
var numOldBuildsDemod                 >= 0 integer; # Num old builds to demo
var numNewBuilds      {NewBuildTypes} >= 0 integer; # Num new builds to create

# Variables to hold total cost of new builds over all types
var newBuildTotalCost = sum{b in NewBuildTypes} ( (numNewBuilds[b] * newBuildCost[b]) ) ;

# Variables to hold total cost of old demolitions
var oldDemoTotalCost = (numOldBuildsDemod * demoCost) ;

# Variable to hold the sum of all new build types over all New build types
var sumOfNewBuilds =  sum{b in NewBuildTypes}( numNewBuilds[b] );

# OBJECTIVE FUNCTION ===============================================
maximize taxRevenue: sum{b in NewBuildTypes}( numNewBuilds[b] * newBuildTax[b] );

# CONSTRAINTS ======================================================

# C1  Spend less than or equal to the federal budget
s.t. meetTheBudget: 
    newBuildTotalCost + oldDemoTotalCost <= budget ;

# C2 Can only produce new builds using the demolished buildings land
s.t. useAvailLand: 
    sum{b in NewBuildTypes}( numNewBuilds[b] * newBuildSpace[b] )
    <= numOldBuildsDemod * freedUpSpace ;

# C3 Can only clear a certain amount of old buildings
s.t. maxBuildingsCleared: numOldBuildsDemod <= maxBuildingDemod ;

# C4 For each new build type (b ∈ NewBuildTypes), 
#    the percentage share of the new build type must meet the minimum required
s.t. share {b in NewBuildTypes}: 
    numNewBuilds[b] >= newBuildPercShare[b] * sumOfNewBuilds ;

# CONTROLS ==========================================================
    data problem1.dat; # retreive data file with sets/param. values
    solve;

    print;

    print "Number of old buildings to demolish and cost (dollars):";
    display numOldBuildsDemod, oldDemoTotalCost ;
    
    print "Number of new buildings produced and cost (dollars):";
    display numNewBuilds , newBuildTotalCost ;
    
    print "Total Budget Used (dollars):";
    display newBuildTotalCost + oldDemoTotalCost ;
    
    print "Part 3: Max Tax Revenue generated (dollars):";
    display taxRevenue ;
    