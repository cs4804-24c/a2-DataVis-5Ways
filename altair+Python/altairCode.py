# sources
# https://altair-viz.github.io/user_guide/saving_charts.html
# https://altair-viz.github.io/user_guide/encodings/index.html


import altair as alt
import pandas as pd

df = pd.read_csv("penglings.csv")
print(df)
chart = (alt.Chart(df).mark_point().encode(
    alt.X('flipper_length_mm', scale=alt.Scale(domain=(170, 240))).axis(title="Flipper Length (mm)"),
    alt.Y('body_mass_g', scale=alt.Scale(domain=(2500, 6500))).axis(title="Body Mass (g)"),
    shape='species',
    size='bill_length_mm',
    color='species',
    tooltip=["species", "island", "bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g", "sex", "year"]
    ).properties(
        width=800,
        height=800
    ).configure_mark(
        opacity=0.8
    ).interactive())

chart.save('A2AltairChart.html', embed_options={'renderer': 'svg'})
