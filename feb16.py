# Todays topics Slicing an  array
import numpy as np

arr1 = np.array([1,2,3,4,5,6,7])
print("SLiced : ",arr1[1:4]) # first will include and second wont

arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print(arr2[1,1:4])