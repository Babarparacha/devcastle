import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler,MinMaxScaler
from sklearn.model_selection import train_test_split
# data={
#     "name":['ahsan','noman','jameel','babar'],
#     "age":[30,None,50,29],
#     "salary":[30000,40000,50000,None]
#     # "city":['lahore','karachi','bahawalnagar'],
# }
# df=pd.DataFrame(data)
# print(df.isnull().sum()) #========sum of missing values
# drop_none_data=df.dropna() #======drop none data
# print(drop_none_data)
# fill missing values 
# df['age'].fillna(df['age'].mean(),inplace=True)
# df['age']=df['age'].round(1)
# df['salary'].fillna(df['salary'].mean(),inplace=True)
# print(df)

#=============== check percentage of data missing before cleaning 
# print(df.isnull().mean()*100)

#======================================

# Read CSV file
# Use raw string r'' so that backslashes don't create escape errors
# df = pd.read_csv(r'F:\Python course\devcastle\machine_learninig\employees_demo_data.csv')

# # Make a copy of dataframe so original data stays unchanged
# df_label = df.copy()
# # Create LabelEncoder object
# le = LabelEncoder()

""" LabelEncoder is a preprocessing tool from the scikit-learn library that converts
  categorical (text) data into numerical labels so that machine learning algorithms can process the data.
"""
# Encode 'age' column
# df_label['age_Encoded'] = le.fit_transform(df_label['age'])

# Encode 'department' column
# df_label['department_Encoded'] = le.fit_transform(df_label['department'])

# Print heading
# print('\nLabel encoded data')

# Show first 5 rows with original and encoded columns
# print(df_label[['name', 'age', 'age_Encoded', 'department', 'department_Encoded']].head())

"""One-Hot Encoding is a technique used in Machine Learning to convert categorical data into binary (0 or 1) columns so algorithms can process it properly.
 It is commonly used with tools in scikit-learn and pandas.
One-Hot Encoding creates a separate column for each category and marks the presence of a category with 1 and the absence with 0."""

# Apply One-Hot Encoding on department column
# df_encoded = pd.get_dummies(df, columns=['department']) #=== return true or false
# df_encoded = pd.get_dummies(df, columns=['department'],dtype=int)  #======return 0,1

# print("One Hot Encoded Data")
# print(df_encoded.head())


data={
    'studyHours':[1,2,3,4,5],
    'testScore':[40,50,60,70,80]
}
df=pd.DataFrame(data)
# Create an instance of StandardScaler
# standard_scaler = StandardScaler()  # This object will standardize features by removing the mean and scaling to unit variance

# Fit the scaler to the data and transform it
# standard_scaled = standard_scaler.fit_transform(df)  
"""'fit_transform' does two things:
1. fit() calculates the mean and standard deviation for each column in the DataFrame 'df'
2. transform() scales the data: (value - mean) / standard deviation"""

# Print a message to indicate what transformation was done
print('standard scaler')

# Convert the scaled data back into a pandas DataFrame for readability and label columns
# This shows the standardized values of 'studyHours' and 'testScore' after scaling
# print(pd.DataFrame(standard_scaled, columns=['studyHours', 'testScore']))

# Create an instance of MinMaxScaler
min_scaler = MinMaxScaler()
"""MinMaxScaler scales features to a given range (default 0 to 1).
fit_transform() learns the min and max from the data and scales it.
Converting back to a DataFrame with column names makes it easy to interpret."""
# Fit the scaler to the dataframe 'df' and transform the values to a 0-1 range
max_scaled = min_scaler.fit_transform(df)

# Print a message to indicate that Min-Max scaling has been applied
print("MinMax Scaler:")

# Convert the scaled array back to a DataFrame for easier readability and set column names
print(pd.DataFrame(max_scaled, columns=['studyHours', 'testScore']))
# 2. Define features (X) and target (y)
x = df[['studyHours']]   # Feature(s)
y = df[['testScore']]    # Target variable (corrected typo: 'testScores' -> 'testScore')


# 3. Split data into training and testing sets
# Typically, test_size=0.2 means 20% test, 80% train
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.8, random_state=42)

# Print shapes to verify split
print("X_train shape:", x_train)
print("X_test shape:", x_test)
print("Y_train shape:", y_train)
print("Y_test shape:", y_test)

# formula z=x−μ​/σ
# Where:
# x = the original value of a feature
# μ = mean of the feature (average of all values in that column)
# σ = standard deviation of the feature (how spread out the values are)
# z = standardized value after scaling