#Import libraries
import pandas as pd
import plotly.express as px

#Read CSV data
df = pd.read_csv('data/penglings.csv')

#Drop any null entries
df = df.dropna(subset=['bill_length_mm'])

#Customize colors of species to match reference
custom_colors = ['#FF8D07', '#088B8C', '#9A35CC']

#Scatter data to chart
fig = px.scatter(df, x='flipper_length_mm', y='body_mass_g', size='bill_length_mm', color='species', color_discrete_sequence=custom_colors, opacity=0.8)

#Label the chart
fig.update_layout(
    title='PENGLINGS!!',
    xaxis_title='Flipper Length (mm)',
    yaxis_title='Body Mass (g)',
    legend_title_text='Species'
)

#Customize tick values
fig.update_xaxes(
    tickvals=[170, 180, 190, 200, 210, 220, 230],
)

fig.update_yaxes(
    tickvals=[3000, 4000, 5000, 6000]
)

#Show the plot
fig.show()