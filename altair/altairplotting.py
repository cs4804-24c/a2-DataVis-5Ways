import altair as alt
import pandas as pd

csvFile = pd.read_csv('penglings.csv')

graph = alt.Chart(csvFile).mark_circle().encode(
    x=alt.X('flipper_length_mm', axis=alt.Axis(tickMinStep=10), scale=alt.Scale(domain=(170,240)), title='Flipper Length (mm)'),
    y=alt.Y('body_mass_g', axis=alt.Axis(tickMinStep=500), scale=alt.Scale(domain=(2500,6500)), title='Body Mass (g)'),
    color='species',
    size=alt.Size('bill_length_mm', 
        scale=alt.Scale(domain=[csvFile.bill_length_mm.min(), csvFile.bill_length_mm.max()], range=[20,120]))
).configure_mark(
    opacity=0.8,
)

graph.save('test.html')