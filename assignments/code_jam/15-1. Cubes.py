import matplotlib.pyplot as plt

# First 5 cubic numbers
numbers = list(range(1, 6))
cubes = [n**3 for n in numbers]

plt.figure(figsize=(6, 4))
plt.plot(numbers, cubes, marker='o')
plt.title("First Five Cubic Numbers")
plt.xlabel("Number")
plt.ylabel("Cube of Number")
plt.grid(True)
plt.show()

# First 5,000 cubic numbers
numbers = list(range(1, 5001))
cubes = [n**3 for n in numbers]

plt.figure(figsize=(10, 5))
plt.plot(numbers, cubes)
plt.title("First 5,000 Cubic Numbers")
plt.xlabel("Number")
plt.ylabel("Cube of Number")
plt.grid(True)
plt.show()

