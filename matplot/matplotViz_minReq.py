import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
#scatter plot example https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_demo2.html#sphx-glr-gallery-lines-bars-and-markers-scatter-demo2-py

# Load the data from the CSV file into a DataFrame
df = pd.read_csv('/home/taya/a2-DataVis-5Ways-yakovenko/penglings.csv').dropna()

#add a column for colours based on species
# Define label mapping dictionary
color_mapping = {
    'Adelie': 'red',
    'Gentoo': 'blue',
    'Chinstrap': 'green'
}

# Apply the mapping to create the new 'label' column
#df['colour_species'] = df['species'].map(color_mapping)
print(df.columns.tolist())


# Create scatter plot
scatter = plt.scatter(df['flipper_length_mm'], df['body_mass_g'], c=df['species'].map(color_mapping),
                      s=df['bill_length_mm']*5, alpha=0.5)

# Add labels and title
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (g)')
plt.title('Flipper Length vs. Body Mass')

# Create custom legend
legend_elements = [
    mpatches.Patch(facecolor=color, edgecolor='black', label=label) for label, color in color_mapping.items()
]
legend_elements.append(mpatches.Circle((0, 0), 50, facecolor='black', alpha=0.5, label='Largest Dot (50.0 mm)'))
legend_elements.append(mpatches.Circle((0, 0), 0.1, facecolor='black', alpha=0.5, label='Smallest Dot (39.1 mm)'))

plt.legend(handles=legend_elements, loc='center left', bbox_to_anchor=(1, 0.5))

# Show plot
plt.grid(True)
plt.show()


