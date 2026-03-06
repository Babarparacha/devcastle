
"""
np.insert(array,index,value,asix=None->0=row-wise,1=column-wise)-add at specific position
np.concatenate(arr1,arr2,asix=None->0=row-wise,1=column-wise)
stacking-combine multiple arrays=> veritically,horizontly
v-stack-row-wise,
hstack-column wise
spliting- it split array in equal,vsplit,hsplit"""
import numpy as np
array_1d=np.array([1,2,3,4,5,6])
# print(np.insert(array_1d,5,7,1))
array_2d=np.array([[1,2,3],[4,5,6]])
#print(np.insert(array_2d,2,10,1)) # it add 10 in both rows
#print(np.insert(array_2d,2,10,0)) # it add 10 and create a new column
#print(np.insert(array_2d,2,10,None)) # flatten the array

#append add data at the end 
# print(np.append(array_2d,[7,8,9,10,11])) # insert data at end
# join two arrays 
# arr_1d=np.array([1,2,3,4])
# arr_2d=np.array([5,6,7,8])
# print(np.concatenate((arr_1d,arr_2d)))

# removing data from array 
#print(np.delete(array_1d,1))#arr(arr,index,axis)
#print(np.delete(array_2d,1,1))#its delete entire row

#stacking-
ar_1d=np.array([1,2,3,4,5,6])
ar_2d=np.array([7,8,9,10,11,12])
print(np.vstack((ar_1d,ar_2d)))
# print(np.hstack((ar_1d,ar_2d)))
# spliting 
# print(np.split(ar_1d,2))