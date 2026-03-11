import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- CODE 8: INSURANCE CLAIMS BY SEGMENT (STRIPPLOT & SWARMPLOT) ---

print("\n" + "="*60)
print("CODE 8: HOUR 3 - INSURANCE CLAIM FREQUENCY ANALYSIS")
print("="*60)

np.random.seed(42)
segments = ['Premium', 'Standard', 'Economy', 'Value']
claims_data = []
seg_list = []

for seg in segments:
    if seg == 'Premium':
        claims = np.random.poisson(2, 100)
    elif seg == 'Standard':
        claims = np.random.poisson(4, 100)
    elif seg == 'Economy':
        claims = np.random.poisson(6, 100)
    else:
        claims = np.random.poisson(8, 100)
    
    claims_data.extend(claims)
    seg_list.extend([seg] * 100)

df = pd.DataFrame({'segment': seg_list, 'annual_claims': claims_data})

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

sns.stripplot(data=df, x='segment', y='annual_claims', 
              ax=axes[0], jitter=True, alpha=0.6, size=6)
axes[0].set_title('Claim Frequency (Stripplot - Jittered)')
axes[0].set_ylabel('Annual Claims')

sns.swarmplot(data=df, x='segment', y='annual_claims', 
              ax=axes[1], size=6, palette='Set2')
axes[1].set_title('Claim Frequency (Swarmplot - Non-overlapping)')
axes[1].set_ylabel('Annual Claims')

plt.tight_layout()
plt.savefig('08_insurance_claims_stripplot.png', dpi=300, bbox_inches='tight')
plt.show()