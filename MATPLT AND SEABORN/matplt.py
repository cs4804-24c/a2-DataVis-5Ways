import seaborn as seaborn
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('penglings.csv')

seaborn.set_theme(style="whitegrid")

seaborn.relplot(x="flipper_length_mm", 
                y="body_mass_g", 
                hue="species", 
                size="bill_length_mm",
                sizes=(50, 100), 
                alpha=0.8, 
                palette=["darkorange", "cyan", "purple",],
                height=4, 
                data=df)


plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (g)")

plt.show()
