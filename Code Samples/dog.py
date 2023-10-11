class Dog:
    """

    A simple attempt to build a Dog Class

    """

    def __init__(self, name: str, age: int, color: str):
        """Initialize name, age and color attributes"""
        self.name = name
        self.age = age
        self.color = color

    def sit(self):
        """Simulates a dog sitting in response to a command"""
        print(f'{self.name} is now sitting.')

    def roll_over(self):
        """Simulates a dog rolling over in response to a command"""
        print(f'{self.name} rolled over!')


my_dog = Dog(name='Aljka', age=30, color='Red')
my_dog.height = 50

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
print(f'{my_dog.name} is {my_dog.height} cm high.')
my_dog.roll_over()

brother_dog = Dog('Archi', 6, 'White-black')

print(f"\nMy brother's dog's name is {brother_dog.name}.")
print(f"My brother's dog is {brother_dog.age} years old.")
brother_dog.sit()

if my_dog.age > brother_dog.age:
    print(f'\n{my_dog.name} is older than {brother_dog.name}')
else:
    print(f'{brother_dog.name} is older than {my_dog.name}')
