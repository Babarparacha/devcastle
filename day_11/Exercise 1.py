import pandas as pd

# The FBR Database: Income vs House Size
data = {
    "study_hours": [1,2,3],
    "test_scores": [2,4,6]
    }
# data1 = data['study_hours']
# print(data1)
# Load the data into a Pandas DataFrame (like an Excel sheet)
df = pd.DataFrame(data)
print(df)
# Calculate the Correlation Matrix
correlation = df["study_hours"].corr(df["test_scores"])

print(f"Correlation Score: {correlation:.2f}")


