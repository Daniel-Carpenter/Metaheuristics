reset;

#OPTIONS -----------------------------------------------------
option solver cplex;
option solver_msg 0;

#SETS AND PARAMETERS -----------------------------------------
set INVESTMENTS;
set COMBINATIONS;

param return{INVESTMENTS} >=0;     #amount of returns as percent of investment
param risk{INVESTMENTS} >=0;       #amount of risk as percent of investment
param fixedCost{INVESTMENTS} >=0;

param upper{INVESTMENTS} >=0, <=1;      #upper bound on investment (percent of capital)
param lower{INVESTMENTS} >=0, <=1;      #lower bound on investment (percent of capital)

param capital >=0;

param combo{COMBINATIONS, INVESTMENTS};
param comboReq{COMBINATIONS} >=0;

param numConstraints >=0;
param bigM = capital;


#DATA --------------------------------------------------------
data riskReward.dat;

#DECISION VARIABLES ------------------------------------------
var x {i in INVESTMENTS} >=lower[i]*capital, <=upper[i]*capital;   #dollars to invest in investment i \in INVESTMENTS
var y {i in INVESTMENTS} binary;  #whether or not to invest in i
var z {j in COMBINATIONS} binary;



#OBJECTIVE ---------------------------------------------------
maximize objRETURNS:        sum{i in INVESTMENTS} return[i] * x[i];
minimize objRISKS: 		    sum{i in INVESTMENTS} risk[i] * x[i];


#CONSTRAINTS -------------------------------------------------
s.t. budget: sum{i in INVESTMENTS} (x[i] + y[i]*fixedCost[i]) = capital;
s.t. mix {c in COMBINATIONS}: sum{i in INVESTMENTS} combo[c,i] * x[i] >= capital * comboReq[c] - bigM*(1-z[c]) ;   
s.t. disjunctive: sum{c in COMBINATIONS} z[c] >= numConstraints;
s.t. investBinary {i in INVESTMENTS}: x[i] <= y[i]*bigM;

#INDEPENDENT OBJECTIVES -------------------------------------------------
printf "\n\nINDEPENDENT OBJECTIVES -------------------------------------------------\n";

#PROBLEMS
problem maxReturn: objRETURNS, x, y, z, budget, mix, disjunctive, investBinary; 
problem minRisk:   objRISKS, x, y, z, budget, mix, disjunctive, investBinary; 

printf "\nMaximize Return...........\n";

solve maxReturn;
display x, objRETURNS, objRISKS;


printf "\nMinimze Risk...........\n";
solve minRisk;
display x, objRETURNS, objRISKS;



#PREMPTIVE OPTIMIZATION -------------------------------------------------
printf "\n\nPREMPTIVE OPTIMIZATION -------------------------------------------------\n";
param optimalValue;

#using RETURN as the 1st priority

printf "\nOptimize first priority...\n";
solve maxReturn;
let optimalValue := objRETURNS;
s.t. stayOptReturns: sum{i in INVESTMENTS} return[i] * x[i] >= optimalValue;

printf "\nOptimize second priority subject to bounds on first...\n";
problem minRisk_2: objRISKS, x, y, z, budget, mix, disjunctive, stayOptReturns, investBinary;
solve minRisk_2;
display x, objRETURNS, objRISKS;


#using RISK as the 1st priority
printf "\nOptimize first priority...\n";
solve minRisk;
let optimalValue := objRISKS;
s.t. stayOptRisks: sum{i in INVESTMENTS} risk[i] * x[i] <= optimalValue;

printf "\nOptimize second priority subject to bounds on first...\n";
problem maxReturn_2: objRETURNS, x, y, z, budget, mix, disjunctive, stayOptRisks, investBinary;
solve maxReturn_2;
display x, objRISKS, objRETURNS;



#SCALARIZATION -------------------------------------------------
printf "\n\nSCALARIZATION -------------------------------------------------\n";
param lambda1;
param lambda2;

let lambda1 := 0.25;
let lambda2 := 1 - lambda1;

maximize weighedRiskReturn:   sum{i in INVESTMENTS} (lambda1 * (return[i] * x[i]) - lambda2 * (risk[i] * x[i]));
problem scalarized: weighedRiskReturn, x, y, z, mix, disjunctive, budget, investBinary; 
solve scalarized;
display x, weighedRiskReturn, objRETURNS, objRISKS;




printf "\n\nMultiple values for SCALARIZATION -------------------------------------------------\n";
for {k in 0..100} {
	let lambda1 := k/100;
	let lambda2 := 1 - lambda1;
     
    solve scalarized;
    #display x, lambda1, lambda2, weighedRiskReturn, objRETURNS, objRISKS;
  
    printf "%d, %3.2f, %3.2f, %7.4f, %7.4f\n", k, lambda1, lambda2, objRETURNS, objRISKS > "paretoS.txt";
}


#EPSILON-CONSTRAINT
printf "\n\EPSILON-CONSTRAINT -------------------------------------------------\n";

#get upper and lower bounds for objectives
param upperRisk;
param lowerRisk;


solve maxReturn;
let upperRisk:=objRISKS;

solve minRisk;
let lowerRisk:=objRISKS;

param epsilon;
let epsilon := objRISKS;


s.t. epsilsonRisks:  sum{i in INVESTMENTS} risk[i] * x[i] <= epsilon;
problem epsConst:  objRETURNS, x, y, z, mix, disjunctive, budget, epsilsonRisks, investBinary; 

param steps = 50;

printf "\n\nMultiple values for EPSILON-CONSTRAINT -------------------------------------------------\n";
for {eps in 0..steps} {
	
	let epsilon := lowerRisk + eps*(upperRisk - lowerRisk)/(steps+1);
	solve epsConst;
	#display x, epsilon, objRETURNS, objRISKS;
	
	printf "%d, %7.4f, %7.4f, %7.4f\n", eps, epsilon, objRETURNS, objRISKS > "paretoEps.txt";
	
}




















