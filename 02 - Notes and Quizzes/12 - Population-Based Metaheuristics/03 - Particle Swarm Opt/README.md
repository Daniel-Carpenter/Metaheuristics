# Partical Swarm Optimization (*PSO*)
> Swarm intelligence that mimics groups of individual fish or birds swarming together without understanding of an overall objective

## Content Overview
1. `PSO` vs `Genetic Algorithm`
2. Defining `Movement`: Inertia, Cognitive and Social Influence
3. Defining the `Swarm` vs. `Particles` 
4. PSO `Algorithm` Steps (*overview*)
5. PSO Neighborhoods (*`Global`* and *`Local`*)
6. PSO Variations


---

<br>

### Conceptual Overview
<img src = "Images/overview1.png" width = 550> <br>

### Visualizing `Swarms Intelligent` in Optimization?
<img src = "Images/swarm1.png" width = 250> <br>
<img src = "Images/swarm2.png" width = 250> <br>
<img src = "Images/swarm3.png" width = 250> <br>
<img src = "Images/swarm4.png" width = 250> <br>
---

<br>

## 1. `PSO` vs `GA`
<img src = "Images/overview2.png" width = 550> <br>

---

<br>

## 2. Defining `Movement`: Inertia, Cognitive and Social Influence
> `Movement` is how the particle goes about the space. 3 factors: 

<img src = "Images/overview3.png" width = 550> <br> <br>

Variable              | Description
----------------------|--------------
`Interia`             | Particle continues to *move in the direction it has been going*
`Cognitive Influence` | Pariticle uses its own memory to adjust the right direction for itself to move
`Social Influence`    | Info that is obtains from other particles in the space.

---

<br>

## 3. Defining the `Swarm` vs. `Particles` 
<img src = "Images/overview4.png" width = 550> <br>

---

<br>

## 4. PSO Algorithm Steps
1. `Initialize` the swarm from the solution space
2. `Evaluate` the fitness of each partical
3. `Update` the individual and global best solutions
4. For each particle, update the `velocity` and the `position`
5. Go back to `step 2`, then `repeat until` we meet the `stopping criteria`


### 4.4 Update the `Velocity` and `Position` of `Particle[i]`

### 4.4.1 `Updating the Velocity`
<img src = "Images/velocity1.png" width = 550> <br>
<img src = "Images/V0.png" width = 275>
<img src = "Images/V1.png" width = 275> <br>

### 4.4.2 `Limiting the Movement of Particles`
> Acceleration constants help limit particle movement  
> Large values of `phi` could cause particle to leave too quickly 

<img src = "Images/phi.png"       width = 550> <br>

### 4.4.3 Balancing `Exploration` and `Exploitation`
> Could force more exploration of area but disable swarm movement in later iterations  

<img src = "Images/converge1.png" width = 550> <br>
<img src = "Images/converge2.png" width = 550> <br>


---

<br>

## 5. PSO Neighborhoods (*`Global`* and *`Local`*)
> Not same concept as usual neighborhood  
> Neighborhoods depend on external relationships that are not problem dependant  

### 5.1 Neighborhood Overview
<img src = "Images/neigh0.png" width = 550> <br>

<br>

### 5.2 Neighborhood Types
> * `Global best` type is a fully connected neighborhood (like above models - note all info shared)
> * `Local best`  type is *not* than a fully connected neighborhood (not all info shared)

<img src = "Images/neigh1.png" width = 550> <br>
<img src = "Images/neigh2.png" width = 550> <br>
*Note `von Neumann` performs well*   
<img src = "Images/neigh3.png" width = 550> <br>
*Note `Star` prevents premature convergence but could lack collaberation*   
<img src = "Images/neigh4.png" width = 550> <br>

---

<br>

## 6. PSO Variations
<img src = "Images/variants.png" width = 550> <br>