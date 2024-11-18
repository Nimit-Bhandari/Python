import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Bubble Sort function that visually updates the plot
def bubble_sort_visual(arr, update_plot):
    n = len(arr)
    # Yield control after every swap (not after every full pass)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap the elements
                update_plot(arr)  # Update the plot after each swap
                yield  # Yield control to animation

# Function to update the plot
def update_plot(arr):
    for rect, val in zip(bars, arr):  # Update each bar's height
        rect.set_height(val)
    plt.draw()

# Initialize the data and the plot
arr = np.random.randint(1,100,20)
fig, ax = plt.subplots()
bars = ax.bar(range(len(arr)), arr, align='center')

# Set up the animation
ani = FuncAnimation(fig, lambda i: next(bubble_sort_visual(arr, update_plot)), 
                    frames=bubble_sort_visual(arr, update_plot), repeat=False)

# Display the plot
plt.show()
