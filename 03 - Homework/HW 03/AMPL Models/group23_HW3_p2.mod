# Homework 3 - Integer Programming
# Adv. Analytics and Metaheuristics
# Daniel Carpenter and Iker Zarandona
# March 2022
# Problem X

reset;                  # Reset globals
options solver cplex;   # Using cplex for simplex alg

# SETS ============================================================
    set PRODUCTS;     # The 5 products
    set SILOS;        # The 8 silos for storage

# PARAMETERS =======================================================
    param cost     {PRODUCTS, SILOS}; # Cost of storing product in silo
    param supply   {PRODUCTS};        # Supply of products
    param capacity {SILOS};           # Capacity of the silos
    param M        {SILOS};           # Map decision variables together 

# DECISION VARIABLES ===============================================
    var tonsOfProduct {PRODUCTS, SILOS} >= 0;  # Amount of each product p to store in silo s
    var isStored      {PRODUCTS, SILOS} binary; # If a product is stored in a silo or not

# OBJECTIVE FUNCTION ===============================================

# CONSTRAINTS ======================================================

# CONTROLS ==========================================================
    data group23_HW3_p2.dat;
    solve;
    
    print;
    print "Optimal amount of ";
    # display decisionVarNameHere;
    

