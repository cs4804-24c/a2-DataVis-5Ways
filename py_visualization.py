import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

penglings_data = '/mnt/data/penglings.csv'
fig, ax = plt.subplots(figsize=(10, 6))

color_dict = dict({'Adelie':'blue', 'Chinstrap':'green', 'Gentoo':'red'})
scatter = ax.scatter(penglings_data['flipper_length_mm'],
                     penglings_data['body_mass_g'],
                     alpha=0.8,
                     c=penglings_data['species'].map(color_dict),
                     s=penglings_data['bill_length_mm'])

ax.set_title('Penguin Size Metrics by Species', fontsize=14)
ax.set_xlabel('Flipper Length (mm)', fontsize=12)
ax.set_ylabel('Body Mass (g)', fontsize=12)
ax.grid(True)

legend_elements = [Line2D([0], [0], marker='o', color='w', label='Adelie',
                          markerfacecolor='blue', markersize=10),
                   Line2D([0], [0], marker='o', color='w', label='Chinstrap',
                          markerfacecolor='green', markersize=10),
                   Line2D([0], [0], marker='o', color='w', label='Gentoo',
                          markerfacecolor='red', markersize=10)]
ax.legend(handles=legend_elements, loc='upper right')

plt.show()
