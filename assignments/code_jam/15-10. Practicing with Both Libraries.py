from random import randint, choice
import matplotlib.pyplot as plt


# --- Die Class ---
class Die:
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        """Assume a six-sided die by default."""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)


# --- RandomWalk Class ---
class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Determine the direction and distance for a step."""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance

    def fill_walk(self):
        """Generate all the points in the random walk."""
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)


# --- Matplotlib Dice Visualization ---
def matplotlib_dice():
    die_1 = Die()
    die_2 = Die()

    # Roll two D6 dice 1000 times
    results = [die_1.roll() + die_2.roll() for _ in range(1000)]

    # Analyze results
    max_result = die_1.num_sides + die_2.num_sides
    frequencies = [results.count(value) for value in range(2, max_result + 1)]

    # Plot with Matplotlib
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(range(2, max_result + 1), frequencies, color='skyblue', edgecolor='black')

    ax.set_title("Matplotlib: Results of Rolling Two D6 Dice 1,000 Times", fontsize=14)
    ax.set_xlabel("Sum of Two Dice", fontsize=12)
    ax.set_ylabel("Frequency", fontsize=12)
    ax.set_xticks(range(2, max_result + 1))

    plt.show()


# --- Plotly Random Walk Visualization ---
def plotly_random_walk():
    rw = RandomWalk(5000)
    rw.fill_walk()

    fig = px.scatter(
        x=rw.x_values,
        y=rw.y_values,
        color=list(range(rw.num_points)),
        color_continuous_scale='Viridis',
        title="Plotly: Random Walk (Interactive)",
        labels={'x': 'X Position', 'y': 'Y Position'},
    )

    fig.update_layout(
        showlegend=False,
        xaxis=dict(showgrid=False, visible=False),
        yaxis=dict(showgrid=False, visible=False),
    )

    fig.show()


# --- Main Menu ---
def main():
    print("🎲 Exercise 15-10: Practicing with Both Libraries")
    print("Choose a visualization:")
    print("1️⃣  Matplotlib Dice Simulation")
    print("2️⃣  Plotly Random Walk Visualization")
    choice_input = input("\nEnter 1 or 2: ")

    if choice_input == "1":
        matplotlib_dice()
    elif choice_input == "2":
        plotly_random_walk()
    else:
        print("Invalid choice. Please run again and enter 1 or 2.")


