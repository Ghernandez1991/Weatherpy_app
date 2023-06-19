# import sqlite3
# import plotly.express as px
# import dash
# import pandas as pd

# from dash import dcc
# from dash import html
# from dash.dependencies import Input, Output


# # Read the data into a pandas DataFrame
# conn = sqlite3.connect("weather.db")
# cursor = conn.cursor()
# query = "SELECT * FROM all_weather_data "
# data = pd.read_sql_query(query, conn)
# print(data.columns)
# data["datetime"] = pd.to_datetime(data["datetime"], unit="s")
# app = dash.Dash(__name__)

# # Create the map figure using scatter_mapbox
# fig = px.scatter_mapbox(
#     data,
#     lat="lat",
#     lon="long",
#     hover_name="City",
#     zoom=2,
#     height=600,
#     mapbox_style="carto-positron",  # Use a more detailed map style
#     animation_frame="datetime",  # Specify the column for animation
# )

# # Update marker attributes based on temperature
# fig.update_traces(
#     marker=dict(
#         size=10,
#         cmax=data["Temp_max"].max(),
#         cmin=data["Temp_max"].min(),
#         color=data["Temp_max"],
#         colorscale="Viridis",  # Choose a colorscale for the temperature range
#         colorbar=dict(title="Temperature (°C)"),
#     ),
#     selector=dict(mode="markers"),  # Select the markers for updating color
# )

# # Create the dropdown menu options
# country_codes = data["country_code"].unique()
# dropdown_options = [{"label": code, "value": code} for code in country_codes]

# # Add the dropdown menu component
# dropdown = dcc.Dropdown(
#     id="country-dropdown",
#     options=dropdown_options,
#     value=None,
#     multi=True,  # Enable multiple selection
#     placeholder="Select country code(s)",
# )


# # Define the callback function to update the map based on the selected country codes
# @app.callback(Output("map-graph", "figure"), Input("country-dropdown", "value"))
# def update_map(country_codes):
#     if country_codes is None:
#         filtered_data = data
#     else:
#         filtered_data = data[data["country_code"].isin(country_codes)]
#     fig = px.scatter_mapbox(
#         filtered_data,
#         lat="lat",
#         lon="long",
#         hover_name="City",
#         zoom=2,
#         height=600,
#         mapbox_style="carto-positron",  # Use a more detailed map style
#         animation_frame="datetime",  # Specify the column for animation
#     )
#     fig.update_traces(
#         marker=dict(
#             size=10,
#             cmax=filtered_data["Temp_max"].max(),
#             cmin=filtered_data["Temp_max"].min(),
#             color=filtered_data["Temp_max"],
#             colorscale="Viridis",
#             colorbar=dict(title="Temperature (°C)"),
#         ),
#         selector=dict(mode="markers"),
#     )
#     return fig


# # Add the map figure and dropdown menu to the app layout
# app.layout = html.Div([dropdown, dcc.Graph(id="map-graph", figure=fig)])

# # Assign the server attribute
# server = app.server
# # app.run_server(debug=True)
# if __name__ == "__main__":
#     app.run_server(debug=False)


# import sqlite3
# import plotly.express as px
# import dash
# import pandas as pd

# from dash import dcc
# from dash import html
# from dash.dependencies import Input, Output
# import gc  # Import the garbage collector module


# # Read the data into a pandas DataFrame
# conn = sqlite3.connect("weather.db")
# cursor = conn.cursor()
# query = "SELECT * FROM all_weather_data"
# data = pd.read_sql_query(query, conn)
# print(data.columns)
# data["datetime"] = pd.to_datetime(data["datetime"], unit="s")
# app = dash.Dash(__name__)

# # Create the map figure using scatter_mapbox
# fig = px.scatter_mapbox(
#     data,
#     lat="lat",
#     lon="long",
#     hover_name="City",
#     zoom=2,
#     height=600,
#     mapbox_style="carto-positron",  # Use a more detailed map style
#     animation_frame="datetime",  # Specify the column for animation
# )

# # Update marker attributes based on temperature
# fig.update_traces(
#     marker=dict(
#         size=10,
#         cmax=data["Temp_max"].max(),
#         cmin=data["Temp_max"].min(),
#         color=data["Temp_max"],
#         colorscale="Viridis",  # Choose a colorscale for the temperature range
#         colorbar=dict(title="Temperature (°C)"),
#     ),
#     selector=dict(mode="markers"),  # Select the markers for updating color
# )

