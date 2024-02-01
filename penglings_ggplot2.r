# Set a CRAN mirror
options(repos = c(CRAN = "https://cloud.r-project.org"))

library(ggplot2)
library(readr)

#load penglings.csv
penglings <- read_csv("penglings.csv")

#scatter plot
result <- ggplot(penglings, aes(x = flipper_length_mm, y = body_mass_g)) + geom_point(aes(color = species, size = bill_length_mm), alpha = 0.8) +
    scale_color_manual(values=c("Adelie" = "darkorange", "Chinstrap" = "darkorchid", "Gentoo" = "cyan4")) +
    labs(x= "Flipper Length (mm)", y = "Body Mass (g)") +
    theme_light(base_size = 16) +  # Using theme_light for a white background
  theme(
    legend.title = element_blank(),
    panel.grid.major = element_blank(),  # Remove major grid lines
    panel.grid.minor = element_blank(),  # Remove minor grid lines
    panel.background = element_rect(fill = "white", colour = "white")  # Set background to white
  )

ggsave("penglings_r_scatter.png", plot = result, width = 10, height=5, dpi = 300)