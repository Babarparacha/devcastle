# creation arrayoperation
import numpy as np
# c--------------heck shape and size-----------------
# array_1d=np.array([1,2,34,5,6])
# array_1d=np.array([1.1,2.2,3.3,5.5,6.6])
array_1d=np.array([1,2,34,5,6])
array_2d=np.array([[1,2,34,5],
                   [34,5,67,89],
                   [77,55,331,1]])
array_3d=np.array([[[1,2,34,5],
                   [34,5,67,89],
                   [77,55,331,1]]])
#print(array_2d.shape) #----------tell us row and clumn in number-------------
#print(array_2d.size) #---------tell us total values in array-------------
#print(array_3d.ndim) #---------------tell us total number of dimension-array type-----------
#print(array_1d.dtype) #-------data type of elements------------------
#print(array_1d.astype(int)) #-----------convert data type of elements--------------

# --------do fast mathamatical operation wihtout using loops----------
# print(array_1d+4)
# print(array_1d*4)
# print(array_1d**4)
# aggregate function 
# print(np.sum(array_1d))
# print(np.mean(array_1d))
# print(np.min(array_1d))
#print(np.std(array_1d)) # -----------standard deviation=probalility of data from percentage---------------
#print(np.var(array_1d))# ------calculate variants-------------
