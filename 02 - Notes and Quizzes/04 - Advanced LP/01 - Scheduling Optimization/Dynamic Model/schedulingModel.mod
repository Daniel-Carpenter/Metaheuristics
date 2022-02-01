#AMPL code for the "Macrosoft" problem DSA/ISE 5113 

reset;

# OPTIONS ----------------------------------------

options solver cplex;


# PARAMETERS AND SETS ----------------------------

    set T circular;    #set of time periods

    param c_FT   >=0;  #cost of FT employee
    param c_PT   >=0;  #cost of PT employee

    param PT_FTE >=0;  #value of PT employee
    param HRfraq >=0;  #HR requirement of min percent of FT employees working

    param FTE{T} >=0;  #daily FTE requirements 


# DECISION VARIABLES ----------------------------

    var empFT{T} >=0 integer; #number of FT employees starting in each time period
    var empPT{T} >=0 integer; #number of PT employees starting in each time period



# OBJECTIVE --------------------------------------
    minimize cost: (c_FT*sum{t in T} empFT[t]) + (c_PT*sum{t in T} empPT[t]);


#CONSTRAINTS ------------------------------------
    subject to FTEreq {t in T}: empFT[t] + empFT[prev(t)] + PT_FTE*empPT[t] >= FTE[t];
    subject to HRreq  {t in T}: empFT[t] + empFT[prev(t)] >= HRfraq * (empFT[t] + empFT[prev(t)] + empPT[t]);


# LOAD DATA --------------------------------------
    data schedulingModel.dat;


# COMMANDS ---------------------------------------
    solve;

    print;
    print 'Number of Full-Time Employees to schedule:';
    display empFT;

    print 'Number of Part-Pime Employees to schedule:';
    display empPT;