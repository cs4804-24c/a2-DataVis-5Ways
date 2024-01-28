# Load the lib
library(ggplot2)

# Read and load data
df <- read.csv("https://raw.githubusercontent.com/cs4804-24c/a2-DataVis-5Ways/main/penglings.csv")
df <- na.omit(df)

# Generate the scatter plot with ggplot2
p <- ggplot(df, aes(x = flipper_length_mm, y = body_mass_g, color = species, size = bill_length_mm)) +
  geom_point(alpha = 0.7) +
  scale_color_manual(values = c("darkorange","darkorchid","cyan4")) +
  labs(x = "Flipper Length (mm)", y = "Body Mass (g)", size = "Bill Length (mm)", color = "Species") +
  theme_minimal()

print(p)

ggsave("ggplot2/ggplot2.png", plot = p, width = 10, height = 6, dpi = 300)
