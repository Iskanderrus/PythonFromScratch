from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
#print(contents, end='')


# accessing lines within txt file

lines = contents.splitlines()
for line in lines:
    print(f'This is a new line with following digits: {line}')

# combining all the digits into one number

digit = float(''.join([x.strip() for x in lines]))

print(type(digit))