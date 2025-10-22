from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        self.num_points = num_points

        # All walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""
        while len(self.x_values) < self.num_points:
            # Choose direction and distance for x and y
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)


import matplotlib.pyplot as plt

# Create a random walk
rw = RandomWalk(5000)
rw.fill_walk()

# Plot the points using a line instead of scatter
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(10, 6))

# Use plot() instead of scatter()
ax.plot(rw.x_values, rw.y_values, linewidth=1)

# Emphasize the start and end points
ax.plot(0, 0, c='green', marker='o')  # Start point
ax.plot(rw.x_values[-1], rw.y_values[-1], c='red', marker='o')  # End point

# Remove the axes for a cleaner look
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.title("Molecular Motion Simulation", fontsize=14)
plt.show()
