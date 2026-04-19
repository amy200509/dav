# ============================================================
# EXPERIMENT 6: Implementation of ARIMA Model
# ============================================================
# Install if needed: pip install statsmodels

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller
from sklearn.metrics import mean_squared_error

print("=" * 50)
print("EXPERIMENT 6: ARIMA Model")
print("=" * 50)

# ---------- Generate Data ----------
np.random.seed(42)
n = 120
data = pd.Series(np.cumsum(np.random.randn(n)) + 100)
print("\nSample Data (first 10):\n", data.head(10))

# ---------- ADF Test (Stationarity) ----------
print("\n--- Augmented Dickey-Fuller Test ---")
result = adfuller(data)
print(f"ADF Statistic : {result[0]:.4f}")
print(f"p-value       : {result[1]:.4f}")
if result[1] > 0.05:
    print("Series is NON-STATIONARY → Differencing needed (d=1)")
else:
    print("Series is STATIONARY")

# ---------- Differencing (if needed) ----------
data_diff = data.diff().dropna()

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(data, color='blue')
plt.title('Original Series')

plt.subplot(1, 2, 2)
plt.plot(data_diff, color='orange')
plt.title('Differenced Series (d=1)')
plt.tight_layout()
plt.savefig('exp6_arima_diff.png')
plt.show()

# ---------- Train / Test Split ----------
train = data[:100]
test  = data[100:]

# ---------- Fit ARIMA(1,1,1) ----------
print("\n--- Fitting ARIMA(1,1,1) ---")
model = ARIMA(train, order=(1, 1, 1))
fitted = model.fit()
print(fitted.summary())

# ---------- Forecast ----------
forecast_result = fitted.forecast(steps=20)
print("\nForecast values:\n", forecast_result.values)

# ---------- Evaluate ----------
mse  = mean_squared_error(test, forecast_result)
rmse = np.sqrt(mse)
print(f"\nMSE : {mse:.4f}")
print(f"RMSE: {rmse:.4f}")

# ---------- Plot ----------
plt.figure(figsize=(10, 5))
plt.plot(data.index, data, label='Actual', color='blue')
plt.plot(test.index, forecast_result.values, label='ARIMA Forecast', color='red', linestyle='--')
plt.title('ARIMA(1,1,1) - Forecast vs Actual')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.tight_layout()
plt.savefig('exp6_arima_forecast.png')
plt.show()
print("\nPlots saved. Experiment 6 Complete!")