# # Create the dropdown menu options
# country_codes = data["country_code"].unique()
# dropdown_options = [{"label": code, "value": code} for code in country_codes]

# # Add the dropdown menu component
# dropdown = dcc.Dropdown(
#     id="country-dropdown",
#     options=dropdown_options,
#     value=None,
#     multi=True,  # Enable multiple selection
#     placeholder="Select country code(s)",
# )


# # Define the callback function to update the map based on the selected country codes
# @app.callback(Output("map-graph", "figure"), Input("country-dropdown", "value"))
# def update_map(country_codes):
#     global fig  # Declare fig as a global variable to access it within the function
#     if country_codes is None:
#         filtered_data = data
#     else:
#         filtered_data = data[data["country_code"].isin(country_codes)]

#     # Delete the old fig object before creating a new one
#     del fig
#     gc.collect()  # Perform garbage collection to clear any remaining references

#     fig = px.scatter_mapbox(
#         filtered_data,
#         lat="lat",
#         lon="long",
#         hover_name="City",
#         zoom=2,
#         height=600,
#         mapbox_style="carto-positron",  # Use a more detailed map style
#         animation_frame="datetime",  # Specify the column for animation
#     )
#     fig.update_traces(
#         marker=dict(
#             size=10,
#             cmax=filtered_data["Temp_max"].max(),
#             cmin=filtered_data["Temp_max"].min(),
#             color=filtered_data["Temp_max"],
#             colorscale="Viridis",
#             colorbar=dict(title="Temperature (°C)"),
#         ),
#         selector=dict(mode="markers"),
#     )
#     return fig


# # Add the map figure and dropdown menu to the app layout
# app.layout = html.Div([dropdown, dcc.Graph(id="map-graph", figure=fig)])

# # Assign the server attribute
# server = app.server

# if __name__ == "__main__":
#     app.run_server(debug=False)


import sqlite3
import plotly.express as px
import dash
import pandas as pd

from dash import dcc
from dash import html
from dash.dependencies import Input, Output


# Read the data into a pandas DataFrame
conn = sqlite3.connect("weather.db")
cursor = conn.cursor()
query = "SELECT * FROM all_weather_data "
data = pd.read_sql_query(query, conn)
print(data.columns)
data["datetime"] = pd.to_datetime(data["datetime"], unit="s")
app = dash.Dash(__name__)

# Create the map figure using scatter_mapbox
fig = px.scatter_mapbox(
    data,
    lat="lat",
    lon="long",
    hover_name="City",
    zoom=2,
    height=600,
    mapbox_style="carto-positron",  # Use a more detailed map style
    animation_frame="datetime",  # Specify the column for animation
)

# Update marker attributes based on temperature
fig.update_traces(
    marker=dict(
        size=10,
        cmax=data["Temp_max"].max(),
        cmin=data["Temp_max"].min(),
        color=data["Temp_max"],
        colorscale="Viridis",  # Choose a colorscale for the temperature range
        colorbar=dict(title="Temperature (°C)"),
    ),
    selector=dict(mode="markers"),  # Select the markers for updating color
)

# Create the dropdown menu options
country_codes = data["country_code"].unique()
dropdown_options = [{"label": code, "value": code} for code in country_codes]

# Add the dropdown menu component
dropdown = dcc.Dropdown(
    id="country-dropdown",
    options=dropdown_options,
    value=None,
    multi=True,  # Enable multiple selection
    placeholder="Select country code(s)",
)


# Define the callback function to update the map based on the selected country codes
@app.callback(Output("map-graph", "figure"), Input("country-dropdown", "value"))
def update_map(country_codes):
    if country_codes is None:
        filtered_data = data
    else:
        filtered_data = data[data["country_code"].isin(country_codes)]

    # Update the existing fig object instead of creating a new one
    fig.data[0].lat = filtered_data["lat"]
    fig.data[0].lon = filtered_data["long"]
    fig.data[0].hovertemplate = filtered_data["City"]
    fig.data[0].marker.cmax = filtered_data["Temp_max"].max()
    fig.data[0].marker.cmin = filtered_data["Temp_max"].min()
    fig.data[0].marker.color = filtered_data["Temp_max"]

    return fig


# Add the map figure and dropdown menu to the app layout
app.layout = html.Div([dropdown, dcc.Graph(id="map-graph", figure=fig)])

# Assign the server attribute
server = app.server

if __name__ == "__main__":
    app.run_server(debug=False)
