import numpy as np

# random_no = np.random.default_rng(seed=3)  # seed is use to produce the same result

# print(random_no.integers(low=1, high=7))
# print(random_no.integers(low=1, high=101))
# print(random_no.integers(low=1, high=101, size=3))
# print(random_no.integers(low=1, high=101, size=(3, 2)))

# np.random.seed(seed=2)
# print(np.random.uniform(low=-1, high=1))  # for float
# print(np.random.uniform(low=-1, high=1, size=3))
# print(np.random.uniform(low=-1, high=1, size=(3, 2)))

rng = np.random.default_rng()
# array = np.array([1, 2, 3, 4, 5])
# print(array)
# rng.shuffle(array)
# print(array)

# fruits = np.array(["mango", "lichi", "kafal", "peach", "watermellon"])
fruits = np.array(["🥭", "🍒", "🫐", "🍑", "🍉"])
# print(fruits)
# fruit = rng.choice(fruits, size=3)
fruit = rng.choice(fruits, size=(3, 3))
print(fruit)
