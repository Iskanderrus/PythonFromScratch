class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank_capacity = 55
        self.fuel = 0
        self.consumption = 5

    def increment_fuel(self, number):
        if number >= 0:
            self.fuel += number
        else:
            print("You are not allowed to pump the gas from my tank!!!")

    def read_fuel(self):
        print(f'Currently the gas tank holds {self.fuel} liters of gas.')

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f'This car has {self.odometer_reading} miles on it.')

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles > 0:
            if self.fuel > 0:
                self.odometer_reading = miles
                self.fuel -= (miles * self.consumption) / 100
            else:
                print('Add gas first.')
        else:
            print('You can\'t roll back an odometer by negative increment!')


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

# updating odometer Option I
my_new_car.odometer_reading = 45
my_new_car.read_odometer()

# updating odometer Option II
my_new_car.update_odometer(55)
my_new_car.read_odometer()

# updating odometer Option III
my_new_car.increment_odometer(25)
my_new_car.read_odometer()


# Inheritance

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def increment_gas_tank_capacity(self, number):
        """Elecric cars do not require gas"""
        print('This car doesn\'t have a tank, dude. ')


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f'This car has a {self.battery_size}-kWh battery.')

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.read_odometer()
my_leaf.increment_gas_tank_capacity(25)
print(my_new_car.gas_tank_capacity)
my_new_car.increment_fuel(25)
my_new_car.increment_odometer(150)
print(my_new_car.fuel)
my_leaf.battery.get_range()
