# ============================================================
# EXPERIMENT 1: Data Analytics Libraries in Python
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression

print("=" * 50)
print("EXPERIMENT 1: Data Analytics Libraries in Python")
print("=" * 50)

# ---------- NumPy ----------
print("\n--- NumPy ---")
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)
print("Mean:", np.mean(arr))
print("Std Dev:", np.std(arr))
print("Max:", np.max(arr))

# ---------- Pandas ----------
print("\n--- Pandas ---")
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'Salary': [50000, 60000, 70000, 55000]
}
df = pd.DataFrame(data)
print(df)
print("\nDescribe:\n", df.describe())

# ---------- Matplotlib ----------
print("\n--- Matplotlib (Plot saved) ---")
plt.figure(figsize=(6, 4))
plt.plot(df['Name'], df['Salary'], marker='o', color='blue')
plt.title('Salary by Name')
plt.xlabel('Name')
plt.ylabel('Salary')
plt.tight_layout()
plt.savefig('exp1_matplotlib.png')
plt.show()
print("Plot saved as exp1_matplotlib.png")

# ---------- Seaborn ----------
print("\n--- Seaborn ---")
sns.barplot(x='Name', y='Salary', data=df)
plt.title('Seaborn Bar Plot')
plt.tight_layout()
plt.savefig('exp1_seaborn.png')
plt.show()
print("Seaborn plot saved as exp1_seaborn.png")

# ---------- SciPy ----------
print("\n--- SciPy ---")
t_stat, p_val = stats.ttest_1samp(df['Salary'], 60000)
print(f"T-statistic: {t_stat:.4f}, P-value: {p_val:.4f}")

# ---------- Scikit-learn ----------
print("\n--- Scikit-learn ---")
X = df[['Age']]
y = df['Salary']
model = LinearRegression()
model.fit(X, y)
print(f"Coefficient: {model.coef_[0]:.2f}")
print(f"Intercept: {model.intercept_:.2f}")

print("\nExperiment 1 Complete!")
