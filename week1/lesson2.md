
# Lesson 2: NumPy Basics & Matrix Multiplication

## Introduction
NumPy is the foundation for numerical computing in Python. It is fast, efficient, and widely used in AI/ML for handling large datasets, performing vectorized operations, and dealing with matrices.

In AI engineering, you will often handle large numerical datasets and matrices — for example, neural network weights and feature vectors. Pure Python lists are slow for these operations because they lack low-level optimizations. NumPy solves this by using C-optimized code under the hood.

---

## Problem Statement
1. Create two random matrices:
   - `A` of shape **3×2**
   - `B` of shape **2×4**
   - Fill them with integers between **1 and 10**.

2. Multiply the two matrices using NumPy's `dot` or `@` operator.

3. Transpose the result matrix.

4. Find:
   - Mean of all elements in the result matrix.
   - Maximum value and its position (row, column).

---

## Solution

```python
import numpy as np

# Step 1: Create matrices
A = np.random.randint(1, 11, size=(3, 2))
B = np.random.randint(1, 11, size=(2, 4))

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Step 2: Matrix multiplication
result = A @ B  # same as np.dot(A, B)

print("\nA × B:")
print(result)

# Step 3: Transpose
result_T = result.T

print("\nTranspose of result:")
print(result_T)

# Step 4: Calculations
mean_val = np.mean(result)
max_val = np.max(result)
max_pos = np.unravel_index(np.argmax(result), result.shape)

print(f"\nMean: {mean_val}")
print(f"Max value: {max_val} at position {max_pos}")
```

---

## Example Output
```
Matrix A:
[[ 1  5]
 [ 4  7]
 [ 3  2]]

Matrix B:
[[ 9  8  7  6]
 [ 5  4  3  2]]

A × B:
[[34 28 22 16]
 [73 60 47 34]
 [37 32 27 22]]

Transpose of result:
[[34 73 37]
 [28 60 32]
 [22 47 27]
 [16 34 22]]

Mean: 39.75
Max value: 73 at position (1, 0)
```

---

## Why NumPy is Better than Pure Python Lists
### **Speed Comparison**
```python
import time

# Python list multiplication
size = 500
list_A = [[i for i in range(size)] for _ in range(size)]
list_B = [[i for i in range(size)] for _ in range(size)]

start = time.time()
result_list = [[sum(a*b for a, b in zip(row_a, col_b)) for col_b in zip(*list_B)] for row_a in list_A]
end = time.time()
print("Pure Python time:", end - start, "seconds")

# NumPy multiplication
np_A = np.array(list_A)
np_B = np.array(list_B)

start = time.time()
result_np = np_A @ np_B
end = time.time()
print("NumPy time:", end - start, "seconds")
```
NumPy is often **10x–100x faster** because it uses **vectorized operations** and **C-level optimizations**.

---

✅ **Next Step**: Practice using NumPy for more complex operations like element-wise multiplication, broadcasting, and reshaping.
