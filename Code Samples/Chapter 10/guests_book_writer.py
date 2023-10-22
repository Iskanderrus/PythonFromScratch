from pathlib import Path

"""
Write a while loop that prompts users for their name. 
Collect all the names that are entered, and then write these names to a file called guest_book.txt. 
Make sure each entry appears on a new line in the file.
"""

path = Path('guests_book.txt')
guests = ''
ask_for_name = True

while ask_for_name:
    guests += f"{' '.join(input('What is your name? ').split()).title()}\n"

    if input('To continue type "y"\nTo stop type "q"\n').lower().strip() != 'y':
        ask_for_name = False
path.write_text(guests)
