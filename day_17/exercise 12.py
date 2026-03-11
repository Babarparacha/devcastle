import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# --- CODE 12: FINANCIAL INDICATORS CORRELATION (HEATMAP) ---

print("\n" + "="*60)
print("CODE 12: HOUR 4 - FINANCIAL MARKET CORRELATION HEATMAP")
print("="*60)

np.random.seed(42)
n = 200

fed_rate = np.random.normal(5.0, 0.5, n)
stock_returns = 0.7 * fed_rate + np.random.normal(0, 2, n)
bond_yields = 0.8 * fed_rate + np.random.normal(0, 1, n)
corp_spreads = -0.6 * fed_rate + np.random.normal(0, 2, n)
volatility = 0.5 * fed_rate + np.random.normal(0, 2, n)

corr_df = pd.DataFrame({
    'FED_Rate': fed_rate,
    'Stock_Returns': stock_returns,
    'Bond_Yields': bond_yields,
    'Corp_Spreads': corp_spreads,
    'Volatility': volatility
})

corr_matrix = corr_df.corr()

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', center=0,
            ax=axes[0], square=True, linewidths=1, cbar_kws={'label': 'Correlation'},
            vmin=-1, vmax=1)
axes[0].set_title('Financial Indicators Correlation Matrix')

income_bracket = pd.cut(corr_df['Stock_Returns'], bins=5, 
                        labels=['Very_Low', 'Low', 'Medium', 'High', 'Very_High'])
return_complexity = pd.cut(corr_df['Volatility'], bins=3, 
                           labels=['Simple', 'Medium', 'Complex'])
contingency = pd.crosstab(income_bracket, return_complexity)

sns.heatmap(contingency, annot=True, fmt='d', cmap='YlOrRd', ax=axes[1],
            cbar_kws={'label': 'Frequency'}, linewidths=1)
axes[1].set_title('Income Bracket × Complexity\n(Fraud Pattern Detection)')

plt.tight_layout()
plt.savefig('12_financial_correlation_heatmap.png', dpi=300, bbox_inches='tight')
plt.show()