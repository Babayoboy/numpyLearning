import numpy as pi

array = pi.array(
    [
        [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]],
        [["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R"]],
        [["S", "T", "U"], ["V", "W", "X"], ["Y", "Z", "!"]],
    ]
)


# print(array.ndim)
# print(array.shape)
# print(array[0][0][0]) #chain indexing
# print(array[2, 2, 2]) # multi-dimensional indexing

word = array[0, 0, 0] + array[1, 1, 1] + array[2, 0, 0] + array[0, 2, 1]
print(word)
