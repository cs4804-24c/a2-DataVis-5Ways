library(ggplot2)

penglings <- read.csv("C:/Users/joshj/Downloads/a2-DataVis-5Ways-main/penglings.csv")

p <- ggplot(penglings, aes(x = flipper_length_mm, y = body_mass_g, color = species, size = bill_length_mm)) +
  geom_point(alpha = 0.6) + 
  scale_color_manual(values = c("Adelie" = "darkorange", "Gentoo" = "cyan", "Chinstrap" = "purple")) +
  labs(x = "Flipper Length (mm)", y = "Body Mass (g)", color = "Species", size = "Bill Length (mm)") +
  theme_minimal()


ggsave("C:/Users/joshj/Desktop/DataVis5Ways/R/R_Penglings_Image.png", plot = p, width = 10, height = 5, dpi = 300)

