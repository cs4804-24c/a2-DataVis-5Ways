import altair as alt
import pandas as pd

data = pd.read_csv(r'E:\IdeaProjects\Altair_method\penglings.csv') # replace this path to your path

data_clean = data.dropna(subset=['flipper_length_mm', 'body_mass_g', 'bill_length_mm'])

domain = ['Adelie', 'Chinstrap', 'Gentoo']
range_ = ['orange', 'purple', 'teal']

scatter_chart = alt.Chart(data_clean).mark_circle(opacity=0.8).encode(
    alt.X('flipper_length_mm:Q', title='Flipper Length (mm)', scale=alt.Scale(domain=[170, data_clean['flipper_length_mm'].max()])),
    alt.Y('body_mass_g:Q', title='Body Mass (g)', scale=alt.Scale(domain=[2000, data_clean['body_mass_g'].max()])),
    color=alt.Color('species:N', scale=alt.Scale(domain=domain, range=range_), legend=alt.Legend(title='Species')),
    size=alt.Size('bill_length_mm:Q', title='Bill Length (mm)'),
    tooltip=['species', 'island', 'flipper_length_mm', 'body_mass_g', 'bill_length_mm']
).properties(
    title='Penguin Scatterplot',
    width=800,
    height=500
)

scatter_chart.save('penguin_scatterplot.html')

scatter_chart
