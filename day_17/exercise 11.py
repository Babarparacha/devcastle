import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- CODE 11: E-COMMERCE CONVERSION RATES (CATPLOT/FACTORPLOT) ---

print("\n" + "="*60)
print("CODE 11: HOUR 3 - E-COMMERCE CONVERSION BY CHANNEL & SEASON")
print("="*60)

np.random.seed(42)
channels = ['Email', 'Social', 'Paid_Ads']
products = ['Electronics', 'Clothing', 'Home']
seasons = ['Spring', 'Summer', 'Fall', 'Winter']

conv_data = []
channel_list, product_list, season_list = [], [], []

for channel in channels:
    for product in products:
        for season in seasons:
            conversion_rate = np.random.uniform(0.02, 0.10)
            conv_data.extend([conversion_rate] * 20)
            channel_list.extend([channel] * 20)
            product_list.extend([product] * 20)
            season_list.extend([season] * 20)

df = pd.DataFrame({
    'channel': channel_list, 
    'product': product_list, 
    'season': season_list, 
    'conversion_rate': conv_data
})

g = sns.catplot(data=df, x='product', y='conversion_rate', hue='channel',
                col='season', kind='bar', height=4, aspect=1.2,
                col_order=['Spring', 'Summer', 'Fall', 'Winter'])
g.set_titles('Season: {col_name}')
g.set_axis_labels('Product Category', 'Conversion Rate')
plt.savefig('11_ecommerce_catplot.png', dpi=300, bbox_inches='tight')
plt.show()