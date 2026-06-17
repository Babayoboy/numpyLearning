This repository contains a collection of Python scripts demonstrating various features and functionalities of the NumPy library. It serves as a personal learning log for mastering array manipulation and numerical computing.

## Topics Covered

### 1. Basics & Arithmetic
- **[array.py](./array.py)**: Introduction to NumPy arrays and comparison with Python lists.
- **[arithmetic.py](./arithmetic.py)**: Scalar arithmetic, vectorized operations, math functions (`sqrt`, `round`, `floor`, `ceil`), and comparison operators.
- **[version.py](./version.py)**: Checking the installed NumPy version.

### 2. Array Manipulation
- **[multi_D_array.py](./multi_D_array.py)**: Working with multi-dimensional (3D) arrays, including chain and multi-dimensional indexing.
- **[slicing.py](./slicing.py)**: Advanced slicing techniques for rows and columns, including steps and reversing arrays.
- **[broadcasting.py](./broadcasting.py)**: Understanding how NumPy handles operations between arrays of different shapes.

### 3. Data Analysis & Filtering
- **[agrigate.py](./agrigate.py)**: Statistical functions such as `sum`, `mean`, `std`, `var`, `min`, `max`, and index-finding functions like `argmin`/`argmax`. Demonstrates operations along specific axes.
- **[filtering.py](./filtering.py)**: Conditional filtering using boolean indexing and the `np.where` function.

### 4. Randomness & Simulations
- **[randomNumber.py](./randomNumber.py)**: Using `numpy.random.default_rng` to generate integers, uniform floats, shuffling arrays, and making random choices.
- **[exersise.py](./exersise.py)**: A practical exercise using random choice to generate a grid of emojis.

## How to Use
Ensure you have NumPy installed:
```bash
pip install numpy
```

Run any script using Python:
```bash
python <filename>.py
```
