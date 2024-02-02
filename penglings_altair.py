import altair as alt
import pandas as pd

data = pd.read_csv("penglings.csv")

domain = ['Adelie', 'Chinstrap', 'Gentoo']
range_ = ['darkorange', 'purple', 'blue']

size_scale = alt.Scale(domain=[data['bill_length_mm'].min(), data['bill_length_mm'].max()],
                       range=[30, 300])

chart = alt.Chart(data).mark_point(opacity=0.8).encode(
    x=alt.X('flipper_length_mm:Q', scale=alt.Scale(zero=False)),
    y=alt.Y('body_mass_g:Q', scale=alt.Scale(zero=False)),
    color=alt.Color('species:N', scale=alt.Scale(domain=domain, range=range_)),
    size=alt.Size('bill_length_mm:Q', scale=size_scale)
).properties(
    title='Penguin Species Scatterplot',
    width=600,
    height=400,
    background='white'
).configure_view(
    strokeWidth=0,
)

chart.save("pengling_altair.html")