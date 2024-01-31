import pandas as pd
import matplotlib.pyplot as plt

file_path = r'E:\IdeaProjects\python_method\penglings.csv'
data = pd.read_csv(file_path)

data_clean = data.dropna(subset=['flipper_length_mm', 'body_mass_g', 'bill_length_mm'])

color_mapping = {
    'Adelie': 'orange',
    'Chinstrap': 'purple',
    'Gentoo': 'teal'
}

plt.figure(figsize=(10, 6))

for species, group in data_clean.groupby('species'):
    plt.scatter(
        group['flipper_length_mm'],
        group['body_mass_g'],
        s=group['bill_length_mm'] * 5,
        alpha=0.8,
        label=species,
        color=color_mapping.get(species)
    )

plt.xlim(170, data_clean['flipper_length_mm'].max())
plt.ylim(2000, data_clean['body_mass_g'].max())

plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (g)')
plt.title('Scatter Plot of Penguins')

plt.legend(title='Species')

plt.show()
