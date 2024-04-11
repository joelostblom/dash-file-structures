import dash_vega_components as dvc
import dash_bootstrap_components as dbc
from dash import html, dcc

from data import cars


# Components
title = html.H1(
    'Splashboard Demo',
    # The title is being styled in the `assets/styles.css` file instead of there
    className='mytitle'
)

dropdown = dcc.Dropdown(
    id='dropdown',
    options=cars.columns,
    value=['Name', 'Miles_per_Gallon', 'Horsepower'],
    multi=True
)

density = dbc.Card([
    dbc.CardHeader('Density', style={'fontWeight': 'bold'}),
    dbc.CardBody(
        dvc.Vega(
            id='scatter',
            opt={'actions': False},  # Remove the three dots button
            style={'width': '100%'}
        )
    )
])

histogram = dbc.Card([
    dbc.CardHeader('Histrogram', style={'fontWeight': 'bold'}),
    dbc.CardBody(
        dvc.Vega(
            id='histogram',
            opt={'actions': False},  # Remove the three dots button
            style={'width': '100%'}
        )
    )
])

sidebar = dbc.Col([
    html.H5('Global controls'),
    html.Br(),
    dropdown,
    html.Br(),
    dcc.Dropdown(),
    html.Br(),
    dcc.Dropdown(),
    ],
    md=3,
    style={
        'background-color': '#e6e6e6',
        'padding': 10,
        'border-radius': 3,
    }
) 


