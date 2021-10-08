# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
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
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                    style={'textAlign': 'center', 'color': '#503D36','font-size': 40}),
                                html.Br(),

                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                html.Div(dcc.Dropdown(
                                    id='site-dropdown',
                                    options=launch_sites,
                                    value='All sites',
                                    placeholder='Select a launch site here',
                                    searchable=True,
                                    clearable=True)
                                ),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                #dcc.RangeSlider(id='payload-slider',...)

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
# -> output pie chart in response to drop down selection
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
    )
def output_pie(site): #input value 
    if (site=='All Sites' or site==None):
        all_sites = spacex_df[spacex_df['class'] == 1].reset_index(drop=True) # All Success only for all sites.
        all_sites.rename(columns={'class': 'count'}, inplace=True)
        fig = px.pie(
                all_sites, 
                values='count', 
                names='Launch Site', 
                title='Total Success Launches by All Sites',
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
            title=site +' launch rate',
            )
    return fig 

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)