# ============================================================
# EXPERIMENT 10: Data Analysis with Pandas & NumPy
# ============================================================

import numpy as np
import pandas as pd

print("=" * 50)
print("EXPERIMENT 10: Pandas & NumPy Data Analysis")
print("=" * 50)

# ===========================================================
# PART A — NumPy
# ===========================================================
print("\n" + "=" * 30)
print("PART A: NumPy")
print("=" * 30)

arr1D = np.array([10, 20, 30, 40, 50])
arr2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("\n1D Array:", arr1D)
print("2D Array:\n", arr2D)

# Basic ops
print("\nMean:", np.mean(arr1D))
print("Median:", np.median(arr1D))
print("Std Dev:", np.std(arr1D))
print("Sum:", np.sum(arr1D))
print("Min/Max:", np.min(arr1D), "/", np.max(arr1D))

# Array operations
print("\nElement-wise *2:", arr1D * 2)
print("Square root:", np.sqrt(arr1D))
print("Array reshape (1D→2D):\n", arr1D.reshape(5, 1))

# Matrix operations
print("\nMatrix Transpose:\n", arr2D.T)
print("Matrix Dot Product:\n", np.dot(arr2D, arr2D.T))

# Random numbers
rand_arr = np.random.randint(1, 100, size=(3, 4))
print("\nRandom 3x4 Array:\n", rand_arr)

# Indexing and slicing
print("\nSlice arr2D [0:2, 1:3]:\n", arr2D[0:2, 1:3])
print("Conditional Filter (arr1D > 25):", arr1D[arr1D > 25])

# ===========================================================
# PART B — Pandas
# ===========================================================
print("\n" + "=" * 30)
print("PART B: Pandas")
print("=" * 30)

data = {
    'Name':       ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age':        [25, 30, 35, 28, 22],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Salary':     [50000, 70000, 80000, 65000, 45000],
    'Score':      [88, 92, 78, 95, 82]
}
df = pd.DataFrame(data)

print("\nDataFrame:\n", df)
print("\nShape:", df.shape)
print("Columns:", list(df.columns))
print("Data Types:\n", df.dtypes)

# Descriptive Statistics
print("\n--- Descriptive Statistics ---")
print(df.describe())

# Selecting
print("\n--- Column Selection ---")
print(df[['Name', 'Salary']])

# Filtering
print("\n--- Filter: Salary > 60000 ---")
print(df[df['Salary'] > 60000])

# Sorting
print("\n--- Sorted by Salary (desc) ---")
print(df.sort_values('Salary', ascending=False))

# GroupBy
print("\n--- GroupBy Department: Mean Salary ---")
print(df.groupby('Department')['Salary'].mean())

# Adding a column
df['Bonus'] = df['Salary'] * 0.10
print("\n--- After Adding Bonus Column ---")
print(df)

# Missing Values Simulation
df.loc[2, 'Score'] = np.nan
print("\n--- Missing Values ---")
print(df.isnull().sum())
df['Score'].fillna(df['Score'].mean(), inplace=True)
print("After filling NaN:\n", df['Score'])

# Merging
extra = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Rating': ['A', 'A', 'B', 'A', 'B']
})
merged = pd.merge(df, extra, on='Name')
print("\n--- Merged DataFrame ---")
print(merged)

print("\nExperiment 10 Complete!")
