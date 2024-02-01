import altair as alt
# from vega_datasets import data
url = '../penglings.csv'

#Idea: show transition of penguin species over time

options = ['Adelie', 'Chinstrap', 'Gentoo']
labels = [option + ' ' for option in options]

input_dropdown = alt.binding_radio(
    options=options + [None],
    labels=labels + ['All'],
    name='Species of penguin: ' 
)

selection = alt.selection_point(
    fields=['species'],
    bind=input_dropdown,
)

time_interval_selector = alt.selection_interval(encodings=['x'], name='year')

chart = alt.Chart(url).transform_calculate(

    url='https://www.google.com/search?q=' + alt.datum.species + '+penguin',

).mark_circle().encode(
    # set x-axis scale limits
    x=alt.X('flipper_length_mm:Q', scale=alt.Scale(domain=(170, 235)), axis=alt.Axis(title='Flipper Length (mm)')),
    y=alt.Y('body_mass_g:Q', scale=alt.Scale(domain=(2500, 6500)), axis=alt.Axis(title='Body Mass (g)')),
    # size porportional to bill_length_mm
    size=alt.Size('bill_length_mm:Q', scale=alt.Scale(range=[10, 200], domain=[30, 55]), title='Bill Length (mm)'),
    # color corresponds to species
    color=alt.Color('species:N', title="Sepcies").scale(domain=options, range=['#ff8d05', '#9934cc', '#048b8c']),
    tooltip=['species:N', 'bill_length_mm:Q', 'body_mass_g:Q', 'flipper_length_mm:Q'],
    href='url:N',
).interactive().add_params(
    selection,
    # slider_selection
).transform_filter(
    selection
).transform_filter(
    time_interval_selector
).properties(
    width=600,
    height=400
)

timeline = alt.Chart(url).mark_line().encode(
    x=alt.X('year:O', axis=alt.Axis(title='Year')),
    y='count()',
).properties(
    height=50,
    width=400
).add_params(
    time_interval_selector
)

chart = alt.vconcat(chart, timeline)

chart.save('chart.html')

