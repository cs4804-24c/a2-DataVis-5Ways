from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv("..\\penglings.csv").dropna()

app = Dash(__name__)

app.layout = html.Div([
    html.H4(children='Interactive Penglings Plot', style={'textAlign':'center'}),
    dcc.Graph(id="scatter-plot", style={'height': '70vh'}),
    html.P("Filter by Bill Length (mm):"),
    dcc.RangeSlider(
        id='range-slider',
        min=32, max=60, step=1,
        marks={32: '32', 35: '35', 40: '40', 45: '45', 50: '50', 55: '55', 60: '60'},
        value=[32, 60]
    ),
])

@app.callback(
    Output("scatter-plot", "figure"), 
    Input("range-slider", "value")
)
def update_graph(slider_range):
    # Filter data entries
    low, high = slider_range
    mask = (df['bill_length_mm'] > low) & (df['bill_length_mm'] < high)

    # Scatterplot
    fig = px.scatter(
        df[mask], 
        x="flipper_length_mm", 
        y="body_mass_g", 
        color="species", 
        size="bill_length_mm", 
        symbol="island", 
        labels={"species": "Species", "island": "Island"}
    )
    fig.update_layout(xaxis_title="Flipper Length (mm)", yaxis_title="Body Mass (g)")
    fig.update_xaxes(range=[160, 240])
    fig.update_yaxes(range=[2300, 6700])

    return fig

app.run_server(debug=True)