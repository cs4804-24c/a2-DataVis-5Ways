import altair as alt
# from vega_datasets import data
url = '../penglings.csv'

chart = alt.Chart(url).mark_circle().encode(
    # set x-axis scale limits
    x=alt.X('flipper_length_mm:Q', scale=alt.Scale(domain=(170, 235))),
    y=alt.Y('body_mass_g:Q', scale=alt.Scale(domain=(2500, 6500))),
    # radius porportional to bill_length_mm
    size=alt.Size('bill_length_mm:Q', scale=alt.Scale(range=[10, 200], domain=[30, 55])),
    # color corresponds to species
    color='species:N',
    # set point to be filled circle
    fill='species:N'
)


chart.save('chart.html')

