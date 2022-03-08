#DSA/ISE 5113 Integer Programming
#Example IP: oil exploration

#Find least-cost selection of 5 out of 10 possible sites 

reset;

#OPTIONS -----------------------------------------------------
option solver cplex;


#SETS AND PARAMETERS -----------------------------------------
set S = 1..10;
param c{S};

#DECISION VARIABLES ------------------------------------------
var x{S} binary;     #explore site s 


#OBJECTIVE ---------------------------------------------------
minimize cost: sum{s in S} c[s]*x[s];

#CONSTRAINTS -------------------------------------------------

#select exactly 5 sites
s.t. sites: sum{s in S} x[s] = 5;

#at most two of sites S5, S6, S7 and S8 may be explored
s.t. restrictions: x[5] + x[6] + x[7] + x[8] <=2;

#Exploring site S3 or site S4 prevents you from exploring site S5.
s.t. contingent1: x[3] + x[5] <=1;
s.t. contingent2: x[4] + x[5] <=1;


#exploring the combination of sites S1 and S7 will prevent you from exploring site S8.
s.t. contingent3: x[1] + x[7] + x[8] <= 2;


data;
param c := 1 10.0  2 15.1  3 7.2  4  9.9  5 11.2
           6  9.5  7 18.3  8 6.1  9 14.1 10 13.9;


solve;
display x;