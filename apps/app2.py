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
    ]
                 , style={"padding":30}


        ),
    dbc.Row([
        dbc.Col(
            html.Div([
                html.H6(id="example-output1", style={"vertical-align": "middle"}, className="text-center")
            ])
        )
    ])
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

@app.callback(
    Output("example-output1","children"),
    [Input("CHOICE_1","value"), Input("CHOICE_2","value"), Input("year_sel_1","value"), Input("year_sel_2", "value"),Input("example-button", "n_clicks")]
)
def corr_gen(cc1, cc2, yy1, yy2, n):
    df_1 = pd.read_csv(cc1)
    df_2 = pd.read_csv(cc2)

    df_1 = df_1.loc[df_1["Year"] == yy1]
    df_2 = df_2.loc[df_2["Year"] == yy2]

    df_all = df_2.merge(df_1.drop_duplicates(), on="Entity", how="left", indicator=False)

    df_all.rename(columns={df_all.columns[3]: "Data-1"}, inplace=True)
    df_all.rename(columns={df_all.columns[6]: "Data-2"}, inplace=True)

    df_all = df_all[df_all['Data-1'].notna()]
    df_all = df_all[df_all['Data-2'].notna()]

    X = np.array(df_all["Data-1"])
    Y = np.array(df_all["Data-2"])

    pearson_coef1 = np.corrcoef(X, Y)
    pearson_coef = pearson_coef1[1,0]

    if not n:
        pass
    else:
        return f"The correlation value is: {pearson_coef}"