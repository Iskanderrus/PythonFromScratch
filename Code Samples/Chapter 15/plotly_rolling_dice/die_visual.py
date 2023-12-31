import plotly.express as px
from die import Die

# Create a die instance
sides_1 = int(input("How many sides has your first die? "))
sides_2 = int(input("How many sides has your second die? "))

die_1 = Die(num_sides=sides_1)
die_2 = Die(num_sides=sides_2)

rolls = int(input("How many times do you want to roll the die? "))

# Make some rolls, and store results in a list
results = [die_1.roll() + die_2.roll() for x in range(rolls)]

# Analyse the results
frequencies = [results.count(value) for value in range(1, die_1.num_sides+die_2.num_sides+1)]

# Visualize the results
title = f"Results of Rolling a Die with {die_1.num_sides} Sides and a Die with {die_2.num_sides} Sides {rolls:,} Times"
labels = {'x': "Result",
          'y': "Frequency of Result"}
fig = px.bar(x=range(2, die_1.num_sides + die_2.num_sides+1), y=frequencies, title=title, labels=labels)

# Further customization of the chart
fig.update_layout(xaxis_dtick=1)

# Immediate display of the chart
#fig.show()

# Saving the chart into HTML file
fig.write_html('dice_visual_d6d10.html')