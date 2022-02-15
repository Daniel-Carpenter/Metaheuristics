# Homework 2 - Advanced LP & Network Flow Models
# Adv. Analytics and Metaheuristics
# Daniel Carpenter and Christopher Ferguson
# February 2022

reset;
options solver cplex;

# SETS -------------------------------------------------------------
    # The discrete day numbers to make tires (1, 2, 3, 4)

# PARAMETERS -------------------------------------------------------
    param NUM_DAYS; # Total number of days possible
    param P >= 0;  # Price of *purchasing* new tires  
    param N >= 0;  # Cost of *normal* service on used tires
    param Q >= 0;  # Cost of *quick* service on used tires
    param r {1 .. NUM_DAYS};   # Demand of tires per day (j ∈ 1 .. NUM_DAYS) 

# DECISION VARS ----------------------------------------------------
    var purch {1 .. NUM_DAYS} >= 0;	# Number of tires to purchase on day (j∈1 .. NUM_DAYS)
    var norm {1 .. NUM_DAYS}  >= 0;	# Number of tires to reshape using the normal service on day (j∈1 .. NUM_DAYS)
    var quick {1 .. NUM_DAYS} >= 0;	# Number of tires to reshape using the quick service on day (j∈1 .. NUM_DAYS)

 #OBJECTIVE FUNCTION -----------------------------------------------
    # Minimize total cost by when using the three types of tire services
    minimize cost: sum{j in 1 .. NUM_DAYS} (purch[j]*P + norm[j]*N + quick[j]*Q);

# CONSTRAINTS -------------------------------------------------------
    
    # Purchase on day 1
    subject to purchaseDay1: 
        purch[1] = r[1];
    
    # Meet the daily required demand
    subject to dailyDemand {j in 1 .. NUM_DAYS}: 
        purch[j] + norm[j] + quick[j] == r[j]; 

    # Can only reshape using normal service every other day
    subject to normOneDay {j in 2 .. NUM_DAYS}: norm[j] + norm[j-1] <= r[j];

# LOAD DATA ---------------------------------------------------------
    data group12_HW2_p3.dat;

# COMMANDS ----------------------------------------------------------
    solve;

    print;
    print 'Tires Purchased:';
    display purch;

    print;
    print 'Tires Reshaped w/Normal:';
    display norm;

    print;
    print 'Tires Reshaped w/Quick:';
    display quick;









  
