from dash import Output, Input, callback
import altair as alt
import pandas as pd


@callback(
    Output('histogram', "spec"),
    Output('scatter', "spec"),
    Input('table', "derived_virtual_data"),
    Input('table', "selected_columns"),
    prevent_initial_call=True  # Avoid triggering before the table has a selected column
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