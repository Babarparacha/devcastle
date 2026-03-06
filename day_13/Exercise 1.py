import numpy as np
print("===== 1. CREATING ARRAYS =====")

# From Python list
arr1 = np.array([10, 20, 30, 40, 50])
print("Array from list:", arr1)

# From built-in methods
zeros_arr = np.zeros((2, 3), dtype=int)
print("\nZeros array:\n", zeros_arr)

seq_arr = np.arange(1, 11, 2)
print("\nSequential array:", seq_arr)

# From random
rand_ints = np.random.randint(0, 100, size=(2, 2))
print("\nRandom integers:\n", rand_ints)

rand_floats = np.random.rand(2, 3)
print("\nRandom floats:\n", rand_floats)


