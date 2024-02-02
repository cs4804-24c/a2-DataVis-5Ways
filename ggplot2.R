# Install and load required packages if not already installed
if (!requireNamespace("ggplot2", quietly = TRUE)) {
  install.packages("ggplot2")
}

if (!requireNamespace("readr", quietly = TRUE)) {
  install.packages("readr")
}

# Load required packages
library(ggplot2)
library(readr)

# made with the help of ChatGPT

# Read the CSV data
dataset <- read_csv("penglings.csv")

# Set up custom colors based on species
customColors <- c("#f0a658", "#a15ece", "#609fa0")

# Create the plot using ggplot2
ggplot(dataset, aes(x = flipper_length_mm, y = body_mass_g, color = species)) +
  geom_point(size = dataset$bill_length_mm / 5, alpha = 0.8) +
  scale_color_manual(values = customColors) +
  labs(
    title = "Data Visualization with ggplot2",
    x = "Flipper Length (mm)",
    y = "Body Mass (g)"
  ) +
  theme_minimal()
