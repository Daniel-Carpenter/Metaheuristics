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
    param M;                          # Map decision variables together 

# DECISION VARIABLES ===============================================
    var tonsOfProduct {PRODUCTS, SILOS} >= 0;  # Amount of each product p to store in silo s
    var isStored      {PRODUCTS, SILOS} binary; # If a product is stored in a silo or not

# OBJECTIVE FUNCTION ===============================================

    minimize costOfStorage: 
        sum{p in PRODUCTS, s in SILOS} tonsOfProduct[p,s] * cost[p,s]; 

# CONSTRAINTS ======================================================

    # C1: For each silo s, the tons of the supplied product p must be less than or equal to the capacity limit of silo s
    subject to meetCapacity {s in SILOS}: 
        (sum{p in PRODUCTS} tonsOfProduct[p,s]) <= capacity[s];

    # C2: For each product p, must use all of the total product that is available
    subject to useAllProduct {p in PRODUCTS}: 
        (sum{s in SILOS} tonsOfProduct[p,s]) == supply[p];

    # C3: Only one product can be in a silo
    subject to oneProductInSilo {s in SILOS}:
        sum{p in PRODUCTS} isStored[p,s] == 1;

    # C4: Map decision variables together
    subject to mapVars {p in PRODUCTS, s in SILOS}: 
        tonsOfProduct[p,s] <= M * isStored[p,s];

# CONTROLS ==========================================================
    data group23_HW3_p2.dat;
    solve;
    
    print;
    print "Which silo(s) stores what product?";
    display isStored; 

    print "Optimal tons of product allocated to each silo:";
    display tonsOfProduct; 
    

