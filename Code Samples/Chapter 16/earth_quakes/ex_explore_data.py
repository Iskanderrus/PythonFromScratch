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
title = all_eq_data['metadata']['title']

# Getting the mapping data
mags = [abs(eq_dict['properties']['mag']) for eq_dict in all_eq_dicts]
lons = [eq_dict['geometry']['coordinates'][0] for eq_dict in all_eq_dicts]
lats = [eq_dict['geometry']['coordinates'][1] for eq_dict in all_eq_dicts]
eq_titles = [eq_dict['properties']['title'] for eq_dict in all_eq_dicts]

# Mapping the earthquakes
fig = px.scatter_geo(lat=lats,
                     lon=lons,
                     size=mags,
                     title=title,
                     color=mags,
                     color_continuous_scale='Viridis',
                     labels={'color': 'Magnitude'},
                     projection='natural earth',
                     hover_name=eq_titles,
                     )
fig.show()
