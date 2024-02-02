import altair as alt
import pandas as pd

data = pd.read_csv("penglings.csv")
chart = alt.Chart(data).mark_point(filled=True).encode(
    x=alt.X('flipper_length_mm',scale=alt.Scale(domain=[170,240])),
    y=alt.Y('body_mass_g',scale=alt.Scale(domain=[2500,6500])),
    color=alt.Color('species',scale=alt.Scale(range=["#fa8f37", "#983bc8", "#3e9392"])),
    size='bill_length_mm',
    opacity=alt.value(0.8)
).properties(
    width = 500,
    height = 400
)

chart.save('altairchart.html')