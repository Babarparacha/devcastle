import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# --------------------------------
# 1️⃣ Get Current Gold Data (Live)
# --------------------------------

symbol = "XAUUSD=X"   # Gold vs USD
df = yf.download(symbol, period="5d", interval="1h")

print("Latest Data:")
print(df.tail())

# --------------------------------
# 2️⃣ Calculate Indicators
# --------------------------------

# Simple Moving Average
df["SMA_20"] = df["Close"].rolling(20).mean()

# Exponential Moving Average
df["EMA_20"] = df["Close"].ewm(span=20).mean()

# RSI Calculation
delta = df["Close"].diff()
gain = delta.clip(lower=0)
loss = -delta.clip(upper=0)

avg_gain = gain.rolling(14).mean()
avg_loss = loss.rolling(14).mean()

rs = avg_gain / avg_loss
df["RSI"] = 100 - (100 / (1 + rs))

# --------------------------------
# 3️⃣ Trend Analysis
# --------------------------------

df["Trend"] = np.where(df["Close"] > df["SMA_20"], "Bullish", "Bearish")

# --------------------------------
# 4️⃣ Pattern Detection
# Example: Bullish Engulfing
# --------------------------------

df["Bullish_Engulfing"] = (
    (df["Close"] > df["Open"]) &
    (df["Close"].shift(1) < df["Open"].shift(1)) &
    (df["Close"] > df["Open"].shift(1)) &
    (df["Open"] < df["Close"].shift(1))
)

# --------------------------------
# 5️⃣ Simple Backtest Strategy
# Buy when:
# Close > SMA and RSI > 50
# --------------------------------

df["Buy_Signal"] = (df["Close"] > df["SMA_20"]) & (df["RSI"] > 50)

df["Return"] = df["Close"].pct_change()
df["Strategy_Return"] = df["Return"] * df["Buy_Signal"].shift(1)

df["Cumulative_Profit"] = (1 + df["Strategy_Return"]).cumprod()

print("\nStrategy Performance:")
print(df[["Close","SMA_20","RSI","Trend","Buy_Signal","Cumulative_Profit"]].tail())

# --------------------------------
# 6️⃣ Plot Price + SMA
# --------------------------------

plt.figure()
plt.plot(df["Close"])
plt.plot(df["SMA_20"])
plt.title("Gold (XAUUSD) - Live Data with SMA")
plt.show()