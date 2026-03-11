import numpy as np
print("task 1")

#====create a 1D array containing numbers from 10 to 50===
arr_1d=np.arange(10,51)
# print(arr_1d)

#====Create a 3×3 matrix filled with zeros====

arr_zeros=np.zeros((3,3))
# print(arr_zeros)

#========Create a 4×4 matrix with random integers between 1 and 100====

random_4x_matrix=np.random.randint(1,101,size=(4,4))
print(random_4x_matrix)

# TASK 2 - Array Attributes

# ====Number of dimensions-====
# print("Number of dimensions",random_4x_matrix.ndim)
# print("Shape of the array",random_4x_matrix.shape)
# print("Total number of elements",random_4x_matrix.size)
# print(" Data type of elements",random_4x_matrix.dtype)

# =======Task 3- indexing & selection ==========


arr = [[10,20,30], [40,50,60],[70,80,90]]

# print(f"Element 50: {arr[1][1]}")
# print(f"Second row: {arr[1]}")
# arr = np.array(arr)
# print(f"third_column = {arr[:, 2]}")
# values = arr[arr > 40]
# print(f"Values greater than 40: {values}")

# =====task 4- boradcastring==========

arr_broadcast=[5,10,15,20,25]
# arr_broadcasted = np.array(arr_broadcast) 
# print(f"Add 10 to every element: {arr_broadcasted + 10}")
# print(f"Multiply every element by 2: {arr_broadcasted * 2}")
# print(f"Square each element: {arr_broadcasted ** 2}")

# =====Task 5 – Mathematical Operations==========
A = [2,4,6]
B = [1,3,5] 
A=np.array(A)
B=np.array(B)
# print(f"Addition (A + B): {A + B}")
# print(f"Subtraction (A - B): {A - B}")
# print(f"Multiplication (A * B): {A * B}")
# print(f"Division (A / B): {A / B}")
# print(f"Exponentiation (A ** B): {A ** B}")

# ====TASK 6 - Statistical Functions======

random_data = np.random.randint(1, 101, size=20)
# print(f"Generated Data (20 random numbers 1-100):")
# print(random_data)
# print(f"Mean: {np.mean(random_data)}")
# print(f"Median: {np.median(random_data)}")
# print(f"Standard Deviation: {np.std(random_data)}")
# print(f"Maximum Value: {np.max(random_data)}")
# print(f"Minimum Value: {np.min(random_data)}")

#===== Create array from 1 to 12 using arrange() & Reshape into different dimensions:====
task_7=np.arange(1,13)
# print(f"3 by 4: {task_7.reshape(3,4)}")
# print(f"4 by 3: {task_7.reshape(4,3)}")

#=====Bonus Challenge – Advanced Operations====
array_5x=np.random.randint(1, 102, size=(5, 5))
# print(array_5x)
# print(f"Row-wise maximum values: {np.max(array_5x,axis=1)}")
# print(f"Row-wise minimum values: {np.min(array_5x,axis=1)}")
# Replace values greater than 80 with 80
array_5x[array_5x > 80] = 80
# print(f" Replace values greater than 80 with 80 {array_5x}")