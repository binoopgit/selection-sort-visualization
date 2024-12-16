import matplotlib.pyplot as plt
import time
import random

# Visualization of Selection Sort
def selection_sort_visualization(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            plt.clf()
            colors = ['skyblue'] * len(arr)
            colors[min_idx] = 'lightgreen'  # Highlight the current minimum in green
            colors[j] = 'lightcoral'  # Highlight the current comparison in red
            plt.bar(range(len(arr)), arr, color=colors)
            plt.xticks(range(len(arr)), arr, rotation=0)
            plt.title(f"Selection Sort Step: Comparing index {min_idx} with index {j}")
            plt.pause(2.0)  # Slower visualization for better understanding

            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        plt.clf()
        colors = ['skyblue'] * len(arr)
        colors[i] = 'lightgreen'  # Mark the sorted element in green
        plt.bar(range(len(arr)), arr, color=colors)
        plt.xticks(range(len(arr)), arr, rotation=0)
        plt.title(f"Selection Sort Step: Swapping index {i} with index {min_idx}")
        plt.pause(2.0)

    # Final visualization
    plt.bar(range(len(arr)), arr, color='skyblue')
    plt.xticks(range(len(arr)), arr, rotation=90)
    plt.title("Selection Sort Completed")
    plt.show()

# Example Selection Sort visualization
arr = [random.randint(1, 100) for _ in range(11)]
selection_sort_visualization(arr)
