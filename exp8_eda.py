# ============================================================
# EXPERIMENT 8: Exploratory Data Analysis (EDA) in Python
# (Equivalent of R: na, summary, plot, hist, boxplot)
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 50)
print("EXPERIMENT 8: Exploratory Data Analysis (EDA)")
print("=" * 50)

# ---------- Load / Create Dataset ----------
np.random.seed(42)
data = {
    'Age':    [23, 25, np.nan, 30, 32, 35, 28, np.nan, 40, 22, 27, 33],
    'Salary': [30000, 35000, 40000, np.nan, 50000, 60000,
               45000, 55000, 70000, 28000, 38000, 52000],
    'Score':  [88, 76, 92, 85, np.nan, 78, 90, 82, 95, 70, 88, 79],
    'Dept':   ['HR', 'IT', 'HR', 'IT', 'Finance', 'Finance',
               'IT', 'HR', 'Finance', 'IT', 'HR', 'Finance']
}
df = pd.DataFrame(data)

print("\n--- Raw Dataset ---")
print(df)

# ---------- Checking Missing Values (like R's is.na()) ----------
print("\n--- Missing Values ---")
print(df.isnull().sum())

# ---------- Fill Missing Values ----------
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].median(), inplace=True)
df['Score'].fillna(df['Score'].mean(), inplace=True)
print("\nAfter Handling NA:\n", df)

# ---------- Summary Statistics (like R's summary()) ----------
print("\n--- Summary Statistics ---")
print(df.describe())
print("\nData Types:\n", df.dtypes)

# ---------- Histogram (like R's hist()) ----------
plt.figure(figsize=(14, 4))

plt.subplot(1, 3, 1)
plt.hist(df['Age'], bins=6, color='skyblue', edgecolor='black')
plt.title('Histogram: Age')
plt.xlabel('Age')
plt.ylabel('Frequency')

plt.subplot(1, 3, 2)
plt.hist(df['Salary'], bins=6, color='salmon', edgecolor='black')
plt.title('Histogram: Salary')
plt.xlabel('Salary')

plt.subplot(1, 3, 3)
plt.hist(df['Score'], bins=6, color='lightgreen', edgecolor='black')
plt.title('Histogram: Score')
plt.xlabel('Score')

plt.tight_layout()
plt.savefig('exp8_histograms.png')
plt.show()

# ---------- Boxplot (like R's boxplot()) ----------
plt.figure(figsize=(12, 5))

plt.subplot(1, 3, 1)
plt.boxplot(df['Age'])
plt.title('Boxplot: Age')

plt.subplot(1, 3, 2)
plt.boxplot(df['Salary'])
plt.title('Boxplot: Salary')

plt.subplot(1, 3, 3)
plt.boxplot(df['Score'])
plt.title('Boxplot: Score')

plt.tight_layout()
plt.savefig('exp8_boxplots.png')
plt.show()

# ---------- Line Plot (like R's plot()) ----------
plt.figure(figsize=(7, 4))
plt.plot(df['Age'], df['Salary'], marker='o', color='purple')
plt.title('Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.tight_layout()
plt.savefig('exp8_plot.png')
plt.show()

# ---------- Count by Department ----------
print("\n--- Value Counts: Dept ---")
print(df['Dept'].value_counts())

print("\nAll plots saved. Experiment 8 Complete!")
