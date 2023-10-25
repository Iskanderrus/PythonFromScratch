from pathlib import Path
import json

path = Path('favourite_number.json')

if path.exists():
    contents = path.read_text()
    number = json.loads(contents)
    print(f'I know your favourite number. It\'s {number}!')

else:
    number = int(input('What is your favourite number? '))
    contents = json.dumps(number)
    path.write_text(contents)

