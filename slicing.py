import numpy as pi

array = pi.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

# array[start:end:step]

# print(array[0])  # prints the first row
# print(array[1]) # prints the secound row
# print(array[-2])  # prints the last secound row

# print(array[1:]) # prints all the row from 2nd
# print(array[1:3]) # prints from secound to 3rd

# print(array[0:4:2])  # form 0-3 with skipping 1 row in between
# print(array[::2])  # if want to select full array with skipping 1 row in between

# print(array[::-1])  # Array in reverse
# print(array[::-2])  # Array in reverse with skiping one

# # print(array[,0]) # Will not work have to add [:,0]
# print(array[:, 0])  # this print the first column
# print(array[:, -2])  # this print the secound first column
# print(array[:, 0:3])  # this prints from first to 3rd column
# print(array[:, ::2])  # this prints from first to last with skiping 1 column
