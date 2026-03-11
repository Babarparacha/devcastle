import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# ============================================================================
# CATEGORICAL DATA PLOTS
# ============================================================================
# --- CODE 6: DEPARTMENT SPENDING (BOXPLOT) ---

print("\n" + "="*60)
print("CODE 6: HOUR 3 - DEPARTMENT SPENDING ANALYSIS")
print("="*60)

np.random.seed(42)
departments = ['Finance', 'Marketing', 'Operations', 'Sales', 'HR']
spending_data = []
dept_list = []

for dept in departments:
    if dept == 'Finance':
        spending = np.random.normal(250, 30, 50)
    elif dept == 'Marketing':
        spending = np.random.normal(180, 80, 50)
    else:
        spending = np.random.normal(150, 40, 50)
    
    spending_data.extend(np.clip(spending, 50, 400))
    dept_list.extend([dept] * 50)

df = pd.DataFrame({'department': dept_list, 'monthly_spend_usd': spending_data})

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

sns.boxplot(data=df, x='department', y='monthly_spend_usd', ax=axes[0], palette='Set2')
axes[0].set_title('Spending Distribution by Department')
axes[0].axhline(y=200, color='red', linestyle='--', label='Budget Cap', alpha=0.7)
axes[0].legend()

sns.boxplot(data=df, x='department', y='monthly_spend_usd', ax=axes[1], palette='Set2')
sns.stripplot(data=df, x='department', y='monthly_spend_usd', 
              color='black', alpha=0.3, size=3, ax=axes[1])
axes[1].set_title('Spending + Individual Transactions')

plt.tight_layout()
plt.savefig('06_department_spending_boxplot.png', dpi=300, bbox_inches='tight')
plt.show()