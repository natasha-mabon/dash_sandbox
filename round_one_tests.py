# Author: Natasha Mabon
# Date: 08/03/2022

# - Package imports, run install script if there are any issues with this ------------------------------------------- #

import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
import config

style = config.Style()

# - Script ---------------------------------------------------------------------------------------------------------- #

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)  # initialising dash app
df = px.data.stocks()  # reading stock price dataset
preferred_blue = style.blue
preferred_font = style.preferred_font

app.layout = html.Div(id='parent', children=[

    # Row 1

    html.Div(children=[
        html.H1(id='H1', children='Test app', style={'textAlign': 'center',
                                                     'color': preferred_blue,
                                                     'font-family': preferred_font,
                                                     'marginTop': 40,
                                                     'marginBottom': 40}),

        dcc.Dropdown(id='dropdown',
                     options=[
                         {'label': 'Google', 'value': 'GOOG'},
                         {'label': 'Apple', 'value': 'AAPL'},
                         {'label': 'Amazon', 'value': 'AMZN'},
                     ],
                     style={'font-family': preferred_font},
                     value='GOOG')
    ], className='row'),

    # Row 2

    html.Div(children=[
        html.Div(children=[
            dcc.Graph(id='bar_plot')], className='six columns'),
        html.Div(children=[
            dcc.Graph(id='bar_plot_2')], className='six columns')
    ], className='row')

])


@app.callback(Output(component_id='bar_plot', component_property='figure'),
              [Input(component_id='dropdown', component_property='value')])
@app.callback(Output(component_id='bar_plot_2', component_property='figure'),
              [Input(component_id='dropdown', component_property='value')])

def graph_update(dropdown_value):
    print(dropdown_value)
    fig = go.Figure([go.Scatter(x=df['date'],
                                y=df['{}'.format(dropdown_value)],
                                line=dict(color=preferred_blue, width=4))
                     ])

    fig.update_layout(title='Stock prices over time',
                      xaxis_title='Dates',
                      yaxis_title='Prices',
                      template='plotly_white',
                      title_font_family=preferred_font
                      )
    return fig


if __name__ == '__main__':
    app.run_server()

print('Script Completed.')
