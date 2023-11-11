import matplotlib.pyplot as plt
from random import choice
from random_walk import RandomWalk
from matplotlib import colormaps


color_maps = list(colormaps)

while True:
    num_points = int(input("How many points? "))
    num_directions = int(input("How many directions? "))
    # Make a random walk
    rw = RandomWalk(num_points=num_points, num_directions=num_directions)
    rw.fill_walk()

    # Plot the points of the walk

    plt.style.use('seaborn-v0_8-dark-palette')
    fig, ax = plt.subplots(figsize=(15, 9))

    point_numbers = range(rw.num_points)
    color_map = choice(color_maps)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=color_map, edgecolors='none', s=1)
    # Remove axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    ax.set_aspect('equal')
    ax.scatter(0, 0, c='green', edgecolors='none', s=15)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=15)

    plt.show()

    keep_running = input("Make another walk? (y/n)").strip().lower()
    if keep_running == 'n':
        break
