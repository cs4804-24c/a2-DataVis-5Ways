import altair as alt
import pandas as pd

df = pd.read_csv("penglings.csv")

# Altair Chart
chart = alt.Chart(df, title="Penglings").mark_point().encode(
    x='flipper_length_mm:Q',
    y='body_mass_g:Q',
    color='species:N',
    size='bill_length_mm:Q',
    shape='island:N',
    tooltip=['species:N', 'bill_length_mm:Q']
).interactive()

# Manually rescale axies
chart.encoding.x.scale = alt.Scale(domain=[160, 240])
chart.encoding.y.scale = alt.Scale(domain=[2300, 6700])

# Scale chart to the size of the container
chart = chart.properties(
    width='container'
)

# Needs other special libraries imported to save in a format other than HTML
chart.save("altair_vis.html") 