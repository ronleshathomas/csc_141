from random import randint

class Die:

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)
    
import matplotlib.pyplot as plt

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = [die_1.roll() + die_2.roll() + die_3.roll() for _ in range(1000)]

max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(value) for value in range(3, max_result + 1)]

plt.style.use('classic')
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(range(3, max_result + 1), frequencies, color='lightgreen', edgecolor='black')

ax.set_title("Results of Rolling Three D6 Dice 1,000 Times", fontsize=14)
ax.set_xlabel("Sum of Three Dice", fontsize=12)
ax.set_ylabel("Frequency", fontsize=12)

ax.set_xticks(range(3, max_result + 1))

plt.show()

