import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- CODE 1: HOUR 1 - TRADING DASHBOARD ---

print("\n" + "="*60)
print("CODE 1: HOUR 1 - TRADING VOLUME & PRICE MOVEMENT DASHBOARD")
print("="*60)

# Fix: Use correct repetition to get exactly 100 rows
# 100 / 3 = 33 remainder 1, so: * 33 + [1 element]
trading_data = {
    'date': pd.date_range('2024-01-01', periods=100),
    'stock': ['TECH', 'FINANCE', 'HEALTHCARE'] * 33 + ['TECH'],  # FIXED: 99 + 1 = 100
    'daily_volume_millions': [1.2, 2.3, 0.8] * 33 + [1.5],       # FIXED: 99 + 1 = 100
    'price_change_percent': [-0.5, 1.2, 0.3] * 33 + [0.8]        # FIXED: 99 + 1 = 100
}
df = pd.DataFrame(trading_data)

sns.set_style("whitegrid")
sns.set_palette("husl")

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

sns.histplot(data=df, x='daily_volume_millions', kde=True, ax=axes[0, 0])
axes[0, 0].set_title('Trading Volume Distribution')

sns.boxplot(data=df, x='stock', y='price_change_percent', ax=axes[0, 1])
axes[0, 1].set_title('Price Movement by Stock')

sns.scatterplot(data=df, x='daily_volume_millions', y='price_change_percent', 
                hue='stock', ax=axes[1, 0], alpha=0.6)
axes[1, 0].set_title('Volume vs Price Correlation')

sns.countplot(data=df, x='stock', ax=axes[1, 1])
axes[1, 1].set_title('Trading Days by Stock')

plt.tight_layout()
plt.savefig('01_trading_dashboard.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n✓ CODE 1 Executed Successfully")