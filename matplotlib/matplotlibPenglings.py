# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 15:26:06 2024

Matplotlib version of Penglings plot

@author: samda
"""
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("penglings.csv")

flipper_length = data['flipper_length_mm']
body_mass = data['body_mass_g']
size = data['bill_length_mm']
species = data['species']

circle_size = []
species_color = []

for i in range(len(species)):
    circle_size.append((size[i]**3)/500)
    
    if species[i] == "Adelie":
        species_color.append('blue')
    elif species[i] == "Gentoo":
        species_color.append('red')
    elif species[i] == "Chinstrap":
        species_color.append('purple')

plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (g)")

plt.scatter(flipper_length, body_mass, s=circle_size, c=species_color, alpha=0.65, linewidth=0)

plt.show()