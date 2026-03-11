import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# --- CODE 4: PORTFOLIO ASSET CLASSES (PAIRPLOT) ---

print("\n" + "="*60)
print("CODE 4: HOUR 2 - PORTFOLIO ASSET CLASS CORRELATIONS")
print("="*60)

np.random.seed(42)
portfolio = pd.DataFrame({
    'stocks': np.random.normal(8, 15, 60),
    'bonds': np.random.normal(3, 5, 60),
    'commodities': np.random.normal(2, 20, 60),
    'real_estate': np.random.normal(6, 12, 60),
    'cash': np.random.normal(1, 0.5, 60)
})

g = sns.pairplot(portfolio, diag_kind='kde', plot_kws={'alpha': 0.6})
g.fig.suptitle('Asset Class Correlation Matrix', y=1.00)
plt.savefig('04_portfolio_pairplot.png', dpi=300, bbox_inches='tight')
plt.show()