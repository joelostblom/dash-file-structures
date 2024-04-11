import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Output, Input, dash_table
from vega_datasets import data


cars = data.cars()
dash.register_page(__name__)

# Components
table = dbc.Col(
    dash_table.DataTable(
        id='table',
        # The data and columns parameters are set in the callback instead
        column_selectable="single",
        selected_columns=['Miles_per_Gallon'], 
        page_size=8,
        sort_action='native',
        filter_action='native',
        style_data_conditional=[{
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(248, 248, 248)'
        }],
         style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold'
        },
        style_as_list_view=True,
        editable=True,
        # Persistnce ensures the column selection is kept
        # when switching away from the Table page and then back again
        # We could have used dcc.Store here to but it is more complex
        # Details: https://dash.plotly.com/persistence
        # persistence=True,
    ),
)

dropdown = dcc.Dropdown(
    id='dropdown',
    options=cars.columns,
    value=['Name', 'Miles_per_Gallon', 'Horsepower'],
    multi=True,
    persistence=True,
)

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

# Layout
layout = dbc.Container(
    [
        dbc.Row([
            sidebar,  # Already wrapped in dbc.Col
            dbc.Col([
                table, # Already wrapped in dbc.Col
            ]),
        ])
    ],
    fluid=True
)

@callback(
    Output('table', "columns"),
    Output('table', "data"),
    Output("table-column", "data"),
    Output("table-rows", "data"),
    Input('dropdown', "value"),
    Input('table', "selected_columns"),
    Input('table', "derived_virtual_data"),
)
def update_table(dropdown_cols, table_column, table_rows):
    return(
        [  # A list of dictionaries, each representing a column
            {
                "name": col.replace('_', ' '),
                "id": col,
                'selectable': False if col == 'Name' else True
            }
            for col in dropdown_cols
        ],
        cars[dropdown_cols].to_dict('records'),
        table_column,
        table_rows
    )