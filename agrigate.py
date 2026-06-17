import numpy as np

array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(np.sum(array))
# print(np.mean(array))
# print(np.std(array))  # Standard deveation
# print(np.var(array))  # Variance
# print(np.min(array))  # for minimum value
# print(np.max(array))  # for max value
# print(np.argmin(array))  # index of min value
# print(np.argmax(array))  # index of max value

print(np.sum(array, axis=0))  # sum of column
print(np.sum(array, axis=1))  # sum of row
