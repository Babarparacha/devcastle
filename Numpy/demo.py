"""NumPy, short for Numerical Python ,is the foundational open-source library for scientific computing in Python, enabling fast operations on large, multi-dimensional arrays and matrices. It provides high-performance data structures like the ndarray (n-dimensional array), along with optimized tools for mathematical, linear algebra, and statistical operations"""
import numpy as np

list=[1,2,34,5]
lists=np.array([1,2,34,5])
print(list)
print(lists)

#========== 2d array && multi array, data in rows and column===================
array_2d=np.array([[1,2,34,5],[34,5,67,89],[77,55,331,1]])
print(array_2d)
array_3d=np.array([[[1,2,34,5],[34,5,67,89],[77,55,331,1]]])
print(array_3d)