def make_pizza(size: int, *toppings: str) -> None:
    """
    Print summarized pizza size and toppings for the pizza we are about to make.
    Size is a mandatory argument.
    Toppings can vary from 0 to infinity.
    """

    print(f'\nMaking a {size}-inch pizza with following topics: ')

    for topping in toppings:
        print(f'\t- {topping}')
    print(f"\n{'*' * 32}")
