import pandas as pd
import matplotlib.pyplot as plt
import mplcursors
from matplotlib.colors import ListedColormap

# read data from csv file
df = pd.read_csv('data/penglings.csv')

# get data from csv
x = df['flipper_length_mm']
y = df['body_mass_g']
sizes = df['bill_length_mm']
species = df['species']

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_axisbelow(True)
plt.grid()
ax.set_facecolor("#EBEBEB")


# map species to colors
species_colors = {
    'Adelie': '#FF8D07',
    'Chinstrap': '#9A35CC',
    'Gentoo': '#088B8C'
}

colors = [species_colors[sp] for sp in species]
# build scatter plot
scatter = plt.scatter(x, y, s=sizes, c=colors, alpha=0.8)


# add labels and title
plt.title('Species of Penguins by Flipper Length, Body Mass and Bill Length')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (g)')
plt.xticks([170, 180, 190, 200, 210, 220, 230])
plt.yticks([3000, 4000, 5000, 6000])

#add tooltip
tooltip = mplcursors.cursor(scatter, hover=True)
tooltip.connect("add", lambda sel: sel.annotation.set_text(
    f"Species: {species[sel.target.index]}\n"
    f"Flipper Length: {x[sel.target.index]} mm\n"
    f"Body Mass: {y[sel.target.index]} g\n"
    f"Bill Length: {sizes[sel.target.index]} mm"
))

#add accessibility alternative text

# Show plot
plt.show()