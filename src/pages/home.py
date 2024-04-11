import dash_bootstrap_components as dbc
from dash import html
import dash

dash.register_page(__name__, path='/')

layout = dbc.Container(
    [
        dbc.Row(dbc.Col(html.H1('Home'))),
        dbc.Row(dbc.Col(html.P('Welcome to the home page!'))),
    ],
    fluid=True
)