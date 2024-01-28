import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../penglings.csv')

df.head()



sns.scatterplot(x = 'flipper_length_mm', y = 'body_mass_g', hue = 'species', size = 'bill_length_mm', alpha = 0.8, data = df)
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (g)')

plt.savefig('../img/penglins_python.png')
plt.show()
