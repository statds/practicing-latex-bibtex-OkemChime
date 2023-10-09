import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]

# Create a scatter plot
plt.scatter(x, y)
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Scatter Plot Example')

# Save the figure to a file (e.g., "scatter_plot.png")
plt.savefig('scatter_plot.png')

# Display the plot (optional)
plt.show()
