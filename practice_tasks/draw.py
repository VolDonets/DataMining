import numpy as np
import matplotlib.pyplot as plt

# Generate x values from 0 to 2π with a step of 0.1
x = np.arange(0, 6 * np.pi, 0.1)

# Calculate sine and cosine values
y_sin = np.sin(x)
y_cos = np.cos(x)

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(x, y_sin, label='Sine')
plt.plot(x, y_cos, label='Cosine')

# Set labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine and Cosine Functions')

# Add legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
