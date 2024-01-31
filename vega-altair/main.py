import altair as alt
import pandas as pd

# use pandas to read the csv
data = pd.read_csv('penglings.csv')

# make chart
chart = alt.Chart(data).mark_circle().encode(
    x=alt.X('flipper_length_mm', title='Flipper Length (mm)', scale=alt.Scale(domain=[170, 240])),
    y=alt.Y('body_mass_g', title='Body Mass (g)', scale=alt.Scale(domain=[2500, 6500])),
    color='species',
    size=alt.Size('bill_length_mm', scale=alt.Scale(domain=[35, 51], range=[20, 200]))
).configure_range(
    # kinda hacky because we just assume it will pick the right species order but it works
    category={'scheme': ["#ff8c00", "#8f20b6", "#008b8b"] }
)

# save chart
chart.save('chart.html', embed_options={'renderer':'svg'})

# save as png as an extra way to view. note this requires installing an extra package
chart.save('chartpng.png')
