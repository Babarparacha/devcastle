
"""
without modifying data change dimension ,re-shapes,convert 1d to 2d , 2d to 3d array
reshape(row,column)
reshape only if dimension matches. does not create copy it's create a view
"""
import numpy as np
array_1d=np.array([1,2,3,4,5,6])
print(array_1d.reshape(2,3)) #array dimension should be same
# 2- flatting arrays- multi-dimension->1d Array
# i-ravel-it return a view-> MODIFY ORIGINAL ARRAY
array_2d=np.array([[1,2,3],[4,5,6]])
# print("ravel",array_2d.ravel())
# 2-flatten- returns a copy- not changes
# print("flatten",array_2d.flatten())
# output same for flatten or ravel 
