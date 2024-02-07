import altair as alt
import pandas as pd

data = pd.read_csv('C:/Users/joshj/Downloads/a2-DataVis-5Ways-main/penglings.csv')

scatter_plot = alt.Chart(data).mark_circle().encode(
    x='flipper_length_mm',
    y='body_mass_g',
    size='bill_length_mm',
    color='species',
    tooltip=['species', 'flipper_length_mm', 'body_mass_g', 'bill_length_mm']
).interactive()

scatter_plot
