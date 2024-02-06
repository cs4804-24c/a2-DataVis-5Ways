import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
#scatter plot example https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_demo2.html#sphx-glr-gallery-lines-bars-and-markers-scatter-demo2-py
#marker + multiple plot example https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_star_poly.html#sphx-glr-gallery-lines-bars-and-markers-scatter-star-poly-py
#groups https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html


# Load the data from the CSV file into a DataFrame
df = pd.read_csv('/home/taya/a2-DataVis-5Ways-yakovenko/penglings.csv').dropna() #11 fileds contained some exmpty values; wanted to avoid error in viz

#add a column for colours based on species
# Define label mapping dictionary
color_mapping = {
    'Adelie': 'red',
    'Gentoo': 'blue',
    'Chinstrap': 'green'
}
marker_map = {
    'Torgersen': 'o',#point
    'Biscoe': '^',#triangle
    'Dream': 's'#square

}

# Apply the mapping to create the new 'label' column
#df['colour_species'] = df['species'].map(color_mapping)
print(df['island'].unique())


#double check thr grouping here -> need consistent labels and need to make sure that the grid shows up for both of them
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

for ax, (gender, group) in zip(axes, df.groupby('sex')):
    for island, island_group in group.groupby('island'):
        ax.scatter(island_group['flipper_length_mm'], island_group['body_mass_g'],
                    c=island_group['species'].map(color_mapping),
                    s=island_group['bill_length_mm']*10,
                    marker=marker_map[island],
                    alpha=0.5,
                    label=island)
    ax.set_title(f'Scatter Plot of {gender} Penguins')
    ax.set_xlabel('Flipper Length (mm)')
    ax.set_ylabel('Body Mass (g)')


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


