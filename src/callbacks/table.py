from dash import Output, Input, callback

from data import cars


@callback(
    Output('table', "columns"),
    Output('table', "data"),
    Input('dropdown', "value"),
)
def update_table(dropdown_cols):
    return(
        [  # A list of dictionaries, each representing a column
            {
                "name": col.replace('_', ' '),
                "id": col,
                'selectable': False if col == 'Name' else True
            }
            for col in dropdown_cols
        ],
        cars[dropdown_cols].to_dict('records')
    )
