# ============================================================
# EXPERIMENT 5: Time Series Analysis using AR / MA Model
# ============================================================
# Install if needed: pip install statsmodels

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

print("=" * 50)
print("EXPERIMENT 5: Time Series - AR and MA Model")
print("=" * 50)

# ---------- Generate Time Series Data ----------
np.random.seed(42)
n = 100
time_series = pd.Series(
    np.cumsum(np.random.randn(n)) + 50
)
print("\nFirst 10 values:\n", time_series.head(10))

# ---------- Plot Original Series ----------
plt.figure(figsize=(10, 4))
plt.plot(time_series, color='steelblue')
plt.title('Original Time Series')
plt.xlabel('Time')
plt.ylabel('Value')
plt.tight_layout()
plt.savefig('exp5_timeseries.png')
plt.show()

# ---------- ACF and PACF ----------
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
plot_acf(time_series, lags=20, ax=axes[0])
plot_pacf(time_series, lags=20, ax=axes[1])
plt.tight_layout()
plt.savefig('exp5_acf_pacf.png')
plt.show()
print("ACF/PACF plots saved.")

# ---------- AR Model ----------
print("\n--- AutoRegressive (AR) Model ---")
train = time_series[:80]
test  = time_series[80:]

ar_model = AutoReg(train, lags=2)
ar_result = ar_model.fit()
print(ar_result.summary())

ar_pred = ar_result.predict(start=80, end=99, dynamic=False)
print("\nAR Predictions:\n", ar_pred.values)

# ---------- MA Model (via ARIMA with p=0, d=0, q=1) ----------
print("\n--- Moving Average (MA) Model ---")
ma_model = ARIMA(train, order=(0, 0, 1))
ma_result = ma_model.fit()
print(ma_result.summary())

ma_pred = ma_result.forecast(steps=20)
print("\nMA Predictions:\n", ma_pred.values)

# ---------- Plot Predictions ----------
plt.figure(figsize=(10, 5))
plt.plot(time_series.index, time_series, label='Original', color='blue')
plt.plot(test.index, ar_pred.values, label='AR Predictions', color='red', linestyle='--')
plt.plot(test.index, ma_pred.values, label='MA Predictions', color='green', linestyle='-.')
plt.title('AR vs MA Model Predictions')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.tight_layout()
plt.savefig('exp5_ar_ma_predictions.png')
plt.show()
print("\nAll plots saved. Experiment 5 Complete!")
