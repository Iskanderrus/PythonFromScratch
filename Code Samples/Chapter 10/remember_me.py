from pathlib import Path
import json

path = Path('username.json')
if path.exists():
    contents = path.read_text()
    stored_name = json.loads(contents)
    print(f"Hi, {stored_name}! Nice to see you again!")
else:
    username = input('What is your name? ')
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember youi when you come back, {username}!")
