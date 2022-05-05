#DSA/ISE 5113 Integer Programming
#Example IP: Cpntinguient Marginal Cost

reset;

# OPTIONS ---------------------------------------------------------
option solver cplex;

# GLOBAL PARAMETERS -----------------------------------------------
param theDemand := 7000;    # The demanded amount of products
param M         := 10000000; # Large scaler that is not inf

var WRS  >= 0;   # amt of product WE to produce
var WII  >= 0;   # amt of product WE to produce
s.t. upperBoundWRS: WRS <= 14000; # Meet the upper bound limit
s.t. upperBoundWII: WII <= 18000; # Meet the upper bound limit
# -------------------------------------------------------------------



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

        
        

# OBJECTIVE -----------------------------------------------------
minimize cost: mcWE1*WE1 + mcWE2*WE2  # WE: Continguint mc based on scenario
               + 1000*WRS + 1000*WII;

# SOLVE THE MODE ==================================================
    
    # Constraint to make it produce  at least the demanded amount
    s.t. meetTheDemand: WE1 + WE2 + WRS + WII>= theDemand;

    solve;
    display WE; 
    display WE1, yWE1; 
    display WE2, yWE2; 
    display WRS, yWRS;
    display WII, yWII;