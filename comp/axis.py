import dash_bootstrap_components as dbc
from dash import html, Output,Input
from dash_daq.ColorPicker import ColorPicker
fonts = ['Arial', 'Courier New', 'Times New Roman', 'Verdana', 'Georgia', 'Tahoma']

default = {
    'label':'X-label',
    'font':'Arial',
    'size':20,
    'Color':'#000000'
}

def make_axis(fig):
    return dbc.Form(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [html.H5("X-Label"),
                        html.Div(id='x-label', children=
                            [
                                dbc.Input(id='x-label-text', placeholder='Label Text',
                                style={'margin':'5px'},value=default['label']),
                                dbc.InputGroup([
                                dbc.Select(id='x-label-font', options=fonts,value=default['font']),
                                dbc.Input(id='x-label-size',type='number',placeholder='size',
                                min=1,value=default['size']),
                                dbc.Input(id='x-label-color',placeholder='Color',
                                type='color',value=default['Color'],style={'height':'40px'})
                                ],style={'margin':'5px'}),
                            ]
                        ),
                        html.H5("X-Rangings"),
                        html.Div(id='x-range', children=
                            [
                                dbc.InputGroup([dbc.Input(id='x-range-min',type='number',
                                placeholder='Min range',value=0),
                                dbc.Input(id='x-range-max',type='number',
                                placeholder='Max range',value=10),
                                dbc.Input(id='x-range-step',type='number',
                                placeholder='Steps',min=1,value=1)],style={'margin':'5px'})]
                        )],
                    ),
                ],
                className="mb-3"
            ),
        ],className="fullscreen-child",style={'margin':'5px'})
    
def register_axis_callbacks(app,fig):
    @app.callback(
        Output('figure-preview', 'figure'),
        [Input('x-label-text', 'value'),
        Input('x-label-font', 'value'),
        Input('x-label-color', 'value'),
        Input('x-label-size', 'value'),
        Input('x-range-min', 'value'),
        Input('x-range-max', 'value'),
        Input('x-range-step', 'value')]
    )
    def update_axis_label(label,font,color,size,r_min,r_max,r_step):
        default['label'] = label
        default['font'] = font
        default['Color'] = color
        default['size'] = size
        return fig.update_layout(xaxis=dict(
            title=label,
            title_font=dict(
                size=size,
                color=color,
                family=font),
            range=[r_min,r_max],
            dtick=r_step
            ))
