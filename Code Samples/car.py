class Car:
    """ A simple attempt to represent a car. """

    def __init__(self, make, model, year):
        """ Initial attributes to describe a car. """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self) -> str:
        """ Return a neatly formatted descriptive name. """
        long_name = f"{self.year} {self.make.title()} {self.model.title()}"
        return long_name

    def read_odometer(self):
        """ Print a statement showing the car's current mileage. """
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage: int):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        :param mileage: Integer to set the odometer.
        :return: New odometer value.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles: int):
        """ Add the given amount to the odometer reading.
        Prevents entering negative values."""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print('You can\'t enter negative value.')


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            battery_range = 150
        elif self.battery_size == 65:
            battery_range = 225

        print(f"This car can go about {battery_range} miles on a full charge.")


class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
