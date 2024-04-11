import dash_bootstrap_components as dbc
from dash import html
import dash

dash.register_page(__name__)

layout = dbc.Container(
    [
        dbc.Row(dbc.Col(html.H1('About'))),
        dbc.Row(dbc.Col(html.P("Carefully selected info about the dashboard"))),
    ],
    fluid=True
)