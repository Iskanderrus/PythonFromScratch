import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk
rw = RandomWalk(num_points=50000, num_directions=12)
rw.fill_walk()

# Plot the points of the walk

plt.style.use('seaborn-v0_8-dark-palette')
fig, ax = plt.subplots()

ax.scatter(rw.x_values, rw.y_values, c=rw.y_values, cmap=plt.cm.plasma, s=2.5)
ax.set_aspect('equal')
plt.show()

