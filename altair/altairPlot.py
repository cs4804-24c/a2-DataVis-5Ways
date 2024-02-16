import altair as alt
import pandas as pd

# Load the data
data = pd.read_csv('penglings.csv')

# Define a custom color scheme
color_scheme = alt.Scale(domain=['Adelie', 'Chinstrap', 'Gentoo'],
                         range=['orange', 'purple', 'teal'])

# Create the chart
chart = alt.Chart(data).mark_circle().encode(
    alt.X('flipper_length_mm:Q', title='Flipper Length (mm)', scale=alt.Scale(domain=(170, 235))),
    alt.Y('body_mass_g:Q', title='Body Mass (g)', scale=alt.Scale(domain=(2500, 6500))),
    alt.Color('species:N', scale=color_scheme),
    alt.Size('bill_length_mm:Q')
).properties(
    title='Nadav Konstantine CS4804 A2 Altair',
    width=600,  # Adjust the width of the plot
    height=400  # Adjust the height of the plot
)

# Save the chart
chart.save('altairPlot.html')