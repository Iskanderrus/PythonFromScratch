from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()
lines = contents.splitlines()

digit = [_.strip() for _ in lines]

birthday = input('Type your birthday in format "mmddyy": ')

if birthday in digit:
    print('Your birthday is in the first million digits of pi.')
else:
    print('Your birthday doesn\'t appear in the first million digits of pi.')
