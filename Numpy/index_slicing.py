# access specific elment and change it 
"""
array[index] #1d array
array[row,column] #2d array
slicing
array[start:stop:step] #step means to skip some index
"""
import numpy as np
array_1d=np.array([1,2,34,5,6])
# print(array_1d[2])
# fancy indexing 
# print(array_1d[[1,3,4]])
# =============filter array boolean masking=============
print(array_1d>25) # ======return true & false========
# slicing 
#print(array_1d[0:4]) #============index 0 to 4==========
#print(array_1d[:4]) #========index 0 to 4===========
#print(array_1d[::2])  #=========every second element==========
#print(array_1d[::-1]) #=============reverse array==============


