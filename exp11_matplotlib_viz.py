# ============================================================
# EXPERIMENT 11: Visualizations using Matplotlib
# (Histogram, Bar Chart, Pie Chart, Box Plot,
#  Violin Plot, Regression Plot) — Any 3
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

print("=" * 50)
print("EXPERIMENT 11: Matplotlib Visualizations")
print("=" * 50)

np.random.seed(42)
data = {
    'Age':    np.random.randint(20, 60, 100),
    'Salary': np.random.randint(30000, 100000, 100),
    'Score':  np.random.normal(75, 10, 100),
    'Dept':   np.random.choice(['HR', 'IT', 'Finance', 'Marketing'], 100)
}
df = pd.DataFrame(data)

# ===========================================================
# 1. HISTOGRAM
# ===========================================================
plt.figure(figsize=(7, 5))
plt.hist(df['Score'], bins=15, color='steelblue', edgecolor='black', alpha=0.8)
plt.title('Histogram - Score Distribution', fontsize=14)
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('exp11_histogram.png')
plt.show()
print("1. Histogram saved.")

# ===========================================================
# 2. BAR CHART
# ===========================================================
dept_salary = df.groupby('Dept')['Salary'].mean()

plt.figure(figsize=(7, 5))
bars = plt.bar(dept_salary.index, dept_salary.values,
               color=['#2196F3', '#4CAF50', '#FF5722', '#9C27B0'],
               edgecolor='black')
for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2,
             bar.get_height() + 500,
             f'{bar.get_height():,.0f}',
             ha='center', va='bottom', fontsize=9)
plt.title('Bar Chart - Average Salary by Department', fontsize=14)
plt.xlabel('Department')
plt.ylabel('Average Salary')
plt.tight_layout()
plt.savefig('exp11_barchart.png')
plt.show()
print("2. Bar Chart saved.")

# ===========================================================
# 3. PIE CHART
# ===========================================================
dept_counts = df['Dept'].value_counts()
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
explode = [0.05] * len(dept_counts)

plt.figure(figsize=(7, 6))
plt.pie(dept_counts.values, labels=dept_counts.index, autopct='%1.1f%%',
        colors=colors, explode=explode, startangle=90,
        wedgeprops={'edgecolor': 'white', 'linewidth': 1.5})
plt.title('Pie Chart - Department Distribution', fontsize=14)
plt.tight_layout()
plt.savefig('exp11_piechart.png')
plt.show()
print("3. Pie Chart saved.")

# ===========================================================
# 4. BOX PLOT
# ===========================================================
dept_groups = [df[df['Dept'] == d]['Salary'].values for d in df['Dept'].unique()]
dept_labels = df['Dept'].unique()

plt.figure(figsize=(7, 5))
bp = plt.boxplot(dept_groups, labels=dept_labels, patch_artist=True,
                 medianprops=dict(color='red', linewidth=2))
colors = ['#AED6F1', '#A9DFBF', '#FAD7A0', '#D7BDE2']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
plt.title('Box Plot - Salary by Department', fontsize=14)
plt.xlabel('Department')
plt.ylabel('Salary')
plt.tight_layout()
plt.savefig('exp11_boxplot.png')
plt.show()
print("4. Box Plot saved.")

# ===========================================================
# 5. VIOLIN PLOT (manual using matplotlib)
# ===========================================================
import seaborn as sns  # using seaborn for violin, part of matplotlib ecosystem
plt.figure(figsize=(8, 5))
sns.violinplot(x='Dept', y='Salary', data=df, palette='muted', inner='quartile')
plt.title('Violin Plot - Salary Distribution by Dept', fontsize=14)
plt.xlabel('Department')
plt.ylabel('Salary')
plt.tight_layout()
plt.savefig('exp11_violinplot.png')
plt.show()
print("5. Violin Plot saved.")

# ===========================================================
# 6. REGRESSION PLOT
# ===========================================================
slope, intercept, r_value, p_value, std_err = stats.linregress(df['Age'], df['Salary'])
x_line = np.linspace(df['Age'].min(), df['Age'].max(), 100)
y_line = slope * x_line + intercept

plt.figure(figsize=(7, 5))
plt.scatter(df['Age'], df['Salary'], alpha=0.5, color='steelblue', label='Data Points')
plt.plot(x_line, y_line, color='red', linewidth=2, label=f'Regression Line (R²={r_value**2:.2f})')
plt.title('Regression Plot - Age vs Salary', fontsize=14)
plt.xlabel('Age')
plt.ylabel('Salary')
plt.legend()
plt.tight_layout()
plt.savefig('exp11_regression.png')
plt.show()
print("6. Regression Plot saved.")

print("\nAll 6 Matplotlib visualizations complete! (Experiment 11 Complete!)")
