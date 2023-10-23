"""
How do I find all files with .txt extension if one directory.
And in subdirestories.
"""

from pathlib import Path

path = Path('../../../../Downloads/')
files = list(path.glob('*.txt'))
for file in files:
    print(f'Files in my directory are: {str(file).split("/")[-1]}')

files = list(path.glob('**/*.txt'))
print('Files including subdirectories are: ')
for file in files:
    print(str(file).split('/')[-1])