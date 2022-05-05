# Homework 3 - Integer Programming
# Adv. Analytics and Metaheuristics
# Daniel Carpenter and Iker Zarandona
# March 2022
# Problem 1

reset;                  # Reset globals
options solver cplex;   # Using cplex for simplex alg

# SETS ============================================================
    set GENERATORS; # Set of generators to use
    set PERIODS;    # Periods in the day
    
# PARAMETERS =======================================================
    param S {GENERATORS}   >= 0; # Fixed cost to start
    param F {GENERATORS}   >= 0; # Fixed cost to operate
    param C {GENERATORS}   >= 0; # Variable cost per megawatt
    param U {GENERATORS}   >= 0; # Upper bound on megawatts in a day
    param M {GENERATORS}   >= 0; # Map decision variables
    param demand {PERIODS} >= 0; # Megawatts required per period

# DECISION VARIABLES ===============================================
    var watts {GENERATORS, PERIODS} >= 0 integer; # Megawatts to use
    var x {GENERATORS, PERIODS} binary; # Map to watts for fixed daily costs
    var y {GENERATORS} binary; # Map to watts for fixed daily costs
    
# OBJECTIVE FUNCTION ===============================================
  minimize cost: 
      (sum{i in GENERATORS} (sum{p in PERIODS} watts[i,p])*C[i]) 
    + (sum{i in GENERATORS} F[i]*sum{p in PERIODS}x[i,p]) 
    + (sum{i in GENERATORS} S[i]*y[i]);

# CONSTRAINTS ======================================================

    # C1: For each period, meet the demanded megawatta
    subject to requiredWatts {p in PERIODS}:
        (sum{i in GENERATORS} watts[i,p]) = demand[p];

    # C2: For each generator, don’t surpass the allowable megawatts
    subject to upperBound {i in GENERATORS}:
        (sum{p in PERIODS} watts[i,p]) <= U[i];

    # C3: For each generator, map decision variables together to account for the fixed costs in a given day Si
    subject to mapVars {i in GENERATORS}:
        (sum{p in PERIODS} watts[i,p]) <= M[i] * y[i];
    
    # C4: For each generator and period, map decision variables y and watts together to account for the fixed costs in a per period p
    subject to mapVars2 {i in GENERATORS, p in PERIODS}:
        watts[i,p] <= M[i] * x[i,p];

# CONTROLS ==========================================================
    data group23_HW3_p1.dat;
    solve;
    
    print;
    print "Which generators are used?";
    display y;
    
    print "Which periods were the generators used?";
    display x;

    print "Optimal Amount of Megawatts for each generator and period:";
    display watts;
