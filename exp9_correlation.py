# ============================================================
# EXPERIMENT 9: Correlation & Multi-Variable Analysis
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 50)
print("EXPERIMENT 9: Correlation & Multi-Variable Analysis")
print("=" * 50)

# ---------- Dataset ----------
np.random.seed(42)
n = 50
df = pd.DataFrame({
    'Age':         np.random.randint(22, 55, n),
    'Experience':  np.random.randint(1, 30, n),
    'Salary':      np.random.randint(30000, 100000, n),
    'Score':       np.random.randint(60, 100, n),
    'Hours_Work':  np.random.randint(30, 60, n)
})

print("\nDataset Head:\n", df.head())

# ---------- Correlation Matrix ----------
print("\n--- Correlation Matrix ---")
corr = df.corr()
print(corr.round(2))

# ---------- Heatmap ----------
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm',
            linewidths=0.5, square=True)
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig('exp9_heatmap.png')
plt.show()

# ---------- Scatter Plot Matrix (Pair Plot) ----------
sns.pairplot(df, diag_kind='kde', plot_kws={'alpha': 0.5})
plt.suptitle('Pair Plot - Multi-Variable Relationships', y=1.02)
plt.tight_layout()
plt.savefig('exp9_pairplot.png')
plt.show()

# ---------- Individual Scatter Plots ----------
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].scatter(df['Age'], df['Salary'], alpha=0.6, color='blue')
axes[0].set_title('Age vs Salary')
axes[0].set_xlabel('Age')
axes[0].set_ylabel('Salary')

axes[1].scatter(df['Experience'], df['Salary'], alpha=0.6, color='green')
axes[1].set_title('Experience vs Salary')
axes[1].set_xlabel('Experience')
axes[1].set_ylabel('Salary')

axes[2].scatter(df['Hours_Work'], df['Score'], alpha=0.6, color='red')
axes[2].set_title('Hours Worked vs Score')
axes[2].set_xlabel('Hours Work')
axes[2].set_ylabel('Score')

plt.tight_layout()
plt.savefig('exp9_scatter_plots.png')
plt.show()

# ---------- Grouped Bar Chart ----------
dept = pd.DataFrame({
    'Dept':   ['HR', 'IT', 'Finance', 'HR', 'IT', 'Finance'],
    'Salary': [45000, 70000, 60000, 40000, 75000, 55000],
    'Score':  [80, 90, 85, 75, 88, 82]
})
dept_avg = dept.groupby('Dept').mean()
dept_avg.plot(kind='bar', figsize=(7, 5), colormap='Set2', edgecolor='black')
plt.title('Average Salary & Score by Department')
plt.xlabel('Department')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('exp9_grouped_bar.png')
plt.show()

print("\nAll plots saved. Experiment 9 Complete!")
