"""

Write a function that stores information about a car in a dictionary.
The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the
function with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:

car = make_car('subaru', 'outback', color='blue', tow_package=True)

Print the dictionary that’s returned to make sure all the information was
stored correctly.

'"""


def car_db(manufacturer, model_name, **car_data) -> dict:
    car_data['manufacturer'] = manufacturer
    car_data['model_name'] = model_name
    return car_data


my_car = car_db('Opel', 'Astra', engine=1.8, gear='manual', year=2008, number_of_owners=2)
for k,v in my_car.items():
    print(f'Your car\'s {k} is {v}.')
