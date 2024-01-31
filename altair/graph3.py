import altair as alt
import pandas as pd

df = pd.read_csv("..\penglings.csv")

plot = alt.Chart(df).mark_circle().encode(
    x=alt.X('flipper_length_mm', scale=alt.Scale(domain=[170, 235])),
    y=alt.Y('body_mass_g', scale=alt.Scale(domain=[2500, 6500])),
    color='species',
    size='bill_length_mm',
    tooltip=['species', 'island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex', 'year']
).configure(background='#d3d3d3'
).configure_range(
    category=["#FF8C01", "#9933CB", "#128E8E"]
).properties(
    width=575,
    height=450
)

plot.save('output.html')
