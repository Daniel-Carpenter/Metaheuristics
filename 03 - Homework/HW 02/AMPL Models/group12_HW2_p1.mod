
reset;                  # Reset globals
options solver cplex;   # Using cplex for simplex alg

# SETS ============================================================
    set FRUIT circular;	# Circular to index the kth element for constraint 2
    set PRODUCTS circular; # ""

# PARAMETERS =======================================================
    param amountOfFruit {FRUIT} >= 0;   # amt of fruit available by grade
    param avgGradeOfFruit {FRUIT};      # Avg fruit grade
    param productLimit {PRODUCTS} >= 0; # Demand for products in tons
    param poundsPerProduct {PRODUCTS};  # Pounds associated with a product
    param contrToProfit {PRODUCTS};     # Product contribution to profit
    param netProfit {PRODUCTS};         # Net profit per TON
    param productGradeLimit {PRODUCTS}; # The min grade for each product


# DECISION VARIABLES ===============================================
    ## Includes upper and lower bounds
    var produce {f in FRUIT, p in PRODUCTS} >= 0;
    # var grade {p in PRODUCTS} >= 0, <= 10;

# OBJECTIVE FUNCTION ===============================================
    maximize Total_Profit: 
        sum {f in FRUIT, p in PRODUCTS} produce[f, p] * netProfit[p];

# CONSTRAINTS ======================================================

    ## C1: Number of products produced (p ∈ PRODUCTS) must be <=  tons of fruit provided (f ∈ FRUIT)
    subject to maxTons {f in FRUIT}: 
        (sum {p in PRODUCTS} produce[f,p]) == amountOfFruit[f];

    ## C2:  Limit the number of produced to <= the demand
    subject to demand {p in PRODUCTS}:
        (sum {f in FRUIT} produce[f,p]) <= productLimit[p];

    ## C3: Cannot produce Jelly (idx 1) using Grade A (idx 3)
    subject to noGradeAJelly: 
        produce[member(1, FRUIT), member(3, PRODUCTS)] == 0;


    # subject to grades {p in PRODUCTS}: 
    #     (sum {f in FRUIT} amountOfFruit[f] * avgGradeOfFruit[f]) / produce[p] >=  grade[p];

# CONTROLS ==========================================================
    data group12_HW2_p1.dat;
    solve;
    
    print;
    print "At maximum profit, the tons of each product to product (by fruit grade):";
    display produce;
    #display grade;

