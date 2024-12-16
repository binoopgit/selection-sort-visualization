# Selection Sort Visualization

This project provides a simple visualization of the Selection Sort algorithm using Python and Matplotlib. The visualization demonstrates how the algorithm works by showing the step-by-step process of finding the minimum element and swapping it with the current index.

## Selection Sort Overview

Selection Sort is a simple comparison-based sorting algorithm. It works by dividing the list into two parts: a sorted section and an unsorted section. At each step, it selects the smallest element from the unsorted section and swaps it with the leftmost unsorted element, expanding the sorted section.

### How it Works:
1. **Find the Minimum**:
   - Start from the first element in the unsorted section and find the smallest element.
2. **Swap**:
   - Swap the smallest element with the leftmost unsorted element.
3. **Expand the Sorted Section**:
   - Move the boundary of the sorted section to include the newly sorted element.
4. **Repeat**:
   - Repeat the process until the entire list is sorted.

### Example:
Consider the list `[64, 34, 25, 12]`:
- **First Pass**:
  - Find the smallest element (`12`) and swap it with the first element. List becomes: `[12, 34, 25, 64]`.
- **Second Pass**:
  - Find the smallest element in the remaining unsorted section (`25`) and swap it with the second element. List becomes: `[12, 25, 34, 64]`.
- **Subsequent Passes**:
  - Continue this process until the entire list is sorted.

### Time Complexity:
- **Best Case**: O(n²)
- **Average Case**: O(n²)
- **Worst Case**: O(n²)

Selection Sort is not efficient for large datasets due to its quadratic time complexity, but it is simple to implement and useful for small datasets.

---

## Prerequisites

To run this code, you will need:

- Python 3.x
- Matplotlib library

You can install Matplotlib using pip:
```bash
pip install matplotlib

## How the Visualization Works

The algorithm iteratively selects the smallest element from the unsorted section and swaps it with the leftmost unsorted element.

The visualization highlights:
- **Green bar**: The current minimum element.
- **Red bar**: The element being compared.
- After each pass, the sorted elements are marked in green.

## Features

- Step-by-step visualization of the Selection Sort algorithm.
- Comparisons are highlighted in red, and the current minimum is highlighted in green.
- The sorting process is intentionally slowed down for easier comprehension.

## Example

An array of 11 random elements is generated, and the sorting process is displayed in real time.

## Customization

- You can change the number of elements in the list by modifying the line:
  ```python
  arr = [random.randint(1, 100) for _ in range(11)]

-  You can adjust the speed of the visualization by modifying the plt.pause() value.

## License

This project is open source and available under [MIT](https://choosealicense.com/licenses/mit/)# selection-sort-visualization
