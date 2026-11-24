import numpy as np

# Create 1D array from 1 to 10
arr = np.arange(1, 11)
print("Original Array:", arr)

# Slicing operations
first_five = arr[:5]
elements_step2 = arr[::2]

print("First 5 elements:", first_five)
print("Every second element:", elements_step2)

# Statistical measures
print("Sum:", arr.sum())
print("Mean:", arr.mean())
print("Maximum:", arr.max())
print("Minimum:", arr.min())

# Broadcasting modification
arr_modified = arr + 10
print("Array after broadcasting (+10):", arr_modified)


'''output:
Original Array: [ 1  2  3  4  5  6  7  8  9 10]
First 5 elements: [1 2 3 4 5]
Every second element: [1 3 5 7 9]
Sum: 55
Mean: 5.5
Maximum: 10
Minimum: 1
Array after broadcasting (+10): [11 12 13 14 15 16 17 18 19 20]    ''
