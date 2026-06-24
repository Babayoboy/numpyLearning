# NumPy Practice & Learning

Welcome to my **NumPy** learning repository! This project contains a collection of Python scripts demonstrating various numerical computing, array manipulation, and statistical techniques using the [NumPy](https://numpy.org/) library.

Each script is a self-contained example focusing on a specific aspect of NumPy—ranging from basic array initialization to slicing, broadcasting, filtering, and random number generation.

---

## Table of Contents

- [Features Covered](#features-covered)
- [Repository Structure](#repository-structure)
- [Installation & Setup](#installation--setup)
- [Scripts Overview](#scripts-overview)
  - [1. Basics & Arithmetic](#1-basics--arithmetic)
  - [2. Array Manipulation](#2-array-manipulation)
  - [3. Data Analysis & Filtering](#3-data-analysis--filtering)
  - [4. Randomness & Simulations](#4-randomness--simulations)

---

## Features Covered

Below is a summary of the NumPy components and configurations practiced in this repository:

| Feature | Description | File Demonstration |
| :--- | :--- | :--- |
| **Array Creation** | Converting Python structures and comparing array vs. list behaviors | [array.py](./array.py) |
| **Scalar & Vector Math** | Basic calculations, trigonometric and rounding operations, and geometric formulas | [arithmetic.py](./arithmetic.py) |
| **Multi-Dimensional Arrays** | Indexing and dimensional analysis of 3D grids | [multi_D_array.py](./multi_D_array.py) |
| **Array Slicing** | Row and column extraction, stepping, and reversing | [slicing.py](./slicing.py) |
| **Broadcasting** | Operating on arrays with mismatching shapes | [broadcasting.py](./broadcasting.py) |
| **Aggregations** | Sum, mean, standard deviation, variance, and extrema indices across axes | [agrigate.py](./agrigate.py) |
| **Boolean Filtering** | Applying conditional masks and using `np.where` for data replacement | [filtering.py](./filtering.py) |
| **Random Generator** | Sampling integers, uniform distributions, shuffling, and choosing items | [randomNumber.py](./randomNumber.py), [exersise.py](./exersise.py) |
| **System Info** | Auditing the environment configuration | [version.py](./version.py) |

---

## Repository Structure

```text
├── array.py              # Comparing lists and array scalar multiplication
├── arithmetic.py         # Vectorized operations, rounding functions, and masks
├── version.py            # Checks the installed NumPy version
├── multi_D_array.py      # 3D coordinates indexing (ANSH extraction demo)
├── slicing.py            # Sub-grid, row, column slices, and index reversing
├── broadcasting.py       # Performing mathematical operations on mismatched dimensions
├── agrigate.py           # Statistical reductions (sum, mean, var, std) across axes
├── filtering.py          # Conditional subsetting using boolean masks and np.where
├── randomNumber.py       # Integer/float generators, shuffling, and choice selection
└── exersise.py           # Emoji grid generator simulation using default_rng
```

---

## Installation & Setup

To run these NumPy scripts locally, make sure you have Python installed, then install the required dependency:

```bash
pip install numpy
```

To run any script (for example, `broadcasting.py`):

```bash
python broadcasting.py
```

---

## Scripts Overview

### 1. Basics & Arithmetic

*   **[array.py](./array.py)**
    *   **Concept**: Comparing memory structure/behavior of standard Python lists vs. NumPy arrays.
    *   **Key takeaway**: Multiplying a standard list by a scalar repeats the elements, whereas a NumPy array handles it as an element-wise vector operation:
        ```python
        array = pi.array([1, 2, 3, 4])
        array = array * 2  # Returns [2, 4, 6, 8]
        ```
*   **[arithmetic.py](./arithmetic.py)**
    *   **Concept**: Applying basic arithmetic operators and math functions on arrays.
    *   **Key takeaway**: Using vectorized operations like `pi.sqrt()`, `pi.round()`, `pi.floor()`, `pi.ceil()`, and performing value replacements with condition masks:
        ```python
        scores[scores < 60] = 0  # Replaces all values below 60 with 0
        ```
*   **[version.py](./version.py)**
    *   **Concept**: Printing metadata details of the library.
    *   **Key takeaway**: Verification of the installed library version using `pi.__version__`.

### 2. Array Manipulation

*   **[multi_D_array.py](./multi_D_array.py)**
    *   **Concept**: Defining and navigating 3D arrays.
    *   **Key takeaway**: Illustrates the difference between chain indexing (`array[0][0][0]`) and cleaner multi-dimensional tuple indexing (`array[2, 2, 2]`). Uses index mapping to assemble characters from a grid (printing `"ANSH"`).
*   **[slicing.py](./slicing.py)**
    *   **Concept**: Slicing 2D arrays with stride intervals.
    *   **Key takeaway**: Extracting whole rows (`array[1]`), reversing rows (`array[::-1]`), extracting specific columns (`array[:, 0]`), and isolating nested sub-grids (`array[0:2, 2:]`).
*   **[broadcasting.py](./broadcasting.py)**
    *   **Concept**: Arithmetic operations across arrays of mismatched shapes.
    *   **Key takeaway**: Under broadcasting rules, dimensions of size 1 are stretched to match the other array's shape to execute element-wise operations:
        ```python
        # Stretches a (1, 10) row vector against a (10, 1) column vector to produce a (10, 10) matrix
        array1 = pi.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
        array2 = pi.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
        print(array1 * array2)
        ```

### 3. Data Analysis & Filtering

*   **[agrigate.py](./agrigate.py)**
    *   **Concept**: Extracting statistical metrics from data arrays.
    *   **Key takeaway**: Offers key reductions like `np.sum()`, `np.mean()`, `np.std()`, `np.var()`, and position tracking with `np.argmin()` / `np.argmax()`. Operations can be isolated to columns (`axis=0`) or rows (`axis=1`).
*   **[filtering.py](./filtering.py)**
    *   **Concept**: Extracting array subsets satisfying conditional predicates.
    *   **Key takeaway**: Implements boolean indexing with logical operators (e.g. `&` and `|`), and shows `np.where(condition, x, y)` as a conditional selector.

### 4. Randomness & Simulations

*   **[randomNumber.py](./randomNumber.py)**
    *   **Concept**: Generating pseudo-random arrays using modern generator protocols.
    *   **Key takeaway**: Utilizing `np.random.default_rng()` for random number operations. Illustrates producing integer and float uniform distributions, in-place shuffling, and randomly selecting items from list datasets (e.g. fruit emojis).
*   **[exersise.py](./exersise.py)**
    *   **Concept**: Simulating randomized selection grids.
    *   **Key takeaway**: Applying generator choice APIs (`rdm.choice()`) to sample emojis and build custom 2D status grids (`size=(3, 3)`).
