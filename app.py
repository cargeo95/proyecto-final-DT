from dash import Dash, Input, Output
import dash_bootstrap_components as dbc
from frontend.layout import layout


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = layout

if __name__ == "__main__":
    app.run_server(debug=True)