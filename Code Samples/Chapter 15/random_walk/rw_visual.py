import matplotlib.pyplot as plt

from random_walk import RandomWalk


while True:
    num_points = int(input("How many points? "))
    num_directions = int(input("How many directions? "))
    # Make a random walk
    rw = RandomWalk(num_points=num_points, num_directions=num_directions)
    rw.fill_walk()

    # Plot the points of the walk

    plt.style.use('seaborn-v0_8-dark-palette')
    fig, ax = plt.subplots()

    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.plasma, edgecolors='none', s=2.5)
    ax.set_aspect('equal')
    plt.show()

    keep_running = input("Make another walk? (y/n)").strip().lower()
    if keep_running == 'n':
        break
