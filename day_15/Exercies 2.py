import pandas as pd
# print("===== HOUR 1: INTRODUCTION TO PANDAS =====")
# Already introduced in lecture

# print("\n===== HOUR 2: SERIES & DATAFRAME & SELECTION =====")

# 1️ Creating a Series
ages = pd.Series([18, 20, 22, 21, 19], index=['Alice', 'Bob', 'Charlie', 'David', 'Eve'])
# print("Series of Ages:\n", ages)

# 2️ Creating a DataFrame

# print("\nDataFrame:\n", df)


# ==========================================
# print("\n===== OPERATIONS ON DATAFRAMES =====")

# Inspecting data
# print("\nFirst 3 rows:\n", df.head(3))
# print("\nLast 2 rows:\n", df.tail(2))

# Unique values
# print("\nUnique Cities:\n", df['City'].unique())

# Value counts
# print("\nNumber of students per city:\n", df['City'].value_counts())

# # Columns and index
# print("\nColumn Names:", df.columns)
# print("Index Labels:", df.index)

# # Sorting
# print("\nSort by Score descending:\n", df.sort_values(by='City', ascending=False,))

# Apply custom function (e.g., double score)
# df['DoubleScore'] = df['Score'].apply(lambda x: x*2)
# print("\nDouble Score Column:\n", df[['Name','DoubleScore']])
# print("\nDataFrame:\n", df)

# # Replace values
# df_replaced = df.replace({'Karachi': 'KHI'})
# print("\nReplace 'Karachi' with 'KHI':\n", df_replaced)

# Drop rows or columns
# df = df.drop(columns=['DoubleScore'])
# print("\nDataFrame:\n", df)
# print("\nDrop 'DoubleScore' column:\n", df)
# print("_________________________________________________")
# print("\nDataFrame:\n", df)


# # Null value check
pd.options.mode.use_inf_as_na = False
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [18, 20, 22, 21, 19],
    'City': ['Karachi', 'Lahore', None, 'Karachi', 'Lahore'],
    'Score': [85, 90, 78, 92, 'NA']
}
df = pd.DataFrame(data)
# print("\nCheck for missing values:\n", df.isnull())


import numpy as np
print(np.nan)