import numpy as np
print("\n===== 4. COPYING =====")

original = np.array([1, 2, 3])
copied = original.copy()
copied[0] = 99

print("Original:", original)
print("Copied:", copied)


# print("\n===== 5. APPEND & INSERT =====")

# appended = np.append(original, [4, 5])
# print("After append:", appended)

# inserted = np.insert(original, 1, 100)
# print("After insert:", inserted)


print("\n===== 6. SORTING & DELETING =====")

# messy = np.array([5, 1, 9, 3])

# sorted_arr = np.sort(messy)
# print("Sorted array:", sorted_arr)

# deleted = np.delete(sorted_arr, 1)
# print("After deleting index 1:", deleted)

