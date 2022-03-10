# Daniel Carpenter
# Exam 1
# Problem 1

reset;                  # Reset globals
options solver cplex;   # Using cplex for simplex alg

# SETS ============================================================
    set P circular; # The three types of products, High-Gloss, Semi-Gloss, and Flat

# PARAMETERS =======================================================
    param  rawA   {P} >= 0; # Raw ingredient A needed to produce product p ∈ P;
    param  rawB   {P} >= 0; # Raw ingredient B needed to produce product p ∈ P;
    param  demand {P} >= 0; # Min demand to be met for product p ∈ P;
    param  profit {P} >= 0; # Associated profit for product p ∈ P;

# DECISION VARIABLES ===============================================
    var amtToProduce {P} >=0 integer; # amount of product p ∈ P to produce

# OBJECTIVE FUNCTION ===============================================
    maximize theProfit: sum{p in P} amtToProduce[p] * profit[p];
    
# CONSTRAINTS ======================================================
    
    # C1: Meet the minimum demand for each product
    s.t. meetMinDemand{p in P}: amtToProduce[p] >= demand[p];
    
    # C2/3: Cannot exceed the supply of Raw Material A or B
    s.t. rawSupplyA: sum{p in P} amtToProduce[p] * rawA[p] <= 4000;
    s.t. rawSupplyB: sum{p in P} amtToProduce[p] * rawB[p] <= 6000;

    # C4: Ratio of 3:2 for High and Semi Gloss, respectively
    s.t. highToSemiRatio {p in P}: 1.5 * amtToProduce[last(P)] == amtToProduce[first(P)];

# CONTROLS ==========================================================
    data problem1.dat;
    solve;

    print;
    print "For each product, product the following amounts:";
    display amtToProduce;
