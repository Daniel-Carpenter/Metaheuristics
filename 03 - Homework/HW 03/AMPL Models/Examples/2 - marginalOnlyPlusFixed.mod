#DSA/ISE 5113 Integer Programming
#Example IP: Marginal + Fixed Cost Example

reset;

# OPTIONS ---------------------------------------------------------
option solver cplex;

# GLOBAL PARAMETERS -----------------------------------------------
param theDemand := 17999; # The demanded amount of products
param M := 10000000;      # Large scaler that is not inf


# WRS - Marginal Cost + Fixed Cost Model ===============================

    # PARAMETERS --------------------------------------------------
    param mcWRS    := 2.30;  # Marginal cost compnent of WRS
    param fixWRS   := 20000; # Fixed Cost component of WRS
    param availWRS := 14000; # Amount of WRS that is available 

    # DECISION VARIABLES ------------------------------------------
    var WRS >= 0;   #amt of product WRS to produce
    
    # CONSTRAINTS -------------------------------------------------
    s.t. upperBoundWRS: WRS <= availWRS;

# END OF WRS - Basic Marginal Cost Model =========================

        

# OBJECTIVE -----------------------------------------------------
minimize cost: mcWRS*WRS;

# SOLVE THE MODE ==================================================
    
    # Constraint to make it produce  at least the demanded amount
    s.t. meetTheDemand: WRS >= theDemand;


    solve;
    display WRS; # Amount of WRS Used