#DSA/ISE 5113 Integer Programming
#Example IP: Piecewise Linear Cost example

reset;

# OPTIONS ---------------------------------------------------------
option solver cplex;

# GLOBAL PARAMETERS -----------------------------------------------
param theDemand := 20000; # The demanded amount of products
param M := 10000000;      # Large scaler that is not inf


# WOW - Piecewise Linear Cost Model ===============================

    # PARAMETERS -------------------------------------------------

    #assume the linear costs for decision variable WOW are as follows
    #cost = 9.50 for     0 <=WOW < 3000
    #cost = 4.90 for  3000 <=WOW < 9000
    #cost = 2.75 for  9000 <=WOW < INFINITY

    param mcWOW1 := 9.50; param mcWOW1Upper := 3000;  # 3000 upper bound
    param mcWOW2 := 4.90; param mcWOW2Upper := 6000;  # 3000 + 6000 = 9000 upper bound
    param mcWOW3 := 2.75; param mcWOW3Upper := M;     # M = None 

    # DECISION VARIABLES ------------------------------------------
    var WOW >= 0;   #amt of product WOW to produce

    var d1WOW >=0;  # piecewise component 1 of var WOW
    var d2WOW >=0;  # piecewise component 2 of var WOW 
    var d3WOW >=0;  # piecewise component 3 of var WOW

    var y1WOW binary; #to model piecewise cost for var WOW
    var y2WOW binary; #to model piecewise cost for var WOW

    # OBJECTIVE -----------------------------------------------------
    minimize cost: mcWOW1*d1WOW + mcWOW2*d2WOW + mcWOW3*d3WOW;

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

# END OF WOW - Piecewise Linear Cost Model =======================

        

# SOLVE THE MODE ==================================================
    
    # Constraint to make it produce  at least the demanded amount
    s.t. meetTheDemand: WOW >= theDemand;


    solve;
    display WOW;#,   # Amount of WOW used for wigits
            # d1WOW, # Amount used within each bin
            # d2WOW, # Amount used within each bin
            # d3WOW, # Amount used within each bin
            # y1WOW, # is the bin used? 
            # y2WOW; # is the bin used?
