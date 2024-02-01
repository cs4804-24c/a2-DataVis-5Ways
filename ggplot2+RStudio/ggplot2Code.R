library(ggplot2)
library(plotly)
library(readr)
penglings <- read_csv("Downloads/penglings.csv")
View(penglings)

p <- ggplot(penglings, aes(x = flipper_length_mm, y = body_mass_g)) +
geom_point(aes(color = species,
               shape = species, 
               size = bill_length_mm),
               alpha=0.8)

ggplotly(p + labs(y = "Body Mass (g)", x = "Flipper Length (mm)"))
