# ============================================================
# EXPERIMENT 3: Simple Linear Regression in Python
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

print("=" * 50)
print("EXPERIMENT 3: Simple Linear Regression")
print("=" * 50)

# ---------- Dataset ----------
np.random.seed(42)
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([2.1, 4.0, 5.9, 8.2, 9.8, 12.1, 13.9, 16.0, 18.1, 20.3])

print("\nInput X:", X.flatten())
print("Output y:", y)

# ---------- Train/Test Split ----------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---------- Model Training ----------
model = LinearRegression()
model.fit(X_train, y_train)

print(f"\nSlope (Coefficient): {model.coef_[0]:.4f}")
print(f"Intercept:           {model.intercept_:.4f}")

# ---------- Prediction ----------
y_pred = model.predict(X_test)
print(f"\nActual:    {y_test}")
print(f"Predicted: {y_pred}")

# ---------- Metrics ----------
mse = mean_squared_error(y_test, y_pred)
r2  = r2_score(y_test, y_pred)
print(f"\nMSE : {mse:.4f}")
print(f"RMSE: {np.sqrt(mse):.4f}")
print(f"R²  : {r2:.4f}")

# ---------- Plot ----------
plt.figure(figsize=(7, 5))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Regression Line')
plt.title('Simple Linear Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.tight_layout()
plt.savefig('exp3_simple_lr.png')
plt.show()
print("\nPlot saved as exp3_simple_lr.png")
print("Experiment 3 Complete!")
