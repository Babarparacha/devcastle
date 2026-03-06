import numpy as np
print("\n===== 7. CONCATENATE & SPLIT =====")

arrA = np.array([[1, 2], [3, 4]])
arrB = np.array([[5, 6], [7, 8]])

# Concatenate vertically
concat_v = np.concatenate((arrA, arrB), axis=0)
print("Vertical Concatenation:\n", concat_v)

# Concatenate horizontally
concat_h = np.concatenate((arrA, arrB), axis=1)
print("Horizontal Concatenation:\n", concat_h)

# Split
flat_arr = np.array([1, 2, 3, 4, 5, 6,])
split_arr = np.array_split(flat_arr, 3)

merged = np.array([])  # start empty

for part in split_arr:
    merged = np.concatenate((merged, part))

print("Merged array1:", merged)

merged = np.concatenate((split_arr),axis=0,dtype=int)
print("Merged array2:", merged)