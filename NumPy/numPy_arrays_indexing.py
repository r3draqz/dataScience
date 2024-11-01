import numpy as np

# arr = np.arange(0,11)
# print(arr)

##### INDEXING BASICS ####
# print(arr[2:5]) ## index 2 to 5 (exclusive 5)
# print(arr[:6]) ## everything before index 6
# print(arr[2:]) ## everything after index 2 (inclusive)

##### SLICING #####
# slice_arr = arr[:6]
# slice_arr[:] = 99
# print(arr) ## changed the original array because numpy keeps the original memory

# arr_copy = arr.copy()
# arr_copy[:] = 100
# print(arr_copy) ## doesn't affect the original because.copy
# print(arr_copy)

##### INDEXING IN MATRIX #####
# arr_2d = np.array([[5,10,15], [20,25,30], [35,40,45]])
# print(arr_2d)
# print(arr_2d[0]) ## entire first row
# print(arr_2d[1][1]) ## row and column
# print(arr_2d[2,1]) ## single bracket notation row, column
# print(arr_2d[:2,1:]) ## up to row 2 (exclusive), from column 1 onwards (inclusive)

# bool_arr = arr>5 # tells where in the array is it greater than 5
# print(arr[bool_arr == False]) # where it's false
# arr_2d = np.arange(50).reshape(5,10)
# print(arr_2d[1:3,3:5])