from dash import Dash, Input, Output
import dash_bootstrap_components as dbc
from frontend.layout import layout


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = layout

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    app.run_server(debug=True, host='0.0.0.0', port=port)
