import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- CODE 13: STOCK PORTFOLIO CLUSTERING (CLUSTERMAP) ---

print("\n" + "="*60)
print("CODE 13: HOUR 4 - STOCK CORRELATION WITH CLUSTERING")
print("="*60)

np.random.seed(42)
stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META',
          'JPM', 'BAC', 'GS', 'WFC',
          'JNJ', 'PFE', 'UNH', 'AbbV',
          'XOM', 'CVX', 'MPC',
          'PEP', 'KO', 'MCD','ASF']

returns = np.random.multivariate_normal(
    mean=[0]*20,
    cov=np.eye(20) + 0.5*np.random.randn(20, 20),
    size=20
).T

stock_returns_df = pd.DataFrame(returns, columns=stocks)
corr = stock_returns_df.corr()

g = sns.clustermap(corr, cmap='coolwarm', center=0, vmin=-1, vmax=1,
                   figsize=(12, 12), method='ward', metric='euclidean',
                   cbar_kws={'label': 'Correlation'}, linewidths=0.5)
# g.title('Stock Correlation with Hierarchical Clustering\n(Groups similar-performing stocks)', 
#             fontsize=12, y=0.98)
plt.savefig('13_stock_clustermap.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n" + "="*60)
print("✓ ALL 13 CODES EXECUTED SUCCESSFULLY")
print("✓ All images saved to current directory")
print("="*60)