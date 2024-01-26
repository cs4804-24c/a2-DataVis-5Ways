import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV file
data = pd.read_csv("./penglings.csv")

# Map species to color
dot_colors = {
  "Adelie": "#FBA044",
  "Chinstrap": "#AA58D2",
  "Gentoo": "#479F9F"
}

plt.figure(figsize=(12, 8))

bill_length_mean = data["bill_length_mm"].mean()

plt.scatter(data["flipper_length_mm"], data["body_mass_g"], c=data["species"].map(dot_colors), s=((data["bill_length_mm"] - data["bill_length_mm"].min())) * 10, alpha=0.6, edgecolors=data["species"].map(dot_colors), linewidths=1)
plt.xlabel("Flipper Length (mm)", color="#5B5B5B")
plt.ylabel("Body Mass (g)", color="#5B5B5B")
plt.title("Scatterplot of Flipper Length vs. Body Mass")

# Set the tick color to #5B5B5B
plt.tick_params(axis='x', colors="#5B5B5B")
plt.tick_params(axis='y', colors="#5B5B5B")

# Add legend for species colors
species_legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label='Adelie', markerfacecolor='#FBA044', markersize=10),
                          plt.Line2D([0], [0], marker='o', color='w', label='Chinstrap', markerfacecolor='#AA58D2', markersize=10),
                          plt.Line2D([0], [0], marker='o', color='w', label='Gentoo', markerfacecolor='#479F9F', markersize=10)]

plt.legend(handles=species_legend_elements, loc='upper left', title='Species')

# Add a background grid
plt.grid(True, linestyle='--', linewidth=0.5, color='#DEDEDE')

plt.show()