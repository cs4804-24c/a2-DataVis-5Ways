import altair as alt
import pandas as pd

# Load the dataset
data = pd.read_csv("penglings.csv")

# Set up color scale based on species
custom_colors = ["#f0a658", "#609fa0", "#a15ece"]
color_scale = alt.Scale(domain=list(data['species'].unique()), range=custom_colors)

# made with the help of ChatGPT
# Create the scatter plot
scatter_plot = alt.Chart(data).mark_circle(opacity=0.8).encode(
    x=alt.X('flipper_length_mm:Q', scale=alt.Scale(zero=False)),
    y=alt.Y('body_mass_g:Q', scale=alt.Scale(zero=False)),
    size=alt.Size('bill_length_mm:Q', scale=alt.Scale(range=[0, 400]), title='Bill Length (mm)'),
    color=alt.Color('species:N', scale=color_scale, title='Species')
).properties(
    width=800,
    height=500
)

# Add x-axis label
x_axis_label = alt.Chart(pd.DataFrame()).mark_text(
).encode(
    x='x:O',
    y=alt.value(550)
)

# Add y-axis label
y_axis_label = alt.Chart(pd.DataFrame()).mark_text(
    angle= 90 
).encode(
    x=alt.value(-200),
    y='y:O'
)

# Combine all charts
final_chart = (scatter_plot + x_axis_label + y_axis_label).configure_axis(
    labelFontSize=12,
    titleFontSize=14
)

final_chart.save("altair_plot.html")
