from dash import html,dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

# Datos de ejemplo
data = [1, 2, 3, 4, 5]
tiempo = [10, 15, 13, 17, 21]

sensorV1 = dbc.Container([
    html.Label("Sensor 1 - Vibración"),
    dcc.Graph(id="sensorVibracion1"),
    dcc.Interval(
        id='interval-sensorVibracion1',
        interval=2000,
        n_intervals=0
    ),
])