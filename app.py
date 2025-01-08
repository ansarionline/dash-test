import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

# Initialize the Dash app with a dark Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
app.title = "Data Visualization Tool"
server = app.server
# Define the layout
app.layout = dbc.Container([
    dbc.Row([
        # Sidebar for panel selection
        dbc.Col([
dcc.Dropdown(
    id='panel-selector',
    options=[
        {'label': 'Axis Controls', 'value': 'axis-controls'},
        {'label': 'Figure Controls', 'value': 'figure-controls'},
        {'label': 'Settings', 'value': 'settings'}
    ],
    value='axis-controls',
    placeholder='Select Panel',
    className="mb-4",
    style={
        'background-color': '#949494',  # Dark background to match the theme
        'color': '#000000',            # White text for readability
        'border': '1px solid #495057', # Border for better separation
        'border-radius': '5px',        # Rounded corners for a polished look
        'padding': '10px',
        'font-color':'#ffffff'# Extra padding for a better feel
    }
),
        html.Div(id='panel-content', className="p-3 bg-secondary text-white rounded")
        ], width=3, className="bg-dark p-3"),

        # Main content area
        dbc.Col([
            # Toolbar
            dbc.Row([
                dbc.Col(dbc.Button("Upload Data", id="upload-data",
                color="success", className="m-1"), width=3),
                
                dbc.Col(dbc.Button("Preview Data", id="preview-data", 
                color="warning", className="m-1"), width=3),

                dbc.Col(dbc.Button("Add Trace", id="add-trace", 
                color="primary", className="m-1"), width=3),
                
                dbc.Col(dbc.Button("Remove Trace", id="remove-trace", 
                color="danger", className="m-1"), width=3),
                
            ], className="mb-3"),

            # Plot preview area
            dbc.Row([
                dbc.Col(
                    dcc.Graph(id='plot-preview', style={'height': '80vh'},
                            config={
                    'scrollZoom': True,
                    'editable': True
                }),
                    width=12
                )
            ]),
        ], width=9)
    ])
], fluid=True)

# Callback for updating the plot based on panel selection and editable properties
@app.callback(
    Output('plot-preview', 'figure'),
    [
        Input('panel-selector', 'value'),
    ]
)
def update_plot(selected_panel):
    # Create a basic plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 1, 2], mode='lines+markers', name='Trace 1'))

    # Add additional properties based on panel selection
    if selected_panel == 'axis-controls':
        pass
    elif selected_panel == 'figure-controls':
        pass
    elif selected_panel == 'settings':
        pass

    return fig
if __name__ == '__main__':
    app.run(debug=True)
