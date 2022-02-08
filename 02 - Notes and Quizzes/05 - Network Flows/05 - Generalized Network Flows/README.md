# Network Flow Modeling
> Generalized Network Flow `via Minimum Cost Flow` Modeling  
> * SEE SLIDES
* Uses multiplier on each flow
* Models conversions - like currencies or deterioration (like `spoliage`)

---

## Code

### Data Inputs *`data.dat`*
```py
#Generalized Network Flow Problem - data file for Political Action Figures Example problem -- 
#a.k.a.: "Feel the burn and make optimization great again!"
#Charles Nicholson, ISE 5113, 2020

#use with Generalized flow model: GMCNFP.txt model
#note: default arc costs and lower bounds are 0
#      default arc upper bounds are infinity
#      default node requirements are 0
#      default multiplier is 1

set NODES :=  	p1 p2 p3 p4            #product time period nodes
		c1 c2 c3 c4 c5 c5p;    #cash flow time period nodes

set ARCS := 	(p1,p2) (p2,p3) (p3, p4)            #inventory arcs
                (c1,c2) (c2,c3) (c3, c4) (c4, c5)   #cash flow arcs  
		(c5, c5p)                           #virtual arc
		(p1,c2) (p2,c3) (p3, c4) (p4, c5)   #sell arcs
                (c1,p2) (c2,p3) (c3, p4);           #buy arcs

param b:= p1 750     #initial product on-hand
	  c1 8500;   #initial cash on-hand

#specify costs, upper bound, and multipliers for each arc
param:  c u mu :=
        [p1, p2] 0.50  1500  0.99   #holding cost, capacity, 1-spoilage rate
        [p2, p3] 0.50  1500  0.99
        [p3, p4] 0.50  1500  0.99
        [c1, c2] . . 1.0025         #short-term interest
        [c2, c3] . . 1.0025
        [c3, c4] . . 1.0025
        [c4, c5] . . 1.0025  
        [p1, c2] . . 10             #product price
       	[p2, c3] . . 40    
        [p3, c4] . . 80
        [p4, c5] . . 50
        [c1, p2] . . 0.1            #1/price 
        [c2, p3] . . 0.025
        [c3, p4] . . 0.0125
        [c5, c5p] -1 . 0;           #virtual arc has negative cost to icentavize flow
```

<br>

### Model *`model.txt`*

```py
# AMPL model for the Minimum Cost Network Flow Problem
#
# By default, this model assumes that b[i] = 0, c[i,j] = 0,
# l[i,j] = 0 and u[i,j] = Infinity.
#
# Parameters not specified in the data file will get their default values.

options solver cplex;

set NODES;                        # nodes in the network
set ARCS within {NODES, NODES};   # arcs in the network 

param b {NODES} default 0;        # supply/demand for node i
param c {ARCS}  default 0;        # cost of one of flow on arc(i,j)
param l {ARCS}  default 0;        # lower bound on flow on arc(i,j)
param u {ARCS}  default Infinity; # upper bound on flow on arc(i,j)
param mu {ARCS} default 1;       # multiplier on arc(i,j) -- if one unit leaves i, mu[i,j] units arrive

var x {ARCS};                     # flow on arc (i,j)
 
minimize cost: sum{(i,j) in ARCS} c[i,j] * x[i,j];  #objective: minimize arc flow cost

# Flow Out(i) - Flow In(i) = b(i)

subject to flow_balance {i in NODES}:
sum{j in NODES: (i,j) in ARCS} x[i,j] - sum{j in NODES: (j,i) in ARCS} mu[j,i] * x[j,i] = b[i];

subject to capacity {(i,j) in ARCS}: l[i,j] <= x[i,j] <= u[i,j];
```

<br>

> Output
```
```
