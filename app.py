import dash
from dash import Output, Input, html, dcc
import dash_bootstrap_components as dbc
from plotly.graph_objects import Figure
from comp import axis, figure, settings, panels

styles = [dbc.themes.DARKLY]
fig = Figure()

app = dash.Dash(__name__, external_stylesheets=styles,
            suppress_callback_exceptions=True)
server = app.server

app.layout = html.Div([
    dbc.Row([
        dbc.Col(
            html.Div([
                panels.make_panel(None),
                html.Div(id='panel-content', style={'margin-top': '20px'})
            ]),
            style={'background-color': '#333', 'height': '100vh', 'padding': '10px'},
            width=3
        ),
        dbc.Col(
            html.Div([
                html.Div("Right Section", id='toolbar',style={'color': '#fff'}),
                dcc.Graph(
                    id='figure-preview',
                    figure=fig,
                    config={'displaylogo': False, 'editable': True},
                    style={'height': '80vh', 'padding': '10px'}
                )
            ]),
            style={'background-color': '#222', 'padding': '20px'},
            width=9
        ),
    ], style={'margin': '0', 'width': '100%'})
])
axis.register_axis_callbacks(app,fig)
@app.callback(
    Output('panel-content', 'children'),
    Input('panel-select', 'value')
)
def update_panel_content(selected_value):
    if selected_value == 'axis':
        return axis.make_axis(None)
    elif selected_value == 'figure':
        return figure.make_fig(None)
    elif selected_value == 'settings':
        return settings.make_settings(None)
    elif selected_value == 'start':
        return html.Div("""Welcome to \n'Data Orbitron.'""")
    return html.Div("Select an option from the dropdown", style={'color': '#fff'})
if __name__ == '__main__':
    app.run(debug=True)
