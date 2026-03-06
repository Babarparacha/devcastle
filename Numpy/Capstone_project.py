# ================================
# Import necessary libraries
# ================================
import numpy as np
import pandas as pd

# ================================
# Load the CSV dataset
# ================================
df = pd.read_csv('employees_demo_data.csv')

print("Initial Dataset Shape:", df.shape)

# ================================
# Check missing values
# ================================
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# ================================
# FIX DATA TYPES
# ================================

# Fix rating column:
# 1) Replace string 'NAN' with actual NaN
df['rating'] = df['rating'].replace('NAN', np.nan)

# 2) Convert rating to numeric
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

# Convert salary to numeric if needed
df['salary(pk)'] = pd.to_numeric(df['salary(pk)'], errors='coerce')

# ================================
# Handle missing values
# ================================
# Fill missing salary with mean
# df['salary(pk)'].fillna(df['salary(pk)'].mean(), inplace=True)
df['salary(pk)'] = df['salary(pk)'].fillna(df['salary(pk)'].mean())
# Fill missing rating with median
# df['rating'].fillna(df['rating'].median(), inplace=True)
df['rating'] = df['rating'].fillna(df['rating'].median())
df['rating'] = df['rating'].round(1)
# Replace infinite values with NaN
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Fill remaining NaN values (numeric columns only)
df.fillna(df.select_dtypes(include=np.number).mean(), inplace=True)

# ================================
# Remove duplicate records
# ================================
df.drop_duplicates(inplace=True)

# ================================
# Handle negative salary values
# ================================
salary_mean = df['salary(pk)'].mean()

df['salary(pk)'] = np.where(
    df['salary(pk)'] < 0,
    salary_mean,
    df['salary(pk)']
)

# ================================
# Outlier detection (3-sigma rule)
# ================================
salary_std = df['salary(pk)'].std()

lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)

# Remove outliers
df = df[
    (df['salary(pk)'] >= lower_bound) &
    (df['salary(pk)'] <= upper_bound)
]

# ================================
# Final checks
# ================================
print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nFinal Dataset Shape:", df.shape)

# ================================
# Save cleaned dataset
# ================================
df.to_csv('cleaned_pk_emp_data.csv', index=False)

print("\n✅ Data cleaning completed successfully!")
print("📁 File saved as: cleaned_pk_emp_data.csv")