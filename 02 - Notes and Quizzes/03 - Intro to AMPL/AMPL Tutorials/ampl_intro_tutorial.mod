#AMPL tutorial for DSA/ISE 5113 students
#Author: Rafia Bushra
#Date: 01/26/2021

reset;
option solver cplex;

#------------------------Parameters------------------------
#Example of defining sets
set MONTH;
set YEAR;

#Example of defining simple, single-valued parameters
param type; #product types
param purchase_cost; #cost of purchasing pre-made products
param making_cost; #cost of making a product
param selling_price; #selling price of each unit

#Example of multi-valued parameters that has values for each value of a pre-defined set 
param demand {1 .. type}; #demand for each product type
param budget {YEAR}; #yearly budget

#Example of a 2 dimensional multi-valued parameter
#i.e. a parameter that depends on 2 pre-defined sets
param limit {MONTH, YEAR}; #maximum number of items that can be produced per term





#------------------------Decision Variables------------------------
#Example of a single-valued decision variable with a single constraint
var purchase >= 0; #Number of products to be purchased at the beginning
#Example of a multi-valued decision variable with multiple constraints
var x {m in MONTH,y in YEAR} >=0, <= limit[m, y]; #Number of products to be produced each month and year 




#------------------------Objective Function------------------------
#Example of a maximizing objective function
maximize profit: selling_price*(purchase + sum {m in MONTH,y in YEAR} x[m,y]) - 
((purchase_cost*purchase) + (making_cost*sum {m in MONTH,y in YEAR} x[m,y]));

/*Example of a minimizing objective function
This block is commented because our objective is not to minimize
minimize profit: selling_price*(purchase + sum {m in MONTH,y in YEAR} x[m,y]) - purchase_cost*purchase;
*/




#------------------------Constraints------------------------
subject to yearly_budget {y in YEAR} : sum {m in MONTH} making_cost*x[m, y] <= budget[y]; #For each year, the total cost of making the products must be less or equal to the yearly budget   
s.t. pre_made_limit : purchase_cost*purchase <= 100; #pre-purchase product cost can not be more than $100




#------------------------Data-----------------------
data ampl_intro_tutorial.dat;




#------------------------Commands------------------------
solve; #solve the LP problem

#Example of simply displaying
display purchase; #Display the purchase variable
display budget; #Display the budget parameter

expand yearly_budget["y2020"]; #Show the yearly_budget constraint at y2020 index 

#Example of nicely printing
printf "-----Solution----- \n";
printf "Number of pre-made products: %d \n", purchase;
for {y in YEAR} {
	printf "Nmmber of products made in February of %s: %d \n", y, x['feb',y];
}
printf " \n ";
