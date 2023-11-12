import plotly.express as px
from die import Die

# Create a die instance with 6 sides
die = Die(num_sides=int(input("How many sides has your die? ")))

# Make some rolls, and store results in a list
results = [die.roll() for x in range(1000)]

# Analyse the results
frequencies = [results.count(value) for value in range(1, die.num_sides+1)]

# Visualize the results
fig = px.bar(x=range(1, die.num_sides+1), y=frequencies)
fig.show()
