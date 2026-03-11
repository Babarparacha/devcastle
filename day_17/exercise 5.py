import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# --- CODE 5: ATM WITHDRAWAL PATTERNS (KDE + RUGPLOT) ---

print("\n" + "="*60)
print("CODE 5: HOUR 2 - ATM WITHDRAWAL DENSITY & DISTRIBUTION")
print("="*60)

np.random.seed(42)
morning_small = np.random.normal(75, 20, 600)
weekly_large = np.random.normal(500, 100, 400)
withdrawals = np.concatenate([morning_small, weekly_large])

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

sns.kdeplot(data=withdrawals, ax=axes[0], fill=True, color='steelblue')
axes[0].set_title('Withdrawal Amount Density (Bimodal Distribution)')
axes[0].set_xlabel('Withdrawal Amount ($)')

sns.kdeplot(data=withdrawals, ax=axes[1], fill=True, color='steelblue')
sns.rugplot(data=withdrawals, ax=axes[1], height=0.05, color='black', alpha=0.3)
axes[1].set_title('Density + Individual Transactions (Rug Marks)')
axes[1].set_xlabel('Withdrawal Amount ($)')

plt.tight_layout()
plt.savefig('05_atm_withdrawal_kde.png', dpi=300, bbox_inches='tight')
plt.show()