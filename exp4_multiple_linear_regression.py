# ============================================================
# EXPERIMENT 4: Multiple Linear Regression in Python
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

print("=" * 50)
print("EXPERIMENT 4: Multiple Linear Regression")
print("=" * 50)

# ---------- Dataset ----------
data = {
    'Experience': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Age':        [22, 25, 28, 30, 32, 35, 38, 40, 42, 45],
    'Salary':     [30000, 35000, 40000, 45000, 50000,
                   60000, 65000, 70000, 75000, 80000]
}
df = pd.DataFrame(data)
print("\nDataset:\n", df)

# ---------- Features & Target ----------
X = df[['Experience', 'Age']]
y = df['Salary']

# ---------- Train/Test Split ----------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---------- Model Training ----------
model = LinearRegression()
model.fit(X_train, y_train)

print(f"\nCoefficients:")
for feat, coef in zip(X.columns, model.coef_):
    print(f"  {feat}: {coef:.4f}")
print(f"Intercept: {model.intercept_:.4f}")

# ---------- Prediction ----------
y_pred = model.predict(X_test)
print(f"\nActual:    {list(y_test)}")
print(f"Predicted: {[round(p,1) for p in y_pred]}")

# ---------- Metrics ----------
mse = mean_squared_error(y_test, y_pred)
r2  = r2_score(y_test, y_pred)
print(f"\nMSE : {mse:.2f}")
print(f"RMSE: {np.sqrt(mse):.2f}")
print(f"R²  : {r2:.4f}")

# ---------- Plot ----------
plt.figure(figsize=(7, 5))
plt.scatter(range(len(y_test)), y_test, color='blue', label='Actual')
plt.scatter(range(len(y_pred)), y_pred, color='red', label='Predicted')
plt.title('Multiple Linear Regression - Actual vs Predicted')
plt.xlabel('Sample Index')
plt.ylabel('Salary')
plt.legend()
plt.tight_layout()
plt.savefig('exp4_multiple_lr.png')
plt.show()
print("\nPlot saved as exp4_multiple_lr.png")
print("Experiment 4 Complete!")
