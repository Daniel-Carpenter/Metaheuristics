
reset;                  # Reset globals
options solver cplex;   # Using cplex for simplex alg

# SETS ============================================================
    set FRUIT;
    set PRODUCTS;

# PARAMETERS =======================================================
    param amountOfFruit {FRUIT} >= 0;
    param avgGradeOfFruit {FRUIT};
    param productLimit {PRODUCTS} >= 0;
    param poundsPerProduct {PRODUCTS};
    param contrToProfit {PRODUCTS};
    param netProfit {PRODUCTS};
    param productGradeLimit {PRODUCTS};


# DECISION VARIABLES ===============================================
    var produce {FRUIT, p in PRODUCTS} >= 0, <= productLimit[p];
    # var grade {p in PRODUCTS} >= 0, <= 10;

# OBJECTIVE FUNCTION ===============================================
    maximize Total_Profit: 
        sum {f in FRUIT, p in PRODUCTS} produce[f, p] * netProfit[p];

# CONSTRAINTS ======================================================

    ## C1
    subject to maxweight: 
        sum {p in PRODUCTS} produce[p] * poundsPerProduct[p] <= 6200000;

    ## C2
    subject to grades {p in PRODUCTS}: 
        (sum {f in FRUIT} amountOfFruit[f] * avgGradeOfFruit[f]) / produce[p] >=  grade[p];

# CONTROLS ==========================================================
    data HW2Q1.dat;
    solve;
    display produce;
    display grade;

