"""K-Means Clustering groups similar data points into clusters without needing labeled data.
 It is used to uncover hidden patterns when the goal is to organize data based on similarity.
.Helps identify natural groupings in unlabeled datasets
.Works by grouping points based on distance to cluster centers
.Commonly used in customer segmentation, image compression, and pattern discovery
.Useful when you need structure from raw, unorganized data"""

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#sample data
data={
    "Csutomer":['asad','badar','ahsan','awais','wajid'],
    "Age":[20,30,50,40,30],
    "Spending":[100,200,300,400,500]
}
df=pd.DataFrame(data)
X=df[['Age','Spending']]
# 1. n_clusters
# Tells KMeans how many groups (clusters) to make.
# Example:
# n_clusters=2 → make 2 clusters
# n_clusters=3 → make 3 clusters
# 2. random_state
# Controls the random starting points of clusters.
# KMeans starts with random centers first.
# If you use the same random_state, you get the same result every time.
# Example:
# random_state=42 means results stay repeatable.
# 3. n_init
# Tells KMeans how many times to run with different starting points.
# Then it picks the best result.
# Example:
# n_init=10 means KMeans will try 10 different initial positions and choose the best one.

model = KMeans(n_clusters=2, random_state=42, n_init=10)

# Fit the model and predict cluster labels
df['Group'] = model.fit_predict(X)
print(df)
plt.figure(figsize=(6,5))
for group in df['Group'].unique():   # [0, 1]
    group_data = df[df['Group'] == group]
    plt.scatter(group_data['Age'], group_data['Spending'], label=f"Group {group}")

plt.xlabel("Age")
plt.ylabel("Spending Score")
plt.title("Customer Segment (K-Means)")
plt.legend()
plt.grid(True)
plt.show()

