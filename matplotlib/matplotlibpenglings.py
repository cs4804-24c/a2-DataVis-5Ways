import pandas as pd
import matplotlib.pyplot as plt

csvFile = pd.read_csv('penglings.csv').dropna()
colors = {
    'Adelie': '#f8a452',
    'Gentoo': '#4ea0a1',
    'Chinstrap': '#b056cf'
}

species = csvFile.groupby('species')
for name,i in species:
    plt.scatter(i.flipper_length_mm,i.body_mass_g,s=i.bill_length_mm, alpha=0.75, label=name, color=colors[name])

plt.grid()
plt.legend(loc='lower right')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (g)')
plt.savefig('matplotliboutput.png')
plt.show()