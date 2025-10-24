class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return (1, self.sides)

six_sided_die = Die()
print("Rolling a 6-sided die 10 times:")
for _ in range(10):
    print(six_sided_die.roll_die(), end=" ")
print("\n")

ten_sided_die = Die(10)
print("Rolling a 10-sided die 10 times:")
for _ in range(10):
    print(ten_sided_die.roll_die(), end=" ")
print("\n")

twenty_sided_die = Die(20)
print("Rolling a 20-sided die 10 times:")
for _ in range(10):
    print(twenty_sided_die.roll_die(), end=" ")
print()

