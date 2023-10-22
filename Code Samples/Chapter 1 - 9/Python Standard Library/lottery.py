import string
from random import choice, shuffle, sample

characters = string.ascii_lowercase + string.ascii_uppercase
numbers = string.digits

equals = False
counter = 0


while not equals:
    symbols_list = []
    for _ in range(10):
        symbols_list.append(choice(characters))

    for _ in range(5):
        symbols_list.append(choice(numbers))

    shuffle(symbols_list)
    my_winning_combination = "".join(sample(symbols_list, 4))

    winning_symbols = sample(symbols_list, 4)
    winning_combination = "".join(winning_symbols)
    print(winning_combination)
    counter += 1
    if my_winning_combination == winning_combination:
        equals = True
print(counter)

