from pathlib import Path
import json

# Read data as a string and convert to a Python object
path = Path('data/all_month.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# Create more readable file with data
path = Path('data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)