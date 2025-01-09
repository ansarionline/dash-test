import dash_bootstrap_components as dbc
def make_panel(fig):
    return dbc.Row([
        dbc.Col([
            dbc.Select(
                id='panel-select',
                options=[
                    {'label': 'Axis', 'value': 'axis'},
                    {'label': 'Figure', 'value': 'figure'},
                    {'label': 'Settings', 'value': 'settings'},
                    {'label': 'Start', 'value': 'start'}
                ],
                value='start',  
                name="Editing Mode"
            ),
        ])
    ])
