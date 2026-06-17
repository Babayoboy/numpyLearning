import numpy as pi

# # array1 = pi.array([[1, 2, 3, 4], [5, 6, 7, 8]]) #this will not work as (2, 4) the dimentions must be same or have one in them
# array1 = pi.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
# array2 = pi.array([[1], [2], [3], [4]])

# print(array1.shape)
# print(array2.shape)

# print(array1 * array2)

array1 = pi.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
array2 = pi.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

print(array1.shape)
print(array2.shape)
print(array1 * array2)
