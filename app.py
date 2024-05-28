from dash import Dash, Input, Output
import dash_bootstrap_components as dbc
from frontend.layout import layout
import plotly.graph_objs as go


#conexión base de datos
from bd.senoresController import readDistancia1DB
data_Distancia1 = []
tiempo = []

#conexión background
from background.distancia1BG import create_figure



app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = layout

# Función para agregar nuevos datos desde la base de datos
@app.callback(
    Output('sensorDistancia1', 'figure'),
    Input('interval-component', 'n_intervals'),
)
def actualizacionFigura(n):
    
    data = readDistancia1DB()
    data_Distancia1.append(float(data['distancia']))
    tiempo.append(data['tiempo'])
    figure = create_figure(tiempo, data_Distancia1)
    return figure
                

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    app.run_server(debug=True, host='0.0.0.0', port=port)
