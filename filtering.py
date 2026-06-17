import numpy as np

ages = np.array(
    [
        [21, 17, 18, 30, 19, 55, 3, 8, 10],
        [44, 76, 53, 49, 9, 15, 20, 25, 13],
    ]
)

# teenageer = ages[ages < 18]
# adults = ages[(ages >= 18) & (ages < 65)]
# seniors = ages[ages >= 65]
# print(teenageer)
# print(adults)
# print(seniors)

# even = ages[ages % 2 == 0]
# odd = ages[ages % 2 != 0]
# print(even)
# print(odd)

# or using where it is slower

adults = np.where((ages >= 18), ages, -1)
print(adults)
