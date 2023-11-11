import matplotlib.pyplot as plt

x_values = [x for x in range(1, 101) if x % 2 == 0]
y_values = [x ** 2 for x in range(1, 101) if x % 2 == 0]

plt.style.use('seaborn-v0_8-dark-palette')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.gist_ncar, s=10)

# Set chart title and label axes
ax.set_title("Square Even Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(labelsize=14)

# Set the range for each axis
ax.axis([0, 110, 0, 11_000])
ax.ticklabel_format(style='plain')

plt.show()
