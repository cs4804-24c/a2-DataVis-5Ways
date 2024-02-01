import altair as alt
import pandas as pd

data = pd.read_csv("penglings.csv")

size_scale = alt.Scale(domain=(data['bill_length_mm'].min(), data['bill_length_mm'].max()),
                       range=(10, 1000))

chart = alt.Chart(data).mark_point(opacity=0.8).encode(
    alt.X('flipper_length_mm:Q', scale=alt.Scale(zero=False)),
    alt.Y('body_mass_g:Q', scale=alt.Scale(zero=False)),
    color='species:N',
    size= alt.Size('bill_length_mm:Q',  scale=size_scale)
).properties(
    title='Penguin Species Scatterplot',
    width=600,
    height=400,
    background='white'
).configure_axis(
    grid=False
).configure_view(
    strokeWidth=0,
)

chart.save("pengling_altair.html")