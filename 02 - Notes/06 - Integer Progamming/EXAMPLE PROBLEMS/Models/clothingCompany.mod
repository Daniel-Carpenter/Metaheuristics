#DSA/ISE 5113 Integer Programming
#Example IP: Gandhi Clothing Company (GCC)

#GCC manufactures 3 types of clothing: shirts, shorts, and pants; and each requires certain machinery

reset;

#OPTIONS -----------------------------------------------------
option solver cplex;


#DECISION VARIABLES ------------------------------------------
var x1 >= 0, integer;     # qty of shirts to make
var x2 >= 0, integer;     # qty of shorts to make
var x3 >= 0, integer;     # qty of pants to make

var y1 binary;     # rent shirt machine? 1= yes, 0 = no
var y2 binary;     # rent shorts machine? 1= yes, 0 = no
var y3 binary;     # rent pants machine? 1= yes, 0 = no

#OBJECTIVE ---------------------------------------------------
maximize profit: 6*x1 + 4*x2 + 7*x3 - 200*y1 - 150*y2 - 100*y3;

#CONSTRAINTS -------------------------------------------------

#limited labor
s.t. labor: 3*x1 + 2*x2 + 6*x3 <= 150;

#limited cloth
s.t. cloth: 4*x1 + 3*x2 + 4*x3 <= 160;

#logical connections between x variables and y variables
s.t. x1_and_y1: x1 <= 40*y1;
s.t. x2_and_y2: x2 <= 53*y2;
s.t. x3_and_y3: x3 <= 25*y3;



solve;
display x1, x2, x3, y1, y2, y3;