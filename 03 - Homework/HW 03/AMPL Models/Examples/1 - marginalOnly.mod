#DSA/ISE 5113 Integer Programming
#Example IP: Marginal Cost only example

reset;

# OPTIONS ---------------------------------------------------------
option solver cplex;

# GLOBAL PARAMETERS -----------------------------------------------
param theDemand := 17999; # The demanded amount of products
param M := 10000000;      # Large scaler that is not inf


# WII - Basic Marginal Cost Model ===============================

    # PARAMETERS --------------------------------------------------
    param mcWII    := 4.95;   # Marginal cost compnent of WII
    param availWII := 18000;  # Amount of WII that is available 

    # DECISION VARIABLES ------------------------------------------
    var WII >= 0;   #amt of product WOW to produce
    
    # CONSTRAINTS -------------------------------------------------
    s.t. upperBoundWII: WII <= availWII;

# END OF WII - Basic Marginal Cost Model =========================

        

# OBJECTIVE -----------------------------------------------------
minimize cost: mcWII*WII;

# SOLVE THE MODE ==================================================
    
    # Constraint to make it produce  at least the demanded amount
    s.t. meetTheDemand: WII >= theDemand;


    solve;
    display WII; # Amount of WII Used