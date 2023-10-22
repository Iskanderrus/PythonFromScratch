from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text().splitlines()

for line in contents:
    print(line.strip())

for line in contents:
    print(line.strip().replace('Python', 'C'))
