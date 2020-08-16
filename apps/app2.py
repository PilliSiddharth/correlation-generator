import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from data_files import CHOICE_1, CHOICE_2, country
import dash_bootstrap_components as dbc
from app import app
import numpy as np
import pandas as pd

topic_options = [{'label': key, 'value':CHOICE_1[key]} for key in CHOICE_1]
topic_options_2 = [{'label': key, 'value':CHOICE_2[key]} for key in CHOICE_2]


topic_options_3 = [{'label':key, 'value':country[key]} for key in country]


layout = html.Div([
    dbc.Container([
    dbc.Row([
        dbc.Col(
            html.H2("Correlation-Generator(Year)",className="text-center")
        )
    ], style={'padding':20}),
    dbc.Row([
        dbc.Col(
            html.Div([
            html.H5("Select Series-1:", className="text-center"),

            dcc.Dropdown(
                id="CHOICE_1",
                options=topic_options,
                multi=False,
                value=list(CHOICE_1.keys()),
                className="dcc_control"
            )
        ], style={'padding':10}),
    )]
    ),



    dbc.Row([
        dbc.Col(
            html.Div([
                html.H5("Select Series-2:", className="text-center"),

                dcc.Dropdown(
                    id="CHOICE_2",
                    options=topic_options_2,
                    multi=False,
                    value=list(CHOICE_2.keys()),
                    className="dcc_control",

                )
            ], style={'padding':30}),
        )
    ]),
    dbc.Row([
        dbc.Col(
           html.Div([
               html.H5("Year Selection-1:", className="text-center"),
            dcc.Dropdown(
                id="year_sel_1",
                # options=[],
                # className="dcc_control"
            )
           ])
        ),
    dbc.Col(
        html.Div([
            html.H5("Year Selection-2:", className="text-center"),
            dcc.Dropdown(
                id="year_sel_2",
                # options=[],
                # className="dcc_control"
            )
        ])
    )], style={"padding":45}),
    # dbc.Row([
             html.Div([

        dbc.Button("Click me", id="example-button", color="primary", block=True),
        html.Span(id="example-output1", style={"vertical-align": "middle"}),
    ]
                 , style={"padding":30}


        )
    # ])
])])
# class corr_gen:
@app.callback(
    Output("year_sel_1","options"),
    [Input("CHOICE_1","value")])
def drpdwn_1_opt(ch1):
    df1 = pd.read_csv(ch1)
    y1 = list(df1['Year'].unique())
    y2 = list(df1['Year'].unique())
    drdp1 = dict(zip(y1,y2))
    return [{"label":str(i), "value":drdp1[i]}for i in drdp1]


@app.callback(
    Output("year_sel_2","options"),
    [Input("CHOICE_2","value")])
def drpdwn_2_opt(ch2):
    df_2 = pd.read_csv(ch2)
    y_1 = list(df_2['Year'].unique())
    y_2 = list(df_2['Year'].unique())
    drdp2 = dict(zip(y_1,y_2))
    return [{"label":str(i), "value":drdp2[i]}for i in drdp2]
