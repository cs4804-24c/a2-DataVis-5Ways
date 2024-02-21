import pandas as pd
import altair as alt

# Read the CSV file
data = pd.read_csv('penglings.csv')

# Define colors for each species
color_map = {'Adelie': 'orange', 'Gentoo': 'mediumorchid', 'Chinstrap': 'mediumturquoise'}  # Add more colors if needed

# Create Altair Chart
chart = alt.Chart(data).mark_circle().encode(
    alt.X('flipper_length_mm:Q', sort=alt.SortField(field='flipper_length_mm', order='ascending'), scale=alt.Scale(domain=[169, 235]), axis=alt.Axis(ticks=True)),
    alt.Y('body_mass_g:Q', sort=alt.SortField(field='body_mass_g', order='ascending'), scale=alt.Scale(domain=[2500, 8500]), axis=alt.Axis(ticks=True)),
    color=alt.Color('species', scale=alt.Scale(domain=list(color_map.keys()), range=list(color_map.values()))),
    size='bill_length_mm'
).properties(
    width=600,
    height=400
).configure_axis(
    grid=False
).configure_legend(
    orient='top-right',
    titleFontSize=14,
    labelFontSize=12,
    titleFontWeight='normal',
    labelFontWeight='normal',
    gradientLength=200,
    gradientThickness=30,
    titlePadding=10,
    labelPadding=5,
    symbolStrokeWidth=2,
    symbolSize=100,
    symbolType='circle',
    titleAlign='left',
    titleLimit=0,
    labelLimit=0,
    direction='vertical',
    rowPadding=5,
    columnPadding=5,
    symbolLimit=0,
    symbolOffset=0,
    symbolOpacity=1,
    offset=10
).properties(
    title='Scatter Plot with Species Color and Marker Size'
)

chart.show()
