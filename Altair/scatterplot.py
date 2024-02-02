import altair as alt
import pandas as pd

# Load the penguins dataset
url = 'https://raw.githubusercontent.com/Rob-hub-lang/a2-DataVis-5Ways/main/penglings.csv'
df = pd.read_csv(url)

# Define custom colors for each species
species_colors = {'Adelie': 'darkorange', 'Chinstrap': 'darkorchid', 'Gentoo': 'darkgreen'}

# Create scatter plot
scatter_plot = alt.Chart(df).mark_circle(opacity=0.8).encode(
    x=alt.X('flipper_length_mm:Q', scale=alt.Scale(zero=False)),
    y=alt.Y('body_mass_g:Q', scale=alt.Scale(zero=False)),
    color=alt.Color('species:N', scale=alt.Scale(domain=list(species_colors.keys()), range=list(species_colors.values()))),
    size=alt.Size('bill_length_mm:Q'),
    tooltip=['species:N', 'flipper_length_mm:Q', 'body_mass_g:Q', 'bill_length_mm:Q']
).properties(
    width=800,
    height=500
)

# Add axes with ticks and labels
x_axis = alt.Axis(title='Flipper Length (mm)')
y_axis = alt.Axis(title='Body Mass (g)')
scatter_plot = scatter_plot.configure_axis(
    labelFontSize=12,
    titleFontSize=14,
    tickCount=10
).encode(
    x=alt.X('flipper_length_mm:Q', scale=alt.Scale(zero=False), axis=x_axis),
    y=alt.Y('body_mass_g:Q', scale=alt.Scale(zero=False), axis=y_axis)
)

# Display the plot
scatter_plot.save('scatter_plot.html')
