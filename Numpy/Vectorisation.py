"""Vectorization in NumPy is the process of performing operations on entire arrays at once, rather than using explicit Python for loops to process individual elements. """

# ==========old way ===================
# list=[200,300,500]
# list2=[4,6,7]
# res=[x+y for x,y in zip(list,list2)]
# print(res)
import numpy as np
arr1=np.array([200,300,500])
# arr2=np.array([4,6,7])
# result=arr1+arr2
# print(result)
print(arr1*3) # ==============big calculation================