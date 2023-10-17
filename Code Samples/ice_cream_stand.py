from restaurant import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Chocolate', 'Banana', 'Vanilla', 'Karadut']

    def display_flavors(self):
        print(f'In {self.restaurant_name.title()} we serve following flavors of Ice Cream:')
        for flavor in self.flavors:
            print(f'\t\t- {flavor}')


dondurma = IceCreamStand('Kulahi', 'Turkish Ice Cream')
dondurma.describe_restaurant()
dondurma.display_flavors()
