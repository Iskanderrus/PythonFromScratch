import plotly.express as px
from die import Die

# Create a die instance with 6 sides
die = Die(num_sides=int(input("How many sides has your die? ")))
rolls = int(input("How many times do you want to roll the die? "))
# Make some rolls, and store results in a list
results = [die.roll() for x in range(rolls)]

# Analyse the results
frequencies = [results.count(value) for value in range(1, die.num_sides+1)]

# Visualize the results
title = f"Results of Rolling One Die with {die.num_sides} Sides {rolls} Times"
labels = {'x': "Result",
          'y': "Frequency of Result"}
fig = px.bar(x=range(1, die.num_sides+1), y=frequencies, title=title, labels=labels)
fig.show()
