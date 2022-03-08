#DSA/ISE 5113 Integer Programming
#Example IP: basic facility location

#A company is thinking about building new facilities in LA and SF.
#Which facilities should be built to maximize the total profit?

reset;

#OPTIONS -----------------------------------------------------
option solver cplex;


#DECISION VARIABLES ------------------------------------------
var x1 binary;     #build new factory in LA
var x2 binary;     #build new factory in SF
var x3 binary;     #build new warehouse in LA
var x4 binary;     #build new warehouse in SF


#OBJECTIVE ---------------------------------------------------
maximize profit: 9*x1 + 5*x2 + 6*x3 + 4*x4;

#CONSTRAINTS -------------------------------------------------

#constrain total amount to 10 million
s.t. budget: 6*x1 + 3*x2 + 5*x3 + 2*x4 <= 10;

#build at most one of the two warehouses
s.t. warehouses: x3 + x4 <= 1;

#build at least one of the two factories
s.t. factories: x1 + x2 >= 1;

#can’t build a warehouse unless there is a factory in the city
s.t. LA: x3 <= x1;
s.t. SF: x4 <= x2;

#can’t select option 3 unless at least one of options 1 and 2 is selected
s.t. additionalReq: x3 <= x1 + x2;

#can’t select option 4 unless at least two of options 1, 2 and 3 are selected
s.t. anotherReq: 2*x4 <= x1 + x2 + x3;

solve;
display x1, x2, x3, x4;