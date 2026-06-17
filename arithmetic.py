import numpy as pi

array = pi.array([1.01, 2.5, 3.99])

# Scalar arithmetic

# print(array + 1)
# print(array - 2)
# print(array * 3)
# print(array / 4)
# print(array**5)

# Vevtorized math funcs

# print(pi.sqrt(array))  # squareroot
# print(pi.round(array))  # round
# print(pi.floor(array))  # round down
# print(pi.ceil(array))  # round up

# Excersie calculate area of circle of radius 1,2,3]
radii = pi.array([1, 2, 3])
print(pi.pi * radii**2)

# Element-wise arithmetic

# array1 = pi.array([1, 2, 3])
# array2 = pi.array([4, 5, 6])
# print(array1 + array2)
# print(array1 - array2)
# print(array1 * array2)
# print(array1 / array2)
# print(array1**array2)

# Comparison operators

scores = pi.array([91, 55, 69, 67, 100, 76, 90])
# print(scores == 100)
# print(scores <= 60)
# print(scores >= 60)

scores[scores < 60] = 0
print(scores)
