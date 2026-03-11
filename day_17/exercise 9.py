import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# --- CODE 9: REGIONAL SALES COMPARISON (BARPLOT) ---

print("\n" + "="*60)
print("CODE 9: HOUR 3 - REGIONAL SALES PERFORMANCE (BARPLOT)")
print("="*60)

np.random.seed(42)
regions = ['North', 'South', 'East', 'West']
sales_data = []
region_list = []

for region in regions:
    if region == 'North':
        sales = np.random.normal(45, 15, 100)
    elif region == 'South':
        sales = np.random.normal(52, 14, 100)
    elif region == 'East':
        sales = np.random.normal(48, 16, 100)
    else:
        sales = np.random.normal(51, 15, 100)
    
    sales_data.extend(np.clip(sales, 10, 150))
    region_list.extend([region] * 100)

df = pd.DataFrame({'region': region_list, 'transaction_value': sales_data})

fig, ax = plt.subplots(figsize=(10, 6))

sns.barplot(data=df, x='region', y='transaction_value', 
            palette='Set2', errorbar='sd', ax=ax)
ax.set_title('Average Transaction Value by Region (with ±1 SD error bars)')
ax.set_ylabel('Transaction Value ($)')
ax.axhline(y=50, color='red', linestyle='--', label='Target: $50', alpha=0.7)
ax.legend()

plt.tight_layout()
plt.savefig('09_regional_sales_barplot.png', dpi=300, bbox_inches='tight')
plt.show()