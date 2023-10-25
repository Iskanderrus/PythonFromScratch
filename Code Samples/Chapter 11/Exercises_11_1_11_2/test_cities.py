from city_functions import simple_city_function


def test_simple_city_function():
    """ Do city name and country name work? """
    formatted_data = simple_city_function('moscow', 'russia')
    assert formatted_data == "Moscow, Russia"


def test_simple_city_function_with_population():
    """ Do city name, country name and valid population number work? """
    formatted_data = simple_city_function('moscow', 'russia', 15_000_000)
    assert formatted_data == "Moscow, Russia - population: 15000000"


def test_simple_city_function_with_population_as_a_string():
    """ Do city name, country name and valid population number work? """
    formatted_data = simple_city_function('moscow', 'russia', '15_000_000')
    assert formatted_data == "Moscow, Russia - population: 15000000"


def test_simple_city_function_with_population_as_a_string_in_uk_format():
    """ Do city name, country name and valid population number work? """
    formatted_data = simple_city_function('moscow', 'russia', '15,000,000.05')
    assert formatted_data == "Moscow, Russia - population: 15000000.05"
