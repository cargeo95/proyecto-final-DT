from dash import html,dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

# Datos de ejemplo
data = [1, 2, 3, 4, 5]
tiempo = [10, 15, 13, 17, 21]

sensor5 = dbc.Container([
    html.Label("Sensor 5 - Distancia"),
    dcc.Graph(
        id="sensor5",
        figure={
            'data' : [
                go.Scatter(
                    x = tiempo,
                    y = data,
                    mode = 'lines+markers',
                    marker = {'size':5},
                )
            ],
            'layout': go.Layout(
                
                xaxis={
                    'title': {
                        'text': 'Tiempo (s)',  # Título del eje X
                        'font': {
                            'size': 12  # Ajusta el tamaño del texto del título del eje X
                        }
                    },
                    'tickfont': {
                        'size': 10  # Ajusta el tamaño del texto de las etiquetas del eje X
                    }
                },
                yaxis={
                    'title': {
                        'text': 'Datos del Sensor',  # Título del eje Y
                        'font': {
                            'size': 12  # Ajusta el tamaño del texto del título del eje Y
                        }
                    },
                    'tickfont': {
                        'size': 10  # Ajusta el tamaño del texto de las etiquetas del eje Y
                    }
                }, 
                margin=dict(l=30, r=0, b=0, t=0),  # Ajustar márgenes si es necesario
                height=150,  # Ajustar la altura del gráfico
            )
        },
    )
])