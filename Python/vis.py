import matplotlib.pyplot as plt
import pandas

df = pandas.read_csv("penglings.csv")
df = df.dropna()

fig, ax = plt.subplots()

adelie = df.loc[df["species"] == "Adelie"]
ax.scatter(x=adelie["flipper_length_mm"], y=adelie["body_mass_g"], s=adelie["bill_length_mm"] * 1.5, c="#fda246", alpha=0.8)

chinstrap = df.loc[df["species"] == "Chinstrap"]
ax.scatter(x=chinstrap["flipper_length_mm"], y=chinstrap["body_mass_g"], s=chinstrap["bill_length_mm"] * 1.5, c="#ac5ad4", alpha=0.8)

gentoo = df.loc[df["species"] == "Gentoo"]
ax.scatter(x=gentoo["flipper_length_mm"], y=gentoo["body_mass_g"], s=gentoo["bill_length_mm"] * 1.5, c="#49a1a1", alpha=0.8)

ax.legend(["Adelie", "Chinstrap", "Gentoo"])
ax.set_xlabel("Flipper Length (mm)")
ax.set_ylabel("Body Mass (g)")
plt.show()
