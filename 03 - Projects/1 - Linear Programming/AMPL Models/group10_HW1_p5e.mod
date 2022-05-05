# Problem 5 
# BASE MODEL 
# Steel Mill 
# Daniel Carpenter and Effouehi Moody

# MODEL SETUP ----------------------------------------------------

	## Reset Environment
	reset;
	
	## Set up options and the solver
	option solver cplex;
	option cplex_options 'sensitivity';


# SETS ----------------------------------------------------------
	set PROD; 	# products 
	set STAGE;	# stages

# PARAMETERS ----------------------------------------------------
	param rate {PROD,STAGE} > 0; # tons per hour in each stage 
	param avail {STAGE} >= 0; 	 # hours available/week in each stage 
	param profit {PROD}; 		 # profit per ton

	param commit {PROD} >= 0; # lower limit on tons sold in week 
	param market {PROD} >= 0; # upper limit on tons sold in week


# DECISION VARS -------------------------------------------------
	var Make {p in PROD} >= commit[p], <= market[p]; # tons produced 


# OBJECTIVE: total profits from all products --------------------
	maximize Total_Profit: sum {p in PROD} profit[p] * Make[p]; 


# CONSTRAINTS ---------------------------------------------------
	# In each stage: total of hours used by all
	# products may not exceed hours available
	subject to Time {s in STAGE}: sum {p in PROD} (1/rate[p,s]) * Make[p] <= avail[s];


# DATA INPUTS --------------------------------------------------
	data group10_HW1_p5e.dat; 

# SOLVE --------------------------------------------------------
	solve;
	display Make;