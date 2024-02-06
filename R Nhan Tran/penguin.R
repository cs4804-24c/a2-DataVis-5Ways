library(ggplot2)
library(dplyr)

# The dataset is provided in the gapminder library
library(palmerpenguins)
data <- penguins

# Most basic bubble plot
data %>%
  ggplot(aes(x=flipper_length_mm, y=body_mass_g, size=bill_length_mm, color=species)) +
  geom_point(alpha=0.45) +
  scale_size(range = c(3, 8), name="Population (M)")

