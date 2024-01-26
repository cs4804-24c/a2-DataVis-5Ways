library(palmerpenguins)
library(conflicted)  

library(tidyverse)
conflict_prefer("filter", "dplyr")
conflict_prefer("lag", "dplyr")

plot(penguins$flipper_length_mm, penguins$body_mass_g, 
  xlab = "Flipper Length (mm)", ylab = "Body Weight (g)",
  main = "Scatterplot of Flipper Length vs Body Weight",
  col = alpha(ifelse(penguins$species == "Adelie", "darkorange",
    ifelse(penguins$species == "Chinstrap", "darkorchid", "cyan4")), 0.8),
  pch = 19,
  cex = penguins$bill_length_mm / 15,
  
  )

# Add gridlines
grid()


# Add legend for species
legend("topright", legend = levels(penguins$species), 
       col = c("darkorange", "darkorchid", "cyan4"), pch = 19)