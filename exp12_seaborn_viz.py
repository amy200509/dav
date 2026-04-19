# ============================================================
# EXPERIMENT 12: Visualizations using Seaborn
# (Histogram, Bar Chart, Pie Chart, Box Plot,
#  Violin Plot, Regression Plot) — Any 3
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 50)
print("EXPERIMENT 12: Seaborn Visualizations")
print("=" * 50)

np.random.seed(42)
data = {
    'Age':    np.random.randint(20, 60, 100),
    'Salary': np.random.randint(30000, 100000, 100),
    'Score':  np.random.normal(75, 10, 100),
    'Dept':   np.random.choice(['HR', 'IT', 'Finance', 'Marketing'], 100),
    'Gender': np.random.choice(['Male', 'Female'], 100)
}
df = pd.DataFrame(data)

# Set Seaborn style
sns.set_theme(style='whitegrid', palette='muted')

# ===========================================================
# 1. HISTOGRAM (histplot)
# ===========================================================
plt.figure(figsize=(7, 5))
sns.histplot(df['Score'], bins=15, kde=True, color='steelblue')
plt.title('Seaborn Histogram - Score Distribution', fontsize=14)
plt.xlabel('Score')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('exp12_histogram.png')
plt.show()
print("1. Histogram saved.")

# ===========================================================
# 2. BAR CHART (barplot)
# ===========================================================
dept_salary = df.groupby('Dept')['Salary'].mean().reset_index()

plt.figure(figsize=(7, 5))
sns.barplot(x='Dept', y='Salary', data=dept_salary, palette='Set2')
plt.title('Seaborn Bar Chart - Avg Salary by Dept', fontsize=14)
plt.xlabel('Department')
plt.ylabel('Average Salary')
plt.tight_layout()
plt.savefig('exp12_barchart.png')
plt.show()
print("2. Bar Chart saved.")

# ===========================================================
# 3. PIE CHART (Seaborn doesn't have native pie;
#    using matplotlib inside seaborn style)
# ===========================================================
dept_counts = df['Dept'].value_counts()
plt.figure(figsize=(7, 6))
plt.pie(dept_counts.values, labels=dept_counts.index,
        autopct='%1.1f%%', startangle=90,
        colors=sns.color_palette('pastel'))
plt.title('Pie Chart - Dept Distribution (Seaborn palette)', fontsize=14)
plt.tight_layout()
plt.savefig('exp12_piechart.png')
plt.show()
print("3. Pie Chart saved.")

# ===========================================================
# 4. BOX PLOT (boxplot)
# ===========================================================
plt.figure(figsize=(8, 5))
sns.boxplot(x='Dept', y='Salary', data=df, palette='Set3')
plt.title('Seaborn Box Plot - Salary by Department', fontsize=14)
plt.xlabel('Department')
plt.ylabel('Salary')
plt.tight_layout()
plt.savefig('exp12_boxplot.png')
plt.show()
print("4. Box Plot saved.")

# ===========================================================
# 5. VIOLIN PLOT (violinplot)
# ===========================================================
plt.figure(figsize=(9, 5))
sns.violinplot(x='Dept', y='Score', hue='Gender', data=df,
               palette='coolwarm', split=True, inner='quartile')
plt.title('Seaborn Violin Plot - Score by Dept & Gender', fontsize=14)
plt.xlabel('Department')
plt.ylabel('Score')
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('exp12_violinplot.png')
plt.show()
print("5. Violin Plot saved.")

# ===========================================================
# 6. REGRESSION PLOT (regplot / lmplot)
# ===========================================================
plt.figure(figsize=(7, 5))
sns.regplot(x='Age', y='Salary', data=df,
            scatter_kws={'alpha': 0.5, 'color': 'steelblue'},
            line_kws={'color': 'red', 'linewidth': 2})
plt.title('Seaborn Regression Plot - Age vs Salary', fontsize=14)
plt.xlabel('Age')
plt.ylabel('Salary')
plt.tight_layout()
plt.savefig('exp12_regplot.png')
plt.show()
print("6. Regression Plot saved.")

# ===========================================================
# BONUS: Heatmap (very common in Seaborn)
# ===========================================================
plt.figure(figsize=(6, 5))
corr = df[['Age', 'Salary', 'Score']].corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap='YlGnBu', linewidths=0.5)
plt.title('Seaborn Heatmap - Correlation', fontsize=14)
plt.tight_layout()
plt.savefig('exp12_heatmap.png')
plt.show()
print("Bonus: Heatmap saved.")

print("\nAll Seaborn visualizations complete! (Experiment 12 Complete!)")
