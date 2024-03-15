# Todays topic - creating arrays with numpy

import numpy as np

arr0 = np.array(26)
arr1 = np.array([2,3,5,7,54])
arr2 = np.array([[2,3,5,7,54],[6,5,6,4,6]])
arr3 = np.array([[[2,3,5,7,54],[6,5,6,4,6],[9,8,6,4,6]]])
arr4 = np.array([[[2,3,5,7,54],[6,5,6,4,6]],[[9,8,6,4,6],[2,8,3,7,90]]])

print("Array 0 : ",arr0) 
print()
print("Array 1 : ",arr1) 
print()
print("Array 2 : ",arr2) 
print()
print("Array 3 : ",arr3) 
print()
print("Array 4 : ",arr4) 

# one d -

arrangeArr = np.arange(0,10,2) # will create array
print("Arange Arr : ",arrangeArr)

zeroArr = np.zeros(5)
print("Zeros Arr : ",zeroArr)

arr_ones = np.ones(5)
print("Ones Arr : ",arr_ones)

# 2 d -

zero_2d = np.zeros((2,3))
print(zero_2d)

ones_2d = np.ones((2,3))
print(ones_2d)

# arrangeArr = np.arange(()) # will create array
# print("Arange Arr : ",arrangeArr)

linspace = np.linspace(0,2,5)
print(linspace)

print("ndim arr0 : ",arr0.ndim)
print("ndim arr1 : ",arr1.ndim)
print("ndim arr2 : ",arr2.ndim)

print("shape of arr0 : ",arr0.shape)
print("shape of arr1 : ",arr1.shape)
print("shape of arr2 : ",arr2.shape)




