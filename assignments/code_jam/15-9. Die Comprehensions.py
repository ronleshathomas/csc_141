from random import randint

class Die:
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        """Assume a six-sided die by default."""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)


import matplotlib.pyplot as plt

die_1 = Die()
die_2 = Die()


results = [die_1.roll() + die_2.roll() for _ in range(1000)]


max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result + 1)]


plt.style.use('classic')
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(range(2, max_result + 1), frequencies, color='steelblue', edgecolor='black')


ax.set_title("Results of Rolling Two D6 Dice (Using List Comprehensions)", fontsize=14)
ax.set_xlabel("Sum of Two Dice", fontsize=12)
ax.set_ylabel("Frequency", fontsize=12)

plt.show()
