import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# --- CODE 10: LOAN APPROVAL ANALYSIS (COUNTPLOT) ---

print("\n" + "="*60)
print("CODE 10: HOUR 3 - LOAN APPROVAL DECISIONS (COUNTPLOT)")
print("="*60)

np.random.seed(42)
decisions = np.random.choice(['Approved', 'Rejected', 'Pending'], 500, p=[0.70, 0.20, 0.10])
demographics = np.random.choice(['Group_A', 'Group_B', 'Group_C'], 500)

df = pd.DataFrame({'decision': decisions, 'applicant_group': demographics})

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

sns.countplot(data=df, x='decision', ax=axes[0], palette='RdYlGn_r',
              order=['Approved', 'Pending', 'Rejected'])
axes[0].set_title('Loan Decision Frequency')
axes[0].set_ylabel('Count')
for container in axes[0].containers:
    axes[0].bar_label(container)

sns.countplot(data=df, x='applicant_group', hue='decision', ax=axes[1],
              palette='RdYlGn')
axes[1].set_title('Loan Decisions by Applicant Group')
axes[1].set_ylabel('Count')
axes[1].legend(title='Decision', loc='upper right')

plt.tight_layout()
plt.savefig('10_loan_approval_countplot.png', dpi=300, bbox_inches='tight')
plt.show()