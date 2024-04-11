from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash


# Initialization
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title='Multi page',
    use_pages=True,
    suppress_callback_exceptions=True,
)

navbar = dbc.NavbarSimple(
    [
        dbc.NavLink(
            html.Div(page["name"]),
            href=page["path"],
            active="exact",
        )
        for page in dash.page_registry.values() if page['name'] not in ['Home', 'About']
    ][::-1] + [
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("About", href="about"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="SplashBoard",
    brand_href="/",
    color="steelblue",
    dark=True,
    fluid=True,
    links_left=True,
    style={'margin-bottom': '20px'}
)

app.layout = dbc.Container(
    [
        dcc.Store(id="table-rows", data={}),
        dcc.Store(id="table-column", data={}),
        dbc.Row(
            dbc.Col(
                navbar
            ),
            style={'bavkground-color': 'red'}
        ),
        dbc.Row(
            dbc.Col(dash.page_container)
        )
    ],
    fluid=True,
    style={'padding': 0}
)

if __name__ == '__main__':
    app.run(debug=True)
