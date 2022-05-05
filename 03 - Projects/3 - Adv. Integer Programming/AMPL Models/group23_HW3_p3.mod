# Homework 3 - Integer Programming
# Adv. Analytics and Metaheuristics
# Daniel Carpenter and Iker Zarandona
# March 2022
# Problem 3

reset;                  # Reset globals
options solver cplex;   # Using cplex for simplex alg

# GLOBAL PARAMETERS ===============================================
param theDemand := 55000;    # The demanded amount of products
param M         := 10000000; # Large scaler that is not inf

# WII - Basic Marginal Cost Model ===============================

    # PARAMETERS --------------------------------------------------
    param mcWII    := 4.95;   # Marginal cost compnent of WII
    param availWII := 18000;  # Amount of WII that is available 

    # DECISION VARIABLES ------------------------------------------
    var WII >= 0;   #amt of product WOW to produce
    
    # CONSTRAINTS -------------------------------------------------
    s.t. upperBoundWII: WII <= availWII;

# END OF WII - Basic Marginal Cost Model =========================


# WRS - Marginal Cost + Fixed Cost Model ==========================

    # PARAMETERS --------------------------------------------------
    param mcWRS    := 2.30;  # Marginal cost compnent of WRS
    param fixWRS   := 20000; # Fixed Cost component of WRS
    param availWRS := 14000; # Amount of WRS that is available 

    # DECISION VARIABLES ------------------------------------------
    var WRS >= 0;    # amt of product WRS to produce
    var yWRS1 binary; # Binary used for fixed cost if used
    
    # CONSTRAINTS -------------------------------------------------
    s.t. map_yWRS1: WRS <= availWRS * yWRS1; # Upper bound and map

# END OF WRS - Basic Marginal Cost Model =========================


# WE - Basic Marginal Cost Model ===============================

    # PARAMETERS --------------------------------------------------
    param mcWE1   := 3.95;  # If buy from WRS, m. cost for WE
    param mcWE2   := 4.10;  # Else m. cost for WE
    param availWE := 7000;  # Amount of WE that is available 

    # DECISION VARIABLES ------------------------------------------
        # WE decision vars
        var WE1 >= 0;   # Decision variable associated with $3.95 marginal cost
        var WE2 >= 0;   # Decision variable associated with $4.10 marginal cost
        var WE  >= 0;   # Decision variable for final output 
        
        # Binary Vars to see what product is selected
        var yWRS  binary;   # If WRS is selected
        var yWII  binary;   # If WII is selected
        var yWE1  binary;   # If WE  is selected
        var yWE2  binary;   # If WE  is selected
        var z     binary;   # Octivates only one constraint

    # CONSTRAINTS -------------------------------------------------
        # Map binary variables to show selection of products
        s.t. mapWE1: WE1  <= M * yWE1; # Map the W vars to the y binary
        s.t. mapWE2: WE2  <= M * yWE2; # ""
        s.t. mapWRS: WRS  <= M * yWRS; # ""
        s.t. mapWII: WII  <= M * yWII; # ""

        # Logical Constraints
            # If buy from WRS, then can do WE1. (Use of Mz to choose one constraint)
            s.t. ifWRS_ThenWE1:    yWRS <= yWE1 + M*z;      
            
            # If WE2, cannot do WII. (Use of Mz to choose one constraint)
            s.t. ifWRS_thenNotWII: yWE2 +  yWII <= 1 + M*(1-z); 

            # If WE1, then cannot do WE2, Must choose one
            s.t. only1WE:   yWE1 + yWE2 <= 1;                  
            
            # Finally, set WE to the sum of WE1 and WE2 for the final output
            s.t. setWE: WE == WE1 + WE2;

        s.t. upperBoundWE: WE <= availWE; # Meet the upper bound limit

# END OF WE - Basic Marginal Cost Model =========================


# WU - Marginal Cost + Fixed Cost Model ===============================

    # PARAMETERS --------------------------------------------------
    param mcWU      := 4.25;  # Marginal cost compnent of WU
    param availWU   := 22000; # Amount of WU that is available 
    param minBuyAmt := 15000; # Must buy at least 15k 

    # DECISION VARIABLES ------------------------------------------
    var WU >= 0;    # amt of product WU to produce
    var yWU binary; # Binary used for fixed cost if used
    
    # CONSTRAINTS -------------------------------------------------
    s.t. buyAtLeastMin: WU <= availWU   * yWU;    # Buy at least min amount
    s.t. map_yWU:       WU >= minBuyAmt * yWU;  # Under the upper bound

# END OF WU - Basic Marginal Cost Model =========================


# WOW - Piecewise Linear Cost Model ===============================

    # PARAMETERS -------------------------------------------------

    #assume the linear costs for decision variable WOW are as follows
    #cost = 9.50 for     0 <=WOW < 3000
    #cost = 4.90 for  3000 <=WOW < 9000
    #cost = 2.75 for  9000 <=WOW < INFINITY

    param mcWOW1 := 9.50; param mcWOW1Upper := 3000;  # 3000 upper bound
    param mcWOW2 := 4.90; param mcWOW2Upper := 6000;  # 3000 + 6000 = 9000 upper bound
    param mcWOW3 := 2.75; param mcWOW3Upper := 25000; # Cannot exceed 25000 due to supply
    # DECISION VARIABLES ------------------------------------------
    var WOW >= 0;   #amt of product WOW to produce

    var d1WOW >=0;  # piecewise component 1 of var WOW
    var d2WOW >=0;  # piecewise component 2 of var WOW 
    var d3WOW >=0;  # piecewise component 3 of var WOW

    var y1WOW binary; #to model piecewise cost for var WOW
    var y2WOW binary; #to model piecewise cost for var WOW


    # CONSTRAINTS ----------------------------------------------------

        #connect WOW with d1WOW, d2WOW, and d3WOW;
        s.t. X_WOW: WOW = d1WOW + d2WOW + d3WOW;
        
        #ensure that the piece wise costs are used correctly,
        #i.e., you have to use all of d1WOW before you use d2WOW,...
        # First Piece (Between 0 and Upper)
        s.t. piece1a: mcWOW1Upper*y1WOW <= d1WOW;
        s.t. piece1b: d1WOW <= mcWOW1Upper;
        
        # Second Piece (Between last piece and Upper)
        s.t. piece2a: mcWOW2Upper*y2WOW <= d2WOW;
        s.t. piece2b: d2WOW <= mcWOW2Upper*y1WOW;
        
        # Third Piece (Between last piece and Upper)
        s.t. piece3: d3WOW <= mcWOW3Upper*y2WOW;
        
        # Cannot go over upper
        s.t. upperBoundWOW: WOW <= mcWOW3Upper;

# END OF WOW - Piecewise Linear Cost Model ==========================

# Last Constraint: Must meet the demand
s.t. meetTheDemand: WII + WRS + WE + WU + WOW >= theDemand;


# ===================================================================
# OBJECTIVE FUNCTION 
# ===================================================================

minimize cost:    mcWII*WII                 # WII: Variable cost only
                + fixWRS*yWRS1 + mcWRS*WRS  # WRS: Fixed plus variable
                + mcWE1*WE1    + mcWE2*WE2  # WE: Continguint mc based on scenario
                + mcWU*WU                   # WU: Restricted range to over 15k
                + mcWOW1*d1WOW + mcWOW2*d2WOW + mcWOW3*d3WOW # WOW: Piecewise
                ;


# CONTROLS ==========================================================

solve;

print;
printf  "Demand\t| WII\t| WRS\t| WE\t|  WU\t|  WOW\t| Total Cost";
printf "\n%s\t %s\t %s\t %s\t %s\t %s\t %f", theDemand, WII, WRS, WE, WU, WOW, cost;
print;
        

