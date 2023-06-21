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
query = "SELECT * FROM all_weather_data"
data = pd.read_sql_query(query, conn)
print(data.columns)
data["datetime"] = pd.to_datetime(data["datetime"], unit="s")
app = dash.Dash(__name__)

# Create the map figure using scatter_mapbox
fig = px.scatter_mapbox(
    pd.DataFrame(columns=["lat", "long", "City", "Temp_max"]),
    lat="lat",
    lon="long",
    hover_name="City",
    zoom=2,
    height=600,
    mapbox_style="carto-darkmatter",  # Use a more detailed map style
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

# Create the dropdown menu options for datetime
datetime_options = (
    pd.to_datetime(data["datetime"]).dt.strftime("%Y-%m-%d %H:%M:%S").unique()
)
datetime_dropdown_options = [{"label": dt, "value": dt} for dt in datetime_options]

# Create the dropdown menu options for country codes
country_code_options = data["country_code"].unique()
country_code_dropdown_options = [
    {"label": code, "value": code} for code in country_code_options
]

# Add the datetime dropdown menu component
datetime_dropdown = dcc.Dropdown(
    id="datetime-dropdown",
    options=datetime_dropdown_options,
    value=None,
    multi=True,  # Enable multiple selection
    placeholder="Select datetime(s)",
)

# Add the country code dropdown menu component
country_code_dropdown = dcc.Dropdown(
    id="country-code-dropdown",
    options=country_code_dropdown_options,
    value=None,
    multi=True,  # Enable multiple selection
    placeholder="Select country code(s)",
)


@app.callback(
    Output("map-graph", "figure"),
    [Input("country-code-dropdown", "value")],
)
def update_map(country_codes):
    if country_codes is not None:
        filtered_data = data[data["country_code"].isin(country_codes)]
    else:
        filtered_data = pd.DataFrame(columns=["lat", "long", "City", "Temp_max"])

    fig = px.scatter_mapbox(
        filtered_data,
        lat="lat",
        lon="long",
        hover_name="City",
        hover_data=["Temp_max"],  # Include Temp_max in the hover data
        zoom=2,
        height=600,
        mapbox_style="carto-darkmatter",  # Use a more detailed map style
    )
    fig.update_traces(
        marker=dict(
            size=10,
            cmax=filtered_data["Temp_max"].max(),
            cmin=filtered_data["Temp_max"].min(),
            color=filtered_data["Temp_max"],
            colorscale="Viridis",
            colorbar=dict(title="Temperature (°C)"),
        ),
        selector=dict(mode="markers"),
    )
    return fig


# Add the map figure and dropdown menus to the app layout
app.layout = html.Div(
    [datetime_dropdown, country_code_dropdown, dcc.Graph(id="map-graph", figure=fig)]
)

# Assign the server attribute
server = app.server
# app.run_server(debug=True)
if __name__ == "__main__":
    app.run_server(debug=False)
