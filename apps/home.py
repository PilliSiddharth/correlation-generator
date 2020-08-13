import dash_html_components as html
import dash_bootstrap_components as dbc

# needed only if running this as a single page app
# external_stylesheets = [dbc.themes.LUX]

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# change to app.layout if running as single page app instead
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Welcome to the Correlation-Generator", className="text-center")
                    , className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.H5(children='This app is used for generating the correlation-value using ourworldindata datasets! '
                            )
                    , className="mb-4")
        ]),

        dbc.Row([
            dbc.Col(dbc.Card(children=[html.H4(children='Access the Datasets used in the web application in OurWorldInData',
                                               className="text-center"),
                                       dbc.Button("Access Data",
                                                  href="https://www.ourworldindata.org",
                                                  color="primary",
                                                  className="mt-3"),
                                       ],
                             body=True, color="dark", outline=True)
                    , width=6, className="mb-4"),

            dbc.Col(dbc.Card(children=[html.H3(children='Access the code used to build this dashboard',
                                               className="text-center"),
                                       dbc.Button("GitHub",
                                                  href="https://github.com/meredithwan/covid-dash-app",
                                                  color="primary",
                                                  className="mt-1"),
                                       ],
                             body=True, color="dark", outline=True)
                    , width=6, className="mb-4"),

            # dbc.Col(dbc.Card(children=[html.H3(children='Read the project Documentation here',
            #                                    className="text-center"),
            #                            dbc.Button("Documentation",
            #                                       href="https://medium.com/@meredithwan",
            #                                       color="primary",
            #                                       className="mt-3"),
            #
            #                            ],
            #                  body=True, color="dark", outline=True)
            #         , width=4, className="mb-4")
        ], className="mb-5"),

        html.A("Icon made by: Becris",
               href="https://creativemarket.com/Becris")

    ])])

