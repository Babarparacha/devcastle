import numpy as np
print("\n===== 3. METHODS =====")

flat = np.array([10, 50, 20, 90, 30, 40])

# Reshape
reshaped = flat.reshape((2, 3))
print("Reshaped array:\n", reshaped)

# Max / Min
print("Max value:", flat.max())
print("Min value:", flat.min())

# Argmax / Argmin
print("Index of Max:", flat.argmax())
print("Index of Min:", flat.argmin())

# Axis example
print("Column-wise max:", reshaped.max(axis=0))
print("Row-wise max:", reshaped.max(axis=1))


