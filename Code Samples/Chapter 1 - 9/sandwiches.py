"""

Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the
sandwich that’s being ordered. Call the function three times, using a different
number of arguments each time.

"""


def sandwich_maker(ingredients):
    return ingredients


salmon_sandwich = sandwich_maker(['bread', 'cheese', 'salad', 'tomato', 'pickles', 'salmon'])

print(f'You ordered a sandwich with:')
print(*salmon_sandwich, sep=",\n")
