import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# --- CODE 2: TAX INCOME DISTRIBUTION ---

print("\n" + "="*60)
print("CODE 2: HOUR 2 - TAX AUTHORITY INCOME DISTRIBUTION")
print("="*60)

np.random.seed(42)
incomes = np.concatenate([
    np.random.normal(35000, 10000, 800),
    np.random.normal(150000, 50000, 150),
    np.random.exponential(30000, 50)
])

df = pd.DataFrame({'annual_income': incomes})

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

sns.histplot(data=df, x='annual_income', kde=True, bins=40, ax=axes[0])
axes[0].set_title('Income Distribution (All Taxpayers)')
axes[0].axvline(df['annual_income'].median(), color='red', linestyle='--', label='Median')
axes[0].legend()

df['bracket'] = pd.cut(df['annual_income'], bins=[0, 50000, 100000, 500000], 
                       labels=['<$50K', '$50-100K', '>$100K'])
sns.histplot(data=df, x='annual_income', kde=True, hue='bracket', ax=axes[1], bins=30)
axes[1].set_title('Distribution by Tax Bracket')

plt.tight_layout()
plt.savefig('02_tax_income_distribution.png', dpi=300, bbox_inches='tight')
plt.show()