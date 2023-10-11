def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make"""
    print(f'\nMaking a {size}-inch pizza with following topics: ')
    for topping in toppings:
        print(f'\t- {topping}')
    print(f"\n{'*' * 32}")
