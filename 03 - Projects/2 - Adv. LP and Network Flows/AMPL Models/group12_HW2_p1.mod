    # Homework 2 - Advanced LP & Network Flow Models
# Adv. Analytics and Metaheuristics
# Daniel Carpenter and Christopher Ferguson
# February 2022
# Problem 1

reset;                  # Reset globals
options solver cplex;   # Using cplex for simplex alg

# SETS ============================================================
    set FRUIT circular;	# Circular to index the kth element for constraint 2
    set PRODUCTS circular; # ""

# PARAMETERS =======================================================
    param amountOfFruit {FRUIT} >= 0;   # Pounds of fruit available by grade
    param avgGradeOfFruit {FRUIT};      # Avg fruit grade
    param productLimit {PRODUCTS} >= 0; # Demand for products
    param poundsPerProduct {PRODUCTS};  # Pounds associated with a product
    param contrToProfit {PRODUCTS};     # Product contribution to profit
    param netProfit {PRODUCTS};         # Net profit per product
    param productGradeLimit {PRODUCTS}; # The min grade for each product
	param sellingPrice {PRODUCTS};		# Selling price of each product
	param contrToProfitT3 {PRODUCTS};	# Product contribution to profit from Table 3
	param marginalProfitT3 {PRODUCTS};	# Marginal profit from Table 3

# DECISION VARIABLES ===============================================
    ## Includes upper and lower bounds
    var produce {f in FRUIT, p in PRODUCTS} >= 0 integer;

# OBJECTIVE FUNCTION ===============================================
    maximize Total_Profit: 
        sum {f in FRUIT, p in PRODUCTS} produce[f, p] * contrToProfitT3[p];

# CONSTRAINTS ======================================================

    ## C1: Number of pounds of the products produced (p ∈ PRODUCTS) must be <=  pounds of fruit provided (f ∈ FRUIT)
    subject to maxWeight {f in FRUIT}: 
        (sum {p in PRODUCTS} produce[f,p] * poundsPerProduct[p]) == amountOfFruit[f];

    ## C2:  Limit the number of produced to <= the demand
    subject to demand {p in PRODUCTS}:
        (sum {f in FRUIT} produce[f,p]) <= productLimit[p];

    ## C3: For all products (p ∈ PRODUCTS), the weighted-average grade of fruit is greater than the minimum required grade.
    subject to minAvgGrade {p in PRODUCTS}: 
        (sum {f in FRUIT} produce[f,p] * avgGradeOfFruit[f])
        >=  productGradeLimit[p] * (sum {f in FRUIT} produce[f,p]);

# CONTROLS ==========================================================
    data group12_HW2_p1.dat;
    solve;
    
    print;
    print "At maximum profit, the number of products to produce (by fruit grade):";
    display produce;
    #display maxWeight;
    display minAvgGrade;
    #display demand;
    

