import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Create a figure and axis
fig, ax = plt.subplots()

# Create a line plot (initial empty data)
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
line, = ax.plot(x, y)

# Function to update the plot
def update(frame):
    # Modify the data for each frame (change the frequency of the sine wave)
    y = np.sin(x * (1 + frame * 0.1))  # Change frequency over time
    line.set_ydata(y)  # Update the y data of the plot
    return line,  # Return the updated line for blitting

# Create an animation
ani = FuncAnimation(fig, update, frames=10000, interval=50)

# Show the plot
plt.show()
