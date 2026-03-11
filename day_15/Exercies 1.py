# ==========================================
# Pandas Full Demo – Series, DataFrame & Operations
# ==========================================

import pandas as pd
import numpy as np

# print("===== HOUR 1: INTRODUCTION TO PANDAS =====")
# # Already introduced in lecture

# print("\n===== HOUR 2: SERIES & DATAFRAME & SELECTION =====")

# 1️ Creating a Series
ages = pd.Series([18, 20, 22, 21, 19], index=['Alice', 'Bob', 'Charlie', 'David', 'Eve'])
# print("Series of Ages:\n", ages)

# 2️ Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [18, 20, 22, 21, 19],
    'City': ['Karachi', 'Lahore', 'Islamabad', 'Karachi', 'Lahore'],
    'Score': [85, 90, 78, 92, 88]
}
df = pd.DataFrame(data)
# print("\nDataFrame:\n", df)

# 3️ Selection and Indexing
# print("\nAccess Column 'Name':\n", df['Name'])
# print("\nAccess Row by index 2:\n", df.iloc[2])
# print("\nAccess Row by label using loc:\n", df.loc[1])
# print("\nSubset (Name and Score for first 3 rows):\n", df.loc[:2, ['Name','Score']])

# # Conditional selection
# high_score = df[df['Score'] > 85]
# print("\nStudents with Score > 85:\n", high_score)

# # Setting index
# df_indexed = df.set_index('Name')
# print("\nDataFrame with 'Name' as index:\n", df_indexed)


# # ==========================================
