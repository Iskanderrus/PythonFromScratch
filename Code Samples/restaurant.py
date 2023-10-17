"""

Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message
indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods.

"""


class Restaurant:

    def __init__(self, name, cuisine):
        self.restaurant_name = name
        self.cuisine_type = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a restaurant serving the best {self.cuisine_type} food in our city.")

    def set_number_served(self, number):
        if number >= self.number_served:
            self.number_served = number
        else:
            print('You are not allowed to cut number of served persons!')

    def increment_number_served(self, number):
        if number >= 0:
            self.number_served += number
        else:
            print('You are not allowed to cut number of served persons by incrementing negatively!')


# umit_usta = Restaurant("Umit Usta", 'Turkish')
# print(umit_usta.restaurant_name)
# print(umit_usta.cuisine_type)
# umit_usta.describe_restaurant()
#
# """Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance."""
#
# giovanni = Restaurant("Giovanni", 'Italian')
# yakitoria = Restaurant('Yakitoria', 'Japanese')
# korchma = Restaurant('Taras Bulba', 'Ukranian')
#
# giovanni.describe_restaurant()
# yakitoria.describe_restaurant()
# korchma.describe_restaurant()
#
# print(f'There were {giovanni.number_served} customers served in the {giovanni.restaurant_name.title()} Restaurant.')
# giovanni.set_number_served(30)
# print(f'There were {giovanni.number_served} customers served in the {giovanni.restaurant_name.title()} Restaurant.')
# giovanni.set_number_served(-5)
# print(f'There were {giovanni.number_served} customers served in the {giovanni.restaurant_name.title()} Restaurant.')
# giovanni.increment_number_served(6)
# print(f'After the party at the {giovanni.restaurant_name.title()} the number of customers is {giovanni.number_served}')
