from pathlib import Path
import json

import plotly.express as px

# Read data as a string and convert to a Python object
path = Path('data/all_month.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# Create more readable file with data
# path = Path('data/readable_eq_data.geojson')
# readable_contents = json.dumps(all_eq_data, indent=4)
# path.write_text(readable_contents)

# Examine all earthquakes in the dataset
all_eq_dicts = all_eq_data['features']

# Extracting Magnitudes and Location Data
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = abs(eq_dict['properties']['mag'])
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# Mapping the earthquakes
title = "Global Earthquakes - Oct-Nov 2023"
fig = px.scatter_geo(lat=lats,
                     lon=lons,
                     size=mags,
                     title=title,
                     color=mags,
                     color_continuous_scale='Viridis',
                     labels={'color': 'Magnitude'},
                     projection='natural earth',
                     )
fig.show()