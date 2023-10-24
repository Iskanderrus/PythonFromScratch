from pathlib import Path

files = ['cats.txt', 'dogs.txt']

for file in files:
    try:
        path = Path(file)
        contents = path.read_text()
    except FileNotFoundError:
        # print(f'\nFile {file} is not found in this directory.')
        pass
    else:
        names = contents.splitlines()
        print(f"\nNames of the {str(path).split('.')[0]} are: ")
        for name in names:
            print(f'\t- {name}')
