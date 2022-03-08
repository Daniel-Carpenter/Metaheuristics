#DSA/ISE 5113 Integer Programming
#Example IP: Marginal, with restricted range (must be greater than k)

reset;

# OPTIONS ---------------------------------------------------------
option solver cplex;

# GLOBAL PARAMETERS -----------------------------------------------
param theDemand := 5000; # The demanded amount of products
param M := 10000000;      # Large scaler that is not inf


# WU - Marginal Cost + Fixed Cost Model ===============================

    # PARAMETERS --------------------------------------------------
    param mcWU      := 4.25;  # Marginal cost compnent of WU
    param availWU   := 22000; # Amount of WU that is available 
    param minBuyAmt := 15000; # Must buy at least 15k 

    # DECISION VARIABLES ------------------------------------------
    var WU >= 0;     # amt of product WU to produce
    var yWU binary; # Binary used for fixed cost if used
    
    # CONSTRAINTS -------------------------------------------------
    s.t. buyAtLeastMin: WU <= availWU*yWU;    # Buy at least min amount
    s.t. map_yWU:       WU >= minBuyAmt*yWU;  # Under the upper bound

# END OF WU - Basic Marginal Cost Model =========================

        

# OBJECTIVE -----------------------------------------------------
minimize cost: + mcWU*WU; # WU: Restricted range to over 15k

# SOLVE THE MODE ==================================================
    
    # Constraint to make it produce  at least the demanded amount
    s.t. meetTheDemand: WU >= theDemand;


    solve;
    display WU; # Amount of WU Used