import numpy as np

##### INTRO TO NP #####
# my_list = [1,2,3]
# arr = np.array(my_list)
# print(arr)

# my_mat = [[1,2,3],[4,5,6],[7,8,9]]
# matarr = np.array(my_mat)
# print(matarr)
# print(my_mat)

##### CREATING AN ARRAY #####
# print(np.arange(0,10,2))
# print(np.zeros(3)) ## three rows of 0 (kinda like initialize the array)
# print(np.zeros((2,5))) ## two rows, 5 columns
# print(np.ones((10,5))) ## same as zeros, just with ones
# print(np.linspace(0, 5, 10)) ## 10 evenly spaced numbers going up to 5

##### CREATING AN IDENTITY MATRIX ##### - square matrix with a diagnol of 1s
# print(np.eye(5))

##### RANDOM NUMBERS #####
# print(np.random.rand(5)) ## random numbers between zero and one, with the number passed being the number of indices
# print(np.random.rand(5,5)) ## rows and columns of random numbers between zero and one
# print(np.random.randn(2, 3)) ## 2 rows, 3 columns of numbers that are from a standard normal distribution
# print(np.random.randint(1,100,3)) ## 3 random integers between 1 and 100 (exclusive)

##### USEFUL ATTRIBUTES AND ARRAYS #####
# arr = np.arange(25)
# ranarr = np.random.randint(0,50,10)
# print(ranarr)
# arr.reshape(5,5) ## changes to a matrix
# print(arr)

# print(ranarr.max())
# print(ranarr.argmax()) # index of max value
# print(arr.shape) ## number of rows and columns

# arr = arr.reshape(5,5)
# print(arr)
# print(arr.shape)

# print(arr.dtype) ## data type in the array