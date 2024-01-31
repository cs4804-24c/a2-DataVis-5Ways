import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# use pandas to read the csv
data = pd.read_csv('penglings.csv')

# get the R-like background grid
sns.set_theme(style="darkgrid")

# set the figure size to get a nice aspect ratio
plt.figure(figsize=(11, 8))

# make the plot (one line!)
plot = sns.scatterplot(data=data, x="flipper_length_mm", y="body_mass_g", size="bill_length_mm", sizes=(30, 300), hue='species', edgecolors="black", palette=dict(Adelie="#ff8c00bb", Chinstrap="#8f20b6bb", Gentoo="#008b8bbb"))

# move the legend to a better spot
box = plot.get_position()
plot.set_position([box.x0, box.y0, box.width * 0.9, box.height])
plot.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plot.set(xlabel='Flipper Length (mm)', ylabel='Body Mass (g)')
plt.savefig('chartpng.png')
