# creation array from python list
import numpy as np

arr=np.array([1,2,3,4])
# print(arr)
# with default values ,use for future values
zeroes_array=np.zeros(3) #filled with zero 
# print(zeroes_array)
ones_array=np.ones((2,3)) #filled with 1 
# print(ones_array)
filled_array=np.full((2,3),7) #full shaped values
# print(filled_array)
# creating sequences of number in numpy 
arrange=np.arange(1,10,3) #parameter(start,stop,step)
# print(arrange)
# creating identity metrics, is a square matrics with 1 diagonal and zero else where
identity=np.eye(4)
print(identity)


