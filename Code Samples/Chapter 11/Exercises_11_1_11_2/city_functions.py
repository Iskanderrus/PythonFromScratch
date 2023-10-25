def simple_city_function(city: str, country: str, population=0) -> str:
    if population:
        if isinstance(population, int):
            return f'{city.strip().title()}, {country.strip().title()} - population: {population}'
        elif isinstance(population, str) and ',' in population and '.' in population:
            population = population.replace(",", "")
            population = float(population)
            return f'{city.strip().title()}, {country.strip().title()} - population: {round(population, 2)}'
        else:
            return f'{city.strip().title()}, {country.strip().title()} - population: {int(population)}'
    else:
        return f'{city.strip().title()}, {country.strip().title()}'