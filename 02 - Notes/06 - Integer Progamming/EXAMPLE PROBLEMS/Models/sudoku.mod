reset;

param N := 4;   #must be perfect square: e.g. 4,9,16
param n := sqrt(N);

set K = {1..N};   # digits
set I = 1..N;   #rows; 
set J = 1..N;   #columns 

set G within {I,J,K} = {(1,1,2),(4,4,4)};

#DECISION VARIABLES
var x {I,J,K} binary; 


#OBJECTIVE
minimize cost: 0;


subject to cols {j in J, k in K}: sum{i in I} x[i,j,k] = 1; 

subject to rows {i in I, k in K}: sum{j in J} x[i,j,k] = 1; 

subject to allv {i in I, j in J}: sum{k in K} x[i,j,k] = 1; 

subject to subs {p in {1..n}, q in {1..n}, k in K}: sum{j in {n*q-(n-1) .. n*q}, i in {n*p-(n-1) .. n*p}}  x[i,j,k] = 1; 

subject to givens {(i,j,k) in G}: x[i,j,k]=1;

solve;

display x;

for {i in I} {
 for {j in J} {
  for {k in K} {
   if (x[i,j,k] == 1) then printf "(%d,%d)=%s ",i,j, k;
}}
printf "\n";}

#display {k in K}: sum{i in I, j in J} x[i,j,k]; 

for {i in I} {
 for {j in J} {
  for {k in K} {
   if (x[i,j,k] == 1) then printf " %s ", k;
}}
printf "\n";}

