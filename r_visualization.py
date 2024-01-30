import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

plt.figure(figsize=(10, 6))
scatter = sns.scatterplot(
    data = pd.read_csv('penglings.csv'),
    x='flipper_length_mm',
    y='body_mass_g',
    hue='species',
    size='bill_length_mm',
    sizes=(20, 200),
    alpha=0.6
)

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.title('Penguin Size Metrics')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (g)')

plt_file_path = '/mnt/data/penguin_scatterplot.png'
plt.savefig(plt_file_path, bbox_inches='tight')

plt.show()
plt_file_path


