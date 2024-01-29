import altair
import pandas as pd

altair.renderers.enable('mimetype')

data = pd.read_csv("../penglings.csv")
chart = altair.Chart(data).mark_point(filled=True).encode(
    x=altair.X('flipper_length_mm',scale=altair.Scale(domain=[160,240])),
    y=altair.Y('body_mass_g',scale=altair.Scale(domain=[2500,6500])),
    color=altair.Color('species',scale=altair.Scale(range=["#ff8c02", "#9a34ca", "#158f8f"])),
    size='bill_length_mm',
    opacity=altair.value(0.6)
)

chart.show()