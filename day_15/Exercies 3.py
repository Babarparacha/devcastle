import pandas as pd
import numpy as np
print("===== HOUR 1: INTRODUCTION TO PANDAS =====")
# Already introduced in lecture

print("\n===== HOUR 2: SERIES & DATAFRAME & SELECTION =====")

# 1️ Creating a Series
ages = pd.Series([18, 20, 22, 21, 19], index=['Alice', 'Bob', 'Charlie', 'David', 'Eve'])
print("Series of Ages:\n", ages)

# 2️ Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [18, 20, 22, 21, 19],
    'City': ['Karachi', 'Lahore', 'Islamabad', 'Karachi', 'Lahore'],
    'Score': [85, 90, 78, 92, 88]
}
# df = pd.DataFrame(data)
# print("\nDataFrame:\n", df)

print("\n===== HOUR 4: MISSING DATA & HANDLING =====")

# Create DataFrame with missing values
data_missing = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [18, np.nan, 22, 21, np.nan],
    'Score': [85, 90, np.nan, 92, 88]
}
df_missing = pd.DataFrame(data_missing)
print("\nDataFrame with missing values:\n", df_missing)

# # Drop rows with missing data
# df_drop = df_missing.dropna()
# print("\nDrop rows with missing values:\n", df_drop)

# # Fill missing data
# df_fill_mean = df_missing.copy()

# df_fill_mean['Age'] = df_fill_mean['Age'].fillna(df_fill_mean['Age'].mean())

# df_fill_mean['Score'] = df_fill_mean['Score'].fillna(df_fill_mean['Score'].mean())

# print("\nFill missing values with column mean:\n", df_fill_mean)

# # Forward fill
# df_ffill = df_missing.fillna(method='ffill')
# print("\nForward fill missing values:\n", df_ffill)

# # Backward fill
# df_bfill = df_missing.fillna(method='bfill')
# print("\nBackward fill missing values:\n", df_bfill)