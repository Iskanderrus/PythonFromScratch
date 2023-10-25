from pathlib import Path
import json

path = Path('favourite_number.json')
number = int(input('What is your favourite number? '))
contents = json.dumps(number)
path.write_text(contents)
