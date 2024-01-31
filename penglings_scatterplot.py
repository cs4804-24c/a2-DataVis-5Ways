import pandas as pd
import matplotlib.pyplot as plt

#Load the data
data = pd.read_csv('./penglings.csv')

#Define color
species_color = {
    'Adelie': 'darkorange',
    'Chinstrap': 'purple',
    'Gentoo': 'lightblue'
}

plt.figure(figsize=(10,6))
for species, group in data.groupby('species'):
    plt.scatter(group['flipper_length_mm'], group['body_mass_g'], s=group['bill_length_mm']*2, alpha = 0.8,label=species, color=species_color[species])

plt.legend(title = 'Species')

plt.xlim(data['flipper_length_mm'].min() * 0.95, data['flipper_length_mm'].max() * 1.05)
plt.ylim(data['body_mass_g'].min() * 0.95, data['body_mass_g'].max() * 1.05)

plt.xlabel('Flipper Length in (mm)')
plt.ylabel('Body mass in (g)')
plt.xticks(range(int(data['flipper_length_mm'].min() * 0.95), int(data['flipper_length_mm'].max() * 1.05), 10))
plt.yticks(range(int(data['body_mass_g'].min() * 0.95), int(data['body_mass_g'].max() * 1.05), 500))

plt.show()