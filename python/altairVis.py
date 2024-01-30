import altair as alt
import pandas as pd

# Load data from the CSV file
df = pd.read_csv('../penglings.csv')

# Create the scatter plot with adjusted scales
scatter_plot = alt.Chart(df).mark_circle(opacity=0.8, stroke='black', strokeWidth=1).encode(
    x=alt.X('flipper_length_mm:Q', axis=alt.Axis(title='Flipper Length (mm)'), scale=alt.Scale(domain=[170, 240])),
    y=alt.Y('body_mass_g:Q', axis=alt.Axis(title='Body Mass (g)'), scale=alt.Scale(domain=[2000, 7000])),
    size=alt.Size('bill_length_mm:Q', title='Bill Length (mm)', scale=alt.Scale(type='linear')),
    color=alt.Color('species:N', scale=alt.Scale(scheme='category10')),
    tooltip=['species:N', 'flipper_length_mm:Q', 'body_mass_g:Q', 'bill_length_mm:Q']
).properties(
    width=600,
    height=400
)

# Save the scatter plot as an HTML file
scatter_plot.save('../img/altair_plot.html')
