from pathlib import Path

path = Path('programming.txt')

contents = 'I love programming in Python.\n'
contents += 'I love creating new games.\n'
contents += 'I also love working with data.\n'
path.write_text(contents)