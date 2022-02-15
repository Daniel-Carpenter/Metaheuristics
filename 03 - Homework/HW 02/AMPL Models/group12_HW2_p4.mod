# AMPL model for the Minimum Cost Network Flow Problem
#
# By default, this model assumes that b[i] = 0, c[i,j] = 0,
# l[i,j] = 0 and u[i,j] = Infinity.
#
# Parameters not specified in the data file will get their default values.

reset;
options solver cplex;

set NODES;                        # nodes in the network
set ARCS within {NODES, NODES};   # arcs in the network 
set LABOR;                        # nodes in the network
set PLANTS;                        # nodes in the network

param b {NODES} default 0;        # supply/demand for node i
param c {ARCS}  default 0;        # cost of one of flow on arc(i,j)
param l {ARCS}  default 0;        # lower bound on flow on arc(i,j)
param u {ARCS}  default Infinity; # upper bound on flow on arc(i,j)
param mu {ARCS} default 1;       # multiplier on arc(i,j) -- if one unit leaves i, mu[i,j] units arrive
param totalHours {LABOR}; # hours available per month for labor
param productionLimit {PLANTS}; # The production limit for each Plant


var x {ARCS};                     # flow on arc (i,j)
 
minimize cost: sum{(i,j) in ARCS} c[i,j] * x[i,j];  #objective: minimize arc flow cost

# Flow Out(i) - Flow In(i) = b(i)

subject to flow_balance {i in NODES}:
    sum{j in NODES: (i,j) in ARCS} x[i,j] - sum{j in NODES: (j,i) in ARCS} x[j,i] = b[i];

subject to capacity {(i,j) in ARCS}: 
    l[i,j] <= x[i,j] <= u[i,j];

# subject to laborLimit {i in LABOR}:
#     sum{j in NODES: (i,j) in ARCS} x[i, j] <= totalHours[i];


# LOAD DATA ---------------------------------------------------------
    data group12_HW2_p4.dat;

# COMMANDS ----------------------------------------------------------
    solve;








  
