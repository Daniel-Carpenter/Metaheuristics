# Daniel Carpenter
# Final Exam
# Problem 1

reset;                  # Reset globals
options solver cplex;   # Using cplex for simplex alg

# SETS ============================================================

# PARAMETERS =======================================================

# DECISION VARIABLES ===============================================

# OBJECTIVE FUNCTION ===============================================

# CONSTRAINTS ======================================================

# CONTROLS ==========================================================
    data problem1.dat;
    solve;

    print;
    print "Create the following";
    # display decisionVarNameHere;
