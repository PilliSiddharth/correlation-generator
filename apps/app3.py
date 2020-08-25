import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from data_files import CHOICE_1, CHOICE_2, country
import dash_bootstrap_components as dbc
from app import app
import numpy as np
import plotly_express as px
import pandas as pd

topic_options = [{'label': key, 'value':CHOICE_1[key]} for key in CHOICE_1]
# topic_options_2 = [{'label': key, 'value':CHOICE_2[key]} for key in CHOICE_2]

# topic_options_3 = [{'label':key, 'value':country[key]} for key in country]


layout = html.Div([
    dbc.Container([
    dbc.Row([
        dbc.Col(
            html.H2("Correlation-Generator(Country)",className="text-center")
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


    #
    # dbc.Row([
    #     dbc.Col(
    #         html.Div([
    #             html.H5("Select Series-2:", className="text-center"),
    #
    #             dcc.Dropdown(
    #                 id="CHOICE_2",
    #                 options=topic_options_2,
    #                 multi=False,
    #                 value=list(CHOICE_2.keys()),
    #                 className="dcc_control",
    #
    #             )
    #         ], style={'padding':30}),
    #     )
    ]),
    dbc.Row([
        dbc.Col(
            html.Div([
                html.H6("Select Country-1", className="text-center"),

                dcc.Dropdown(
                    id="count_sel_1"
                ),

            ])
        ),
        dbc.Col(
            html.Div([
                html.H6("Select Country-2", className="text-center"),

                dcc.Dropdown(
                    id="count_sel_2"
                )
            ])
        )
    ], style={"padding":30}),
    # dbc.Row([
    #     dbc.Col(
    #         html.Div([
    #             html.H4("Select Country/WORLD:", className="text-center"),
    #
    #             dcc.Dropdown(
    #                 id="Country",
    #                 options=topic_options_3,
    #                 multi=False,
    #                 value=list(country.keys()),
    #                 className="dcc_control",
    #                 placeholder="Select Business Area"
    #             )
    #         ], style={"padding":"30"}
    #
    #     )),
    # ]),
             html.Div([

        dbc.Button("Submit", id="example-button", color="primary", block=True),
    ], style={"padding":30}),
                 # , style={'verticalAlign': 'middle', 'width': '200px', 'display': 'inline-block'}

    dbc.Row([
        dbc.Col(
            html.Div([
                html.H5(id="example-output4", style={"vertical-align": "middle"}, className="text-center"),
            ], style={"padding":30})
        )
    ]),
        dcc.Graph(id="graph3"),
])
    # ])

@app.callback(
    Output("count_sel_1","options"),
    [Input("CHOICE_1","value")])
def drpdwn_1_opt(ch1):
    df1 = pd.read_csv(ch1)
    y1 = list(df1['Entity'].unique())
    y2 = list(df1['Entity'].unique())
    drdp1 = dict(zip(y1,y2))
    return [{"label":str(i), "value":drdp1[i]}for i in drdp1]
#
#
@app.callback(
    Output("count_sel_2","options"),
    [Input("CHOICE_1","value")])
def drpdwn_2_opt(ch2):
    df_2 = pd.read_csv(ch2)
    y_1 = list(df_2['Entity'].unique())
    y_2 = list(df_2['Entity'].unique())
    drdp2 = dict(zip(y_1,y_2))
    return [{"label":str(i), "value":drdp2[i]}for i in drdp2]

@app.callback(
    Output("example-output4","children"),
    [Input("CHOICE_1","value"),Input("count_sel_1","value"), Input("count_sel_2", "value"),Input("example-button", "n_clicks")]
)
def corr_gen(cc1, yy1, yy2, n):
    df_1 = pd.read_csv(cc1)
    df_2 = pd.read_csv(cc1)

    df_1 = df_1.loc[df_1["Entity"] == yy1]
    df_2 = df_2.loc[df_2["Entity"] == yy2]

    df_all = df_2.merge(df_1.drop_duplicates(), on="Year", how="left", indicator=False)

    df_all.rename(columns={df_all.columns[3]: "Data-1"}, inplace=True)
    df_all.rename(columns={df_all.columns[6]: "Data-2"}, inplace=True)

    df_all = df_all[df_all['Data-1'].notna()]
    df_all = df_all[df_all['Data-2'].notna()]

    X = np.array(df_all["Data-1"])
    Y = np.array(df_all["Data-2"])

    try:
        pearson_coef1 = np.corrcoef(X, Y)
        pearson_coef = pearson_coef1[1, 0]
        int(pearson_coef)
    except ZeroDivisionError:
        return "The country you choosed for the dataset is not available"

    if n is None:
        pass
    else:
        dat = str(pearson_coef)
        if dat[0] == '-':
            if pearson_coef >= -0.4:
                pe_str = str(pearson_coef)
                my_str = "This is a Week Negative correlation: {}".format(pe_str)
                return my_str
                # return px.scatter(X, Y, height=700, trendline="ols")

            elif pearson_coef >= -0.7:
                pe_str = str(pearson_coef)
                my_str = "This is a Medium Negative correlation: {}".format(pe_str)
                return my_str
                # return px.scatter(X, Y, height=700, trendline="ols")

            elif pearson_coef < -0.7:
                pe_str = str(pearson_coef)
                my_str = "This is a strong Negative correlation: {}".format(pe_str)
                return my_str
                # return px.scatter(X, Y, height=700, trendline="ols")

        else:
            if pearson_coef <= 0.4:
                pe_str = str(pearson_coef)
                my_str = "This is a Week Positive correlation: {}".format(pe_str)
                return my_str
                # return px.scatter(X, Y, height=700, trendline="ols")

            elif pearson_coef <= 0.7:
                pe_str = str(pearson_coef)
                my_str = "This is a Medium Positive correlation: {}".format(pe_str)
                return my_str
                # return px.scatter(X, Y, height=700, trendline="ols")

            elif pearson_coef > 0.7:
                pe_str = str(pearson_coef)
                my_str = "This is a Strong Positive correlation: {}".format(pe_str)
                return my_str
                # return px.scatter(X, Y, height=700, trendline="ols")

@app.callback(
    Output("graph3","figure"),
    [Input("CHOICE_1","value"),Input("count_sel_1","value"), Input("count_sel_2", "value")]
)
def corr_gen(cc1, yy1, yy2):
    df_1 = pd.read_csv(cc1)
    df_2 = pd.read_csv(cc1)

    df_1 = df_1.loc[df_1["Entity"] == yy1]
    df_2 = df_2.loc[df_2["Entity"] == yy2]

    df_all = df_2.merge(df_1.drop_duplicates(), on="Year", how="left", indicator=False)

    df_all.rename(columns={df_all.columns[3]: "Data-1"}, inplace=True)
    df_all.rename(columns={df_all.columns[6]: "Data-2"}, inplace=True)

    df_all = df_all[df_all['Data-1'].notna()]
    df_all = df_all[df_all['Data-2'].notna()]

    return px.scatter(df_all, x="Data-1", y="Data-2", height=700,trendline="ols")
# @app.callback(
#     Output("Country", "options"),
#     [Input("CHOICE_1", "value"), Input("CHOICE_2","value")]
# )
# def cntry_drpdwn(ch1, ch2):
#     df1 = pd.read_csv(ch1)
#     df2 = pd.read_csv(ch2)
#
#     x1 = list(df1['Entity'].unique())
#     x2 = list(df2['Entity'].unique())
# @app.callback(
# Output("example-output","children"),
# #
#     [Input('CHOICE_1','value'), Input('CHOICE_2', 'value'), Input('Country', 'value'), Input('example-button','n_clicks')]
# )
# def corr_gen(ch1, ch2, count, n):
#
#     df1 = pd.read_csv(ch1)
#     df2 = pd.read_csv(ch2)
#
#     df_1 = df1.loc[(df1["Entity"] == count)]
#     df_2 = df2.loc[(df2["Entity"] == count)]
#
#     df_all = df_2.merge(df_1.drop_duplicates(), on="Year", how="left", indicator=False)
#
#     df_all.rename(columns={df_all.columns[3]: "Data-1"}, inplace=True)
#     df_all.rename(columns={df_all.columns[6]: "Data-2"}, inplace=True)
#
#     df_all = df_all[df_all['Data-1'].notna()]
#     df_all = df_all[df_all['Data-2'].notna()]
#
#     X = df_all["Data-1"]
#     Y = df_all["Data-2"]
#
#     try:
#         pearson_coef1 = np.corrcoef(X, Y)
#         pearson_coef = pearson_coef1[1, 0]
#         int(pearson_coef)
#     except ZeroDivisionError:
#         return "The country you choosed for the dataset is not available"
#
#     if n is None:
#         pass
#     else:
#         dat = str(pearson_coef)
#         if dat[0] == '-':
#             if pearson_coef >= -0.4:
#                 pe_str = str(pearson_coef)
#                 my_str = "This is a Week Negative correlation: {}".format(pe_str)
#                 return my_str
#                 # return px.scatter(X, Y, height=700, trendline="ols")
#
#             elif pearson_coef >= -0.7:
#                 pe_str = str(pearson_coef)
#                 my_str = "This is a Medium Negative correlation: {}".format(pe_str)
#                 return my_str
#                 # return px.scatter(X, Y, height=700, trendline="ols")
#
#             elif pearson_coef < -0.7:
#                 pe_str = str(pearson_coef)
#                 my_str = "This is a strong Negative correlation: {}".format(pe_str)
#                 return my_str
#                 # return px.scatter(X, Y, height=700, trendline="ols")
#
#         else:
#             if pearson_coef <= 0.4:
#                 pe_str = str(pearson_coef)
#                 my_str = "This is a Week Positive correlation: {}".format(pe_str)
#                 return my_str
#                 # return px.scatter(X, Y, height=700, trendline="ols")
#
#             elif pearson_coef <= 0.7:
#                 pe_str = str(pearson_coef)
#                 my_str = "This is a Medium Positive correlation: {}".format(pe_str)
#                 return my_str
#                 # return px.scatter(X, Y, height=700, trendline="ols")
#
#             elif pearson_coef > 0.7:
#                 pe_str = str(pearson_coef)
#                 my_str = "This is a Strong Positive correlation: {}".format(pe_str)
#                 return my_str
#                 # return px.scatter(X, Y, height=700, trendline="ols")
#    #
# @app.callback(
#     Output("graph","figure"),
#     [Input('CHOICE_1','value'), Input('CHOICE_2', 'value'), Input('Country', 'value')]
# )
# def load_fig(ch5, ch6, count9):
#     df = pd.read_csv(ch5)
#     df9 = pd.read_csv(ch6)
#
#     df_18= df.loc[(df["Entity"] == count9)]
#     df_21 = df9.loc[(df9["Entity"] == count9)]
#
#     df_alls = df_21.merge(df_18.drop_duplicates(), on="Year", how="left", indicator=False)
#
#     df_alls.rename(columns={df_alls.columns[3]: "Data-1"}, inplace=True)
#     df_alls.rename(columns={df_alls.columns[6]: "Data-2"}, inplace=True)
#
#     df_alls = df_alls[df_alls['Data-1'].notna()]
#     df_alls = df_alls[df_alls['Data-2'].notna()]
#
#     return px.scatter(df_alls, "Data-1", "Data-2", height=700,trendline="ols")
# return html.Div('The value is:"{}" '.format(pearson_coef))
# @app.callback(
# Output("Country", "options"),
#     [Input("CHOICE_1", "value"), Input("CHOICE_2","value")]
# )
# def load_country(ch1, ch2):
#     if ch1 == "" and ch2 == "":
#         print("Input Invalid")
#     print(ch1)
#     print(ch2)