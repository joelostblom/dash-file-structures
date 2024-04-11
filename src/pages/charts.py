from dash import callback, Output, Input
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import dash
import altair as alt
import pandas as pd


dash.register_page(__name__)


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
    dbc.CardHeader('Histogram', style={'fontWeight': 'bold'}),
    dbc.CardBody(
        dvc.Vega(
            id='histogram',
            opt={'actions': False},  # Remove the three dots button
            style={'width': '100%'}
        )
    )
])


# Layout
layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col(histogram),
                dbc.Col(density),
            ])
        ]),
    ])
], fluid=True)


@callback(
    Output('histogram', "spec"),
    Output('scatter', "spec"),
    Input('table-rows', "data"),
    Input("table-column", "data"),
)
def update_(table_rows, table_column):
    histogram = alt.Chart(pd.DataFrame(table_rows), width='container').mark_bar().encode(
        alt.X(f'{table_column[0]}:Q').bin(maxbins=30),
        alt.Y('count()')
    )
    scatter = alt.Chart(pd.DataFrame(table_rows), width='container').mark_area().transform_density(
        table_column[0],
        as_=[table_column[0], 'density']
    ).encode(
        alt.X(f'{table_column[0]}:Q'),
        alt.Y('density:Q'),
    )
    return histogram.to_dict(), scatter.to_dict()
