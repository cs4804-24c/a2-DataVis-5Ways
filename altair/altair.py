import altair as alt
import pandas as pd

# Load data
source = pd.read_csv('https://raw.githubusercontent.com/cs4804-24c/a2-DataVis-5Ways/main/penglings.csv')

# axis
scatter_plot = alt.Chart(source).mark_circle().encode(
    x=alt.X('flipper_length_mm:Q', scale=alt.Scale(domain=[170, 250])),
    y=alt.Y('body_mass_g:Q', scale=alt.Scale(domain=[2500, 7000])),
    color='species:N',
    size='bill_length_mm:Q'
)

scatter_plot.display()

