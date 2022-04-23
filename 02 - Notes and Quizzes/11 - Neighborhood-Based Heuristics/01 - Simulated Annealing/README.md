
# Simulated Annealing
> Escape local minima by making *controlled bad moves*.  
> As the algorithm continues to makes moves, *gradually make less frequent bad moves*

---
<br>

## SA vs. Hill Climbing
* Hill climbing makes the best move always
* Simulated Annealing makes the bad moves sometimes

---
<br>

## SA Conceptual Process
1. Instead of choosing best move, choose a random move
2. Acceptance Options
    i. `If the move is BETTER` than the current solution, `Accept`
    ii. `If the move is WORSE` than the current solution, `Accept with probability p`

### Controlling Bad Moves: Less bad as iterations increase:
<img src = 'Images/probOfBadMove1.png' width = 400> <br>
<img src = 'Images/probOfBadMove.png' width = 250> <br>
<img src = 'Images/probOfBadMove2.png' width = 400> <br>
<img src = 'Images/probOfBadMove3.png' width = 400> <br>

---
<br>

## SA Algorithm - Conceptual Details

### Conceptual Algorithm
<img src = 'Images/alg0.png' width = 550> <br>

<br>

### Pseudo-Code
<img src = 'Images/alg1.png' width = 550> <br>
<img src = 'Images/alg2.png' width = 550> <br>

---
<br>

## The Terminology: SA analogous to Thermodynamics
<img src = 'Images/term.png' width = 550> <br>
<img src = 'Images/term1.png' width = 550> <br>
