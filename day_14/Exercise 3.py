import numpy as np
print("\n===== 3. BROADCASTING =====")

a = np.array([10, 20, 30])

# Add scaler
# print("Add 5 to each element:", a + 5)

# Broadcasting with another array
# b = np.array([1, 2, 3])
# print("Element-wise addition:", a ** b)


# print("\n===== 4. TYPE CASTING =====")

float_arr = np.array([2, 1, 3.8])
print("Original arr:", float_arr)

print("Original dtype:", float_arr.dtype)

int_arr = float_arr.astype(int)
print("Converted to int:", int_arr)
print("New dtype:", int_arr.dtype)