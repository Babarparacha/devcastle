"""
Numpy used for faster computational results,work in deep level and get fastest result.
"""
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8])
array_2d=np.array([[1,2,3,4,5],[6,7,8,9,10]])
array_3d=np.array(([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]))
# print(arr)
# print(np.zeros((2,3),dtype=int)) # fill single array with 0 values
# print(np.arange(0,5,2))   #(start,end,steps) generate 0 to 4 single array
# print(np.random.randint(0,6,size=(2,3)))  # choose random number between 0 to 6
# copy function 
# print(np.random.rand(4,6))  # create random array 2 rows 6 column
# copied=arr.copy()
# copied[0]=99
# print(copied)
# print(np.insert(array_2d,2,10,1)) # it add 10 in both rows np.insert(array,index,value,asix=None->0=row-wise,1=column-wise)
# print(np.append(array_2d,[7,8,9,10,11])) # insert data at end
# print(np.sort(arr))
#print(np.delete(array_1d,1))#arr(arr,index,axis)
#print(np.delete(array_2d,1,1))#its delete entire row
# print(array_2d.shape) #tell us row and clumn in number
# print(array_2d.reshape(2,5)) #change structure without changing data
# print(array_2d.max())
# print(arr.min())
# print(array_2d.argmax()) #to find index position of extreme values
# print(array_2d.argmin()) #to find index postion of lowest values
# print(np.concatenate((array_3d,array_2d))) #merge two array but dimension should be same
# removing data from array 
flat_arr=np.array_split(arr,2)
print(flat_arr)
for part in flat_arr:
    print(part)
print(np.append(flat_arr,array_2d)) #merge two array but dimension should be same
# print(np.ones((2,3)))  # create 2d_array with 1 values all, 2 row 3 column
# print(np.full((2,3),7)) #create 2d_array with 7 values all, 2 row 3 column
# print(array_2d.ndim) #check dimension of array
# print(array_2d.dtype) # to check data type of an element
# print(array_2d.size) #tell us total values in array