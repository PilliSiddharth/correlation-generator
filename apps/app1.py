import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from data_files import CHOICE_1, CHOICE_2, country
import dash_bootstrap_components as dbc
from app import app

topic_options = [{'label': key, 'value':CHOICE_1[key]} for key in CHOICE_1]

def series_search():
    return html.Div([
        html.Div([
            html.H5("Select Series-1:", className="text-center"),

            dcc.Dropdown(
                id="CHOICE_1",
                options=topic_options,
                multi=False,
                value=list(CHOICE_1.keys()),
                className="dcc_control"
            )
        ])
    ])


topic_options_2 = [{'label': key, 'value':CHOICE_2[key]} for key in CHOICE_2]

def series_search2():
    return html.Div([
        html.Div([
            html.H5("Select Series-2:", className="text-center"),

            dcc.Dropdown(
                id="CHOICE_2",
                options=topic_options_2,
                multi=False,
                value=list(CHOICE_2.keys()),
                className="dcc_control2"
            )
        ])
    ])
topic_options_3 = [{'label':key, 'value':country[key]} for key in country]
def country_search():
    return html.Div([
        html.Div([
            html.H4("Select Country/WORLD:",className="text-center"),

            dcc.Dropdown(
                id="Country",
                options=topic_options_3,
                multi=False,
                value=list(country.keys()),
                className="mb-5",
                placeholder="Select Business Area"
            )
        ] ,style={'width':'96%','padding-left':'3%', 'padding-right':'1', 'padding':50})



    ])


layout = html.Div([
    dbc.Container([
    dbc.Row([
        dbc.Col(
            html.H2("Correlation-Generator(Country)",className="text-center")
        )
    ]),
    dbc.Row([
        dbc.Col(
        )
    ]),
    dbc.Row([
        dbc.Col(
            children=series_search()
        ),
        dbc.Col(
            children=series_search2()
        )
    ]),
    dbc.Row([
        dbc.Col(
            children=country_search()
        )
    ])
    ]
)])

# @app.callback(
#     Output('app-1-display-value', 'children'),
#     [Input('app-1-dropdown', 'value')])
# def display_value(value):
#     return 'You have selected "{}"'.format(value)