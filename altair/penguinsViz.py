import altair as alt
import pandas as pd
import altair_viewer

#example usages taken from documentation https://pypi.org/project/altair/

# load a simple dataset as a pandas DataFrame
pengs = pd.read_csv("/home/taya/a2-DataVis-5Ways-yakovenko/penglings.csv")
print(pengs.columns.tolist())

chart = alt.Chart(pengs).mark_point().encode(
    x='flipper_length_mm',
    y='body_mass_g',
)
chart.show()