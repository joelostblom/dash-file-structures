import dash_bootstrap_components as dbc
from dash import dash_table

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
    ),
)
