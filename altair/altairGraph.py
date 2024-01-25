import altair as alt
import csv
import pandas as pd
#Imports csv file
pen = pd.read_csv('penglings.csv')
print(pen)

# Source Used
#https://altair-viz.github.io/gallery/scatter_tooltips.html

chart = alt.Chart(pen).mark_point(clip=True).encode(
    x = alt.X('flipper_length_mm:Q', scale=alt.Scale(domain=[170,232])),#'flipper_length_mm',
    y = alt.Y('body_mass_g:Q', scale=alt.Scale(domain=[2500,6500])),#'body_mass_g',
    color = 'species',
    size='bill_length_mm',
    shape='island',
    tooltip=[
        alt.Tooltip('flipper_length_mm'),
        alt.Tooltip('body_mass_g'),
        alt.Tooltip('species'),
        alt.Tooltip('island'),
        alt.Tooltip('sex'),
        alt.Tooltip('year')
    ]
    ).properties(
        width = 1000,
        height= 500
    ).configure_point(
        filled=True
    )

chart.save('altairGraph.html')