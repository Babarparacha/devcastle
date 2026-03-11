import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# --- CODE 3: MARKETING SPEND vs REVENUE (JOINTPLOT) ---

print("\n" + "="*60)
print("CODE 3: HOUR 2 - MARKETING SPEND vs REVENUE CORRELATION")
print("="*60)

np.random.seed(42)
marketing = np.random.normal(5000, 2000, 100)
revenue = 2.5 * marketing + np.random.normal(0, 3000, 100)

df = pd.DataFrame({
    'marketing_spend_usd': np.clip(marketing, 500, 15000),
    'revenue_generated_usd': np.clip(revenue, 1000, 50000)
})

g = sns.jointplot(data=df, x='marketing_spend_usd', y='revenue_generated_usd', 
                  kind='scatter', height=8)
g.plot_joint(sns.regplot, scatter=False, color='red', line_kws={'linewidth': 2})
corr = df['marketing_spend_usd'].corr(df['revenue_generated_usd'])
g.ax_joint.text(0.05, 0.95, f'Correlation: {corr:.3f}\nROI: 2.5x',
                transform=g.ax_joint.transAxes, fontsize=11, 
                bbox=dict(boxstyle='round', facecolor='wheat'))
g.set_axis_labels('Marketing Spend ($)', 'Revenue Generated ($)')
plt.savefig('03_marketing_revenue_correlation.png', dpi=300, bbox_inches='tight')
plt.show()