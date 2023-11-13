from pathlib import Path
import csv
import plotly.express as px

path = Path('data/MODIS_C6_1_Russia_Asia_7d.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract latitude, longitude and brightness
lats, lons, brights = [], [], []

for row in reader:
    lat = float(row[0])
    lon = float(row[1])
    bright = float(row[2])
    lats.append(lat)
    lons.append(lon)
    brights.append(bright)

# Mapping the earthquakes
fig = px.scatter_geo(lat=lats,
                     lon=lons,
                     size=brights,
                     title='Fires in Russia and Asia last 7 days',
                     color=brights,
                     color_continuous_scale='OrRd',
                     labels={'color': 'Brightness'},
                     projection='natural earth',
                     )
fig.update_geos(
    visible=False, resolution=50, fitbounds="locations",
    showcountries=True, countrycolor="Black",
    showsubunits=True, subunitcolor="Blue"
)
fig.write_image('fires_in_russia_and_asia_11132023.jpg')