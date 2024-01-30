import pandas as pd
import plotly.express as px

penglings_data_path = '/mnt/data/penglings.csv'
penglings_df = pd.read_csv(penglings_data_path)

cleaned_penglings_df = penglings_df.dropna(subset=['bill_length_mm', 'flipper_length_mm', 'body_mass_g'])

fig = px.scatter(
    cleaned_penglings_df,
    x='flipper_length_mm',
    y='body_mass_g',
    color='species',
    size='bill_length_mm',
    opacity=0.8,
    title='Scatterplot of Penguin Size Metrics',
    labels={
        'flipper_length_mm': 'Flipper Length (mm)',
        'body_mass_g': 'Body Mass (g)',
        'bill_length_mm': 'Bill Length (mm)'
    }
)

fig.update_layout(
    xaxis=dict(tick0=170, dtick=10),
    yaxis=dict(tick0=3000, dtick=500)
)

plot_file_path = '/mnt/data/penguin_scatter_plot.html'
fig.write_html(plot_file_path)

