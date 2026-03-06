import numpy as np
print("\n===== 2. INDEXING & SELECTION =====")

arr = np.array([[5, 15, 25],
                [35, 45, 55],
                [65, 75, 85]])

print("Array:\n", arr)

# # Access single element
# print("Element at row 1, col 2:", arr[1, 2])

# Access full row
# print("Row 0:", arr[0])

# # Access full column
# print("Column 1:", arr[:, 1])

# # Slicing
# print("First two rows:\n", arr[:2, :])

# Logical selection
print("Values greater than 40:", arr[arr > 40])
