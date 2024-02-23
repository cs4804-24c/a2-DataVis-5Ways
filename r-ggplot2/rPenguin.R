library(ggplot2)

penData <- read.csv("penglings.csv", header = TRUE, sep = ",")

plot <- ggplot(penData, aes(x = flipper_length_mm, y = body_mass_g), ) + 
  geom_point(aes(color = species, size = bill_length_mm, shape = island), alpha=0.7) +
  scale_color_manual(values = c("#4fb8b6", "#343483","#383b47")) +
  labs(
    title = "Penguin Flipper Length(mm) vs Body Mass(g)",
    x="Flipper Length (mm)",
    y="Body Mass (g)"
  ) +
  theme(
    plot.title = element_text(family = "Times New Roman", size = 16, face = "bold"),
    axis.title = element_text(family = "Times New Roman", size = 13),
    axis.text = element_text(family = "Times New Roman", size = 11),
    legend.text = element_text(family = "Times New Roman", size = 11),
    legend.title = element_text(family = "Times New Roman", size = 13)
  )

plot

