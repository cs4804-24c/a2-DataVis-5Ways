import altair as alt
import pandas as pd

file_path = 'https://raw.githubusercontent.com/cs4804-24c/a2-DataVis-5Ways/main/penglings.csv'
penglings = pd.read_csv(file_path)

chart_width = 900
chart_height = 600

x_field = 'flipper_length_mm'
y_field = 'body_mass_g'

x_range = [160, 240]
y_range = [3000, 6000]

chart = alt.Chart(penglings).mark_circle(size=60).encode(
    x=alt.X(x_field, scale=alt.Scale(domain=x_range)),
    y=alt.Y(y_field, scale=alt.Scale(domain=y_range)),
    color = alt.Color('species', title = 'Species', scale = alt. Scale(domain = ['Adelie', 'Chinstrap', 'Gentoo'], range = ['orange', 'purple', 'teal'])),
    size = alt.Size('bill_length_mm', title = 'Bill Length (mm)'),
    tooltip=['species', 'flipper_length_mm', 'body_mass_g']
).properties(
    width=chart_width,
    height=chart_height
).interactive()

chart.save('Altair/altair_chart.html')