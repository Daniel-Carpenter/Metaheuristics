#fiver from MIT 15-053 lecture notes

reset;

option solver cplex;


param N > 0;
let N := 5;

set RC circular;
let RC := 1..N;

set Positions within {RC,RC};
let Positions := {};

for {i in RC} {
 for {j in RC} {
    let Positions := Positions union {(i,j)};
 }
}

var x{Positions} binary;
var y{Positions} integer >=0, <=2;

minimize clicks: sum{(i,j) in Positions} x[i,j];
subject to flips {i in RC, j in RC}: x[i,j] + x[i,prev(j)] + +x[i,next(j)] + x[prev(i),j] + x[next(i),j] - 2*y[i,j] = 1;

solve;

for {i in RC}{
 for {j in RC}{
	printf "%d ", x[i,j];
 }
 printf "\n";
}