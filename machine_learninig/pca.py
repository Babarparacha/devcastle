import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

#sample data
data={
    "income":[30000,40000,250000,500000,60000],
    "Age":[20,30,50,40,30],
    "Spending":[100,200,300,400,500]
}
df=pd.DataFrame(data)
scaler=StandardScaler()
scaler_data=scaler.fit_transform(df)
pca=PCA(n_components=2)
pca_result=pca.fit_transform(scaler_data)
pca_df=pd.DataFrame(pca_result,columns=['PCA1','PCA2'])

explain_variance=pca.explained_variance_ratio_
print('variance captured by each pca component')
print(np.round(explain_variance*100,2))


plt.figure(figsize=(8,6))
plt.scatter(pca_df['PCA1'],pca_df['PCA2'],color='black',s=80)
plt.title("PCA projection(2D view)")
plt.xlabel("PCA 1 pattern")
plt.ylabel("PCA 2 pattern")
plt.grid(True)
plt.show()
print("new data with PCA1 and PC2")
print(pca_df)

# PCA is used when you have many columns/features and you want to reduce them into fewer 
# columns while keeping most of the important information.
# Here you have 3 original features:
# income
# Age
# Spending
# Then PCA reduces these 3 columns into 2 new columns:
# PCA1
# PCA2
# These new columns are combinations of the old columns.