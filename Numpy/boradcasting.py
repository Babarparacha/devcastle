""" Broadcasting in NumPy is a powerful mechanism that allows arithmetic operations on arrays of different shapes and sizes without explicitly creating multiple copies of the smaller array.
3 rules->
1-matches dimension [1,2,3]+[4,5,6]
2-expanding single element [1,2,3]+[10]
3-incompatible shapes[1,2,3]+[1,2] """

#----------------old way to do calculation-----------------
# prices=[100,200,300]
# disocunt=10 #10%
# final_prices=[]
# for price in prices:
#     final_price=price-(price*disocunt/100)
#     final_prices.append(final_price)
# print((final_prices))

# -----------now do it using numpy --------------
import numpy as np

# prices=np.array([100,200,300])
# disocunt=10 #10%
# final_price=prices-(prices*disocunt/100)
# print(final_price)

#----------- broadcating single value--------------
# arr=np.array([200,300,400])
# print(arr*2)
# broadcating 2d_array value
matrix=np.array([[1,2,3],[4,5,6]])
vector=np.array([1,2,3])
res=matrix+vector #------------matches dimension example
# print(res)
#---------------incompatible shapes----------------
arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([1,2])
res=arr1+arr2
print(res)

