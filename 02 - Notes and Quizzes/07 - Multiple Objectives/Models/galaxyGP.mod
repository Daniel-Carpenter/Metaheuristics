#Galaxy Industries Linear Programming Problem

reset;

#set-up options
option solver cplex;

#decision variables
var SR >=0; #number of SpaceRay guns to manufacture
var  Z >=0; #number of Zapper guns to manufacture

var d_positive >=0;  #deviation above goal
var d_negative >=0;  #deviation under goal

#goal: hit 4000 in profit exactly

#objective
minimize deviations: d_positive + d_negative;

#constraints
subject to goal: 8*SR + 5*Z = 8000 + d_positive - d_negative;

subject to plastic:   2*SR +   Z <= 1000;
subject to labor:     3*SR + 4*Z <= 2400;
subject to production:  SR +   Z <= 700;
subject to management:  SR -   Z <= 350;


solve;
printf "\nOptimal solution values:\n SR = %6.2f   Z = %6.2f \n", SR, Z; 
printf "\nProfit generated: %6.2f\n",  8*SR + 5*Z; 
printf "Deviation from goal: %6.2f \n", deviations;





