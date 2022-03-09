#Galaxy Industries Linear Programming Problem

reset;

#set-up options
option solver cplex;

param gamma1;
param gamma2;

#decision variables
var SR >=0; #number of SpaceRay guns to manufacture
var  Z >=0; #number of Zapper guns to manufacture


#objective
#max profit, minimize labor

maximize weightedSum: gamma1*(8*SR + 5*Z) - gamma2*(3*SR + 4*Z);

#constraints
subject to plastic:   2*SR +   Z <= 1000;
subject to labor:     3*SR + 4*Z <= 2400;
subject to production:  SR +   Z <= 700;
subject to management:  SR -   Z <= 350;

#subject to temp: 8*SR + 5*Z = 2000;


#problem scalarized: weightedSum, SR, Z, plastic, labor, production, management; 


printf "\n\nMultiple values for SCALARIZATION -------------------------------------------------\n";
for {k in 0..10} {
	let gamma1 := k/10;
	let gamma2 := 1 - gamma1;
     
    #solve;# scalarized;
   
    #printf "\n\ngamma1 = %6.2f; gamma2 = %6.2f \n", gamma1, gamma2; 
    #printf "Optimal solution values: SR = %6.2f   Z = %6.2f \n", SR, Z; 
	#printf "Profit generated: %6.2f\n",  8*SR + 5*Z; 
	#printf "Labor used: %6.2f \n\n", 3*SR + 4*Z ;
    #printf "%d, %3.2f, %3.2f, %7.4f, %7.4f, %7.4f, %7.4f\n", k, gamma1, gamma2, SR, Z, 8*SR + 5*Z, 3*SR + 4*Z > "galaxyParetoS.txt";
}

printf "\n\nMultiple values for REPRESENTATION -------------------------------------------------\n";
for {k in 0..500} {
	
	repeat {
		
		fix SR := Uniform(0, 500);
		fix Z:= Uniform(0,800);
		
		} until 2*SR +   Z <= 1000 and 3*SR + 4*Z <= 2400 and SR +   Z <= 700 and SR -   Z <= 350;
	
   
     
    solve;# scalarized;
   
    if solve_result = "solved" then printf "%d, %3.2f, %3.2f, %7.4f, %7.4f, %7.4f, %7.4f\n", k, gamma1, gamma2, SR, Z, 8*SR + 5*Z, 3*SR + 4*Z > "galaxyParetoS.txt";
    
    unfix SR;
    unfix Z;
    
    
}

