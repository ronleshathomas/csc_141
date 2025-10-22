import matplotlib.pyplot as plt

# Generate data for cubes
numbers = list(range(1, 5001))
cubes = [n**3 for n in numbers]

# Create scatter plot with colormap
plt.figure(figsize=(10, 6))
plt.scatter(numbers, cubes, c=cubes, cmap=plt.cm.viridis, s=10)

# Add title and labels
plt.title("Colored Cubes", fontsize=14)
plt.xlabel("Number", fontsize=12)
plt.ylabel("Cube of Number", fontsize=12)

# Add colorbar and grid
plt.colorbar(label="Cube Value")
plt.grid(True)

# Show the plot
plt.show()

