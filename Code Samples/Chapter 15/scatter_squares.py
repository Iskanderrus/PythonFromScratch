import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-dark-palette')
fig, ax = plt.subplots()
ax.scatter([x for x in range(1, 11) if x % 2 == 0],
           [x ** 2 for x in range(1, 11) if x % 2 == 0])

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(labelsize=14)

plt.show()
