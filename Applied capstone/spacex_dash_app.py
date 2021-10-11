# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
spacex_df.drop(columns=['Unnamed: 0', 'Mission Outcome'], inplace=True)
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Get unique launch sites for drop down menu 
unique_launch_sites = spacex_df['Launch Site'].unique().tolist()
launch_sites = []
launch_sites.append({'label': 'All Sites', 'value': 'All Sites'})
for launch_site in unique_launch_sites:
    launch_sites.append({'label': launch_site, 'value': launch_site})

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[# Header 
                                html.H1('SpaceX Launch Records Dashboard',
                                    style={'textAlign': 'center', 'color': '#503D36','font-size': 40}),
                                html.Br(),

                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # ->Set default select value as 'ALL sites'
                                html.Div(dcc.Dropdown(
                                    id='site-dropdown',
                                    options=launch_sites,
                                    value='All Sites',
                                    placeholder='Select a launch site here',
                                    searchable=True,
                                    clearable=True)
                                ),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                # TASK 3: Add a slider to select payload range
                                # -> Set default value to be max & min payload 
                                html.P("Payload range (Kg):"),
                                html.Div(dcc.RangeSlider(id='payload-slider', 
                                                            min=0, max=10000, step=1000,
                                                            value=[min_payload,max_payload],
                                                            marks={
                                                                0:{'label':'0 (min)', 'style':{'font-size':15, 'font-weight':'bold'}},
                                                                2500:'2500',
                                                                5000:'5000',
                                                                7500:'7500',
                                                                9600: {'label':'9600 (max)', 'style':{'font-size':15, 'font-weight':'bold'}},
                                                                10000:'1000'
                                                                })
                                                            ),
                                html.Div(id='retun-payload-range'),
                                html.Br(),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function to output a pie chart in response to drop down selection
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
    )
def output_pie(site): #input value 
    if (site =='All Sites'):
        all_sites = spacex_df[spacex_df['class'] == 1].reset_index(drop=True) # All Success only for all sites.
        all_sites.rename(columns={'class': 'count'}, inplace=True)
        fig = px.pie(
                all_sites, 
                values='count', 
                names='Launch Site', 
                title='Total Success Launches by Site',
                color_discrete_sequence=px.colors.sequential.RdBu
                )
    else:
        selected_site = spacex_df[spacex_df['Launch Site']==site].reset_index(drop=True)
        site_sucessRate = selected_site.groupby(['Launch Site', 'class']).size().reset_index()
        site_sucessRate.rename(columns={0:'count'}, inplace=True)
        site_sucessRate.replace([0,1],['Fail', 'Successs'], inplace=True)
        fig = px.pie(
                site_sucessRate, 
                values='count', 
                names='class', 
                title='Total Success Launches for site '+site,
                )
    return fig 

# TASK 3:
# Add a callback function that returns the selected pay load range
@app.callback(
    Output('retun-payload-range', 'children'),
    Input('payload-slider', 'value'))
def output_payload_range(payload_range):
    return 'You have selected range {}'.format(payload_range)

# TASK 4:
# Add a callback function to output a scatter plot in response payload range
@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [Input('site-dropdown', 'value'), Input('payload-slider', 'value')]) #multiple inputs
def output_scatter(site, payload_range):
    low,high = payload_range
    df = spacex_df
    filtered_df = df[df['Payload Mass (kg)'].between(low,high)]

    if site =='All Sites':
        fig = px.scatter(filtered_df, 
                        x='Payload Mass (kg)', 
                        y='class', 
                        size='Payload Mass (kg)',
                        color='Booster Version Category', 
                        title='Success Rate for All Sites by Payload Range')
    else:
        filtered_df = filtered_df[filtered_df['Launch Site']==site]
        fig = px.scatter(filtered_df, 
                        x='Payload Mass (kg)', 
                        y='class', 
                        size='Payload Mass (kg)',
                        color='Booster Version Category', 
                        title='Success Rate for Site {} by Payload Range'.format(site))
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)