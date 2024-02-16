import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('penglings.csv')

# Create a dictionary for colors
colors = {'Adelie': 'orange', 'Chinstrap': 'purple', 'Gentoo': 'teal'}

# Create a scatter plot
for species in df['species'].unique():
    species_df = df[df['species'] == species]
    plt.scatter(species_df['flipper_length_mm'], species_df['body_mass_g'], 
                c=colors[species], label=species, 
                s=species_df['bill_length_mm']*4,  # size of points represent 'Bill Length (mm)'
                alpha=0.7)

# Add labels and title
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (g)')
plt.title('Nadav Konstantine Cs4804 A2 MattPlotLib')

plt.grid()
plt.legend()

# Show the plot
plt.show()
