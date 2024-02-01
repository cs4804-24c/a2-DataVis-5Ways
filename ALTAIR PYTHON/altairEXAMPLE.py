import altair as alt
import pandas as pd


df = pd.read_csv('penglings.csv')

x_min, x_max = df['flipper_length_mm'].min(), df['flipper_length_mm'].max()
y_min, y_max = df['body_mass_g'].min(), df['body_mass_g'].max()

domain = ['Adelie', "Gentoo", "Chinstrap"]
range_ = ['orange', 'purple', 'aqua']

alt.Chart(df).mark_point(filled=True).encode(
    alt.X('flipper_length_mm:Q', scale=alt.Scale(domain=[x_min*.95, x_max*1.05])),
    alt.Y('body_mass_g:Q', scale=alt.Scale(domain=[y_min**.95, y_max*1.05])),
    alt.Size('bill_length_mm'),
    alt.Color('species').scale(domain=domain, range=range_),
    alt.OpacityValue(0.8),
    tooltip =[ 
              alt.Tooltip('flipper_length_mm'), 
              alt.Tooltip('body_mass_g'), 
              alt.Tooltip('bill_length_mm')
              ]
).properties(
    width=700,  
    height=700  
).save("penguins_altair.html")