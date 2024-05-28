from dash import html,dcc
import dash_bootstrap_components as dbc

sensorDistancia1 = dbc.Container([
    html.Label("Sensor 5 - Distancia"),
    dcc.Graph(id="sensorDistancia1"),
    dcc.Interval(
        id='interval-component',
        interval=2000,
        n_intervals=0
    ),


])