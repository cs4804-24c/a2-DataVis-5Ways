import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('penglings.csv')

# Define colors for each species
color_map = {'Adelie': 'orange', 'Gentoo': 'mediumorchid', 'Chinstrap': 'mediumturquoise'}

# Map species to colors
data['color'] = data['species'].map(color_map)

# Define marker size based on bill length
marker_size = data['bill_length_mm'] * 3 # Adjust scaling factor as needed

# Create scatter plot
plt.figure(figsize=(10, 6))
for species, group in data.groupby('species'):
    plt.scatter(group['flipper_length_mm'], group['body_mass_g'], c=group['color'], s=marker_size[group.index], alpha=0.8, label=species)

plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (g)')
plt.title('Scatter Plot with Species Color and Marker Size')
plt.legend(loc='upper right')
plt.grid(False)
plt.show()
