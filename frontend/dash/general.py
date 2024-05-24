from dash import html,dcc
import dash_bootstrap_components as dbc

#importamos sensores
from .sensor1 import sensor1
from .sensor2 import sensor2
from .sensor3 import sensor3
from .sensor4x import sensor4x
from .sensor4y import sensor4y
from .sensor4z import sensor4z
from .sensor5 import sensor5
from .sensor6 import sensor6

# Define estilos adicionales en CSS
styles = {
    'column-style': {
        'height': '190px',  # Ajusta la altura deseada
        'padding': '5px',  # Ajusta el padding deseado
        'border': '1px solid #ddd'  # Solo para visualizar los bordes de las columnas
    }
}

altura = {'height': '10%'}

general = dbc.Container([
    html.H4("Visualización sensores"),
    html.Br(),
    dbc.Row([
        dbc.Col(sensor1,md=4,style=styles['column-style']),
        dbc.Col(sensor2,md=4,style=styles['column-style']),
        dbc.Col(sensor3,md=4,style=styles['column-style']),
        dbc.Col(sensor4x,md=4,style=styles['column-style']),
        dbc.Col(sensor4y,md=4,style=styles['column-style']),
        dbc.Col(sensor4z,md=4,style=styles['column-style']),
        dbc.Col(sensor5,md=6,style=styles['column-style']),
        dbc.Col(sensor6,md=6,style=styles['column-style']),
    ])
])