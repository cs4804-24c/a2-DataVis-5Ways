import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import pandas

df = pandas.read_csv("penglings.csv")
df = df.dropna()

fig, ax = plt.subplots()

ax.set_axisbelow(True)
ax.minorticks_on()
ax.grid(visible=True, axis="both", which="major", color="#DDDDDD", linewidth=0.8)
ax.grid(visible=True, axis="both", which="minor", color="#EEEEEE", linewidth=0.5)

adelie = df.loc[df["species"] == "Adelie"]
ax.scatter(x=adelie["flipper_length_mm"], y=adelie["body_mass_g"], s=adelie["bill_length_mm"] * 5, c="#fda246", alpha=0.8)

chinstrap = df.loc[df["species"] == "Chinstrap"]
ax.scatter(x=chinstrap["flipper_length_mm"], y=chinstrap["body_mass_g"], s=chinstrap["bill_length_mm"] * 5, c="#ac5ad4", alpha=0.8)

gentoo = df.loc[df["species"] == "Gentoo"]
ax.scatter(x=gentoo["flipper_length_mm"], y=gentoo["body_mass_g"], s=gentoo["bill_length_mm"] * 5, c="#49a1a1", alpha=0.8)

custom_legend = [
    Line2D([0], [0], marker='o', color='w', markersize=0, label='species'),
    Line2D([0], [0], marker='o', color='w', label='Adelie', markerfacecolor='#fda246', markersize=10),
    Line2D([0], [0], marker='o', color='w', label='Chinstrap', markerfacecolor='#ac5ad4', markersize=10),
    Line2D([0], [0], marker='o', color='w', label='Gentoo', markerfacecolor='#49a1a1', markersize=10),
    Line2D([0], [0], marker='o', color='w', markersize=0, label='bill_length_mm'),
    Line2D([0], [0], marker='o', color='w', label='40', markerfacecolor='#444444', markersize=15),
    Line2D([0], [0], marker='o', color='w', label='50', markerfacecolor='#444444', markersize=17),
]

ax.legend(handles=custom_legend)
ax.set_xlabel("Flipper Length (mm)")
ax.set_ylabel("Body Mass (g)")

plt.show()
