import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("..\penglings.csv")

colors = {'Adelie': '#FF8C01', 'Chinstrap': '#9933CB', 'Gentoo': '#128E8E'}
fig, ax = plt.subplots()

ax.set_facecolor("#d3d3d3")
ax.set_axisbelow(True)

plt.grid(color='white')

plt.scatter(df['flipper_length_mm'], df['body_mass_g'], alpha=0.8, c=df['species'].map(colors), s=df['bill_length_mm']*5)

plt.xlabel("flipper length (mm)")
plt.ylabel("body mass (g)")

plt.show()
