from random import randint, choice

# randint returns a random integer in range from a to b inclusively
print(randint(1, 6))

# choice returns a random value from list or tuple
players_list = ['charles', 'martina', 'michael', 'florence', 'eli']
players_tuple = ('charles', 'martina', 'michael', 'florence', 'eli')

print(choice(players_list))
print(choice(players_tuple))

