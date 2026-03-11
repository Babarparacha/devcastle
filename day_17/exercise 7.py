import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# --- CODE 7: CUSTOMER TRANSACTIONS BY ACCOUNT TYPE (VIOLINPLOT) ---

print("\n" + "="*60)
print("CODE 7: HOUR 3 - BANK ACCOUNT TRANSACTION PATTERNS")
print("="*60)

np.random.seed(42)
account_types = ['Checking', 'Savings', 'Investment', 'Business']
transactions = []
account_list = []

for acc in account_types:
    if acc == 'Checking':
        amt = np.random.normal(150, 100, 200)
    elif acc == 'Savings':
        amt = np.random.normal(500, 200, 200)
    elif acc == 'Investment':
        amt = np.random.lognormal(8, 1.5, 200)
    else:
        amt = np.random.normal(2000, 500, 200)
    
    transactions.extend(np.clip(amt, 10, 10000))
    account_list.extend([acc] * 200)

df = pd.DataFrame({'account_type': account_list, 'transaction_amount': transactions})

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

sns.violinplot(data=df, x='account_type', y='transaction_amount', palette='muted', inner='box', ax=axes[0])
axes[0].set_title('Transaction Distribution by Account Type (Violin)')
axes[0].set_ylabel('Transaction Amount ($)')

sns.violinplot(data=df, x='account_type', y='transaction_amount', palette='muted', inner=None, ax=axes[1])
sns.stripplot(data=df, x='account_type', y='transaction_amount', color='black', alpha=0.4, size=4, jitter=True, ax=axes[1])
axes[1].set_title('Distribution + Individual Points (Stripplot Overlay)')
axes[1].set_ylabel('Transaction Amount ($)')

plt.tight_layout()
plt.savefig('07_account_transaction_violin.png', dpi=300, bbox_inches='tight')
plt.show()