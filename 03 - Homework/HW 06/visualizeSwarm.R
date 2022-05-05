
# ==============================================================================
# Viewer for the first n particle swarm optimization iterations
# ==============================================================================

library(readr)     # Read CSV
library(tidyverse) 
library(ggplot2)   # Plots
library(knitr)     # table printing


# Pull in the data from the swarm optimization (written in main loop)
swarmData <- read_csv('output.csv')


# Table holding the 5 iterations for the 5 particles
# Position and Velocity 1 & 2, as well indicator of global best
swarmDataTable <- swarmData %>%
  mutate(isGlobalBest = if_else(position1 == globalBest1 & 
                                  position2 == globalBest2, 
                                'New Global Best!', '') 
  ) %>%
  
  select(particle, iteration, starts_with('pos'), starts_with('vel'),
         isGlobalBest)

# Print the table
print(kable(swarmDataTable))


# Plot the first 5 iterations with each particle's position
iterPlot <- swarmData %>% 
  ggplot(aes(x = position1,
             y = position2)) +
  
  # Points for the Swarm
  geom_point(alpha = 0.2,
             color = 'steelblue3',
             size  = 5) +
  
  # Red Point for the global best
  geom_point(aes(x = globalBest1,
                 y = globalBest2),
             alpha = 0.25,
             color = 'tomato3',
             size  = 5,
             shape = 18) +
  
  # Label for the global best
  geom_text(label = paste0('     Global Best:       (', round(swarmData$globalBest1, 2), ',', 
                                               round(swarmData$globalBest2, 2),')'),
            aes(x = globalBest1,
                y = globalBest2),
            color = 'tomato3',
            alpha = 0.9,
            size = 3) +
  
  # Facet by Iteration
  facet_grid(rows = vars(paste0('Iteration #: ', iteration)),
             switch = 'y') +
  labs(title = 'Particle Swarm Optimization',
       subtitle = paste0('Shows the first ', max(swarmData$iteration), 
                         ' iterations of the PSO | Daniel Carpenter'),
       x = 'Position 1',
       y = 'Position 2') + 
  
  theme_bw() # a theme

print(iterPlot)
