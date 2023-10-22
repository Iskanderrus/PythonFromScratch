from pathlib import Path

"""
Write a program that prompts the user for their name. 
When they respond, write their name to a file called guest.txt.
"""

path = Path('guests.txt')
path.write_text(' '.join(input('What is your name?\n').split()).title())