
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_html_components as html

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import pandas as pd

df = pd.read_csv('Imiona_nadane_wPolsce_w_latach_2000-2019.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div(children=[
                      html.H1('Popularność imion w XXI wieku', style={'textAlign': 'center',}),
                      html.Div(["Imię: ", dcc.Input(id='name-input', value='KAZIMIERZ', type='text')],
                               style={'textAlign': 'center',}),
                      html.Hr(),
                      dcc.Graph(id='graph',),
                      html.Hr(),
                      html.Span(["**Dane pochodzą z ",
                                html.A('dane.gov.pl/dataset/219,imiona-nadawane-dzieciom-w-polsce',
                                        href="https://dane.gov.pl/dataset/219,imiona-nadawane-dzieciom-w-polsce",
                                        target="blank")]),
                      ])


@app.callback(
    [Output(component_id='graph', component_property='figure'),],
    [Input(component_id='name-input', component_property='value')]
)


def update(name):
    '''Get name from name-input, load data from df, update graph.'''
    name = name.upper()
    df_temp = df[df['Imię'] == name].drop(columns=['Płeć'])
    fig = go.Figure(data=go.Bar(y=df_temp['Liczba'].values, x=df_temp['Rok'].values),)
    fig.update_layout(title=f'Tyle razy imię {name} zostało nadane jako pierwsze w Polsce w latach 2000-2019',
                      hovermode='x',
                      xaxis_title = 'Lata',
                      font=dict(
                        family="Courier New, monospace",
                        size=18,
                        color="RebeccaPurple"),)
    return (fig,)


if __name__ == '__main__':
    app.run_server(debug=False)
