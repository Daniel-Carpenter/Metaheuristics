#DSA/ISE 5113 Integer Programming
#Example IP: Piecewise Linear Cost example

#this was not really a whole example from the lecture, so
#I am making it one now

#assume the linear costs from the lecture for a decision variable x as follows
#cost = 5 for  0 <=x < 4
#cost = 1 for  4 <=x <10
#cost = 3 for 10 <=x <15

#assume the linear costs from the lecture for a decision variable y as follows
#cost = 1 for  0 <= z <  4
#cost = 3 for  4 <= z < 10
#cost = 6 for 10 <= z < 15


reset;

#OPTIONS -----------------------------------------------------
option solver cplex;


#DECISION VARIABLES ------------------------------------------
var x >= 0, <=15;   #amt of product x to produce
var z >= 0, <=15;   #amt of product z to produce

var d1 >=0;  # piecewise component 1 of var x
var d2 >=0;  # piecewise component 2 of var x 
var d3 >=0;  # piecewise component 3 of var x

var y1 binary; #to model piecewise cost for var x
var y2 binary; #to model piecewise cost for var x

var e1 >=0;  # piecewise component 1 of var z
var e2 >=0;  # piecewise component 2 of var z 
var e3 >=0;  # piecewise component 3 of var z

#OBJECTIVE ---------------------------------------------------
minimize cost: 5*d1 + d2 + 3*d3 + e1 + 3*e2 + 6* e3;

#CONSTRAINTS -------------------------------------------------

#connect x with d1, d2, and d3;
s.t. X: x = d1 + d2 + d3;

#ensure that the piece wise costs are used correctly,
#i.e., you have to use all of d1 before you use d2,...

s.t. piece1a: 4*y1 <= d1;
s.t. piece1b: d1 <= 4;

s.t. piece2a: 6*y2 <= d2;
s.t. piece2b: d2 <= 6*y1;

s.t. piece3: d3 <= 5*y2;

#connect z with e1, e2, and e3;
s.t. Z: z = e1 + e2 + e3;

s.t. e1Bounds: e1 <= 4;
s.t. e2Bounds: e2 <= 10;
s.t. e3Bounds: e3 <= 15;

#note: since the costs are increasing for the pieces of z, they will be used in order

#add a constraint to make it produce something
s.t. dosomething: x + z >= 26;

solve;
display x, d1, d2, d3, y1, y2;
display z, e1, e2, e3;
