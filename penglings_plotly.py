import plotly.express as px
import pandas as pd

df = pd.read_csv('penglings.csv')

df['bill_length_mm'] = df['bill_length_mm'].fillna(df['bill_length_mm'].mean())


color_map = {
    "Adelie": "orange",
    "Chinstrap": "darkorchid",
    "Gentoo": "seagreen"
}


fig = px.scatter(df, x='flipper_length_mm', y='body_mass_g',
                 color='species', size='bill_length_mm',
                 hover_data=['species'],
                 color_discrete_map=color_map)

fig.show()
