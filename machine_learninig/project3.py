# =======================
# Import Libraries
# =======================
import pandas as pd
import numpy as np
# Preprocessing
from sklearn.preprocessing import LabelEncoder, StandardScaler
# Model
from sklearn.linear_model import LogisticRegression
# Correct import
from sklearn.model_selection import train_test_split
# Evaluation
from sklearn.metrics import classification_report, confusion_matrix
# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
# =======================
# Load Dataset
# =======================
# Use raw string (r"") to avoid path errors
df = pd.read_csv(r"F:\Python course\devcastle\machine_learninig\std.csv")
# print("dataset shape") 
# # print(f" Rows:{df.shape[0]},columns:{df.shape[1]}")
#  # print("dataset info")
#  # print(df.info()) 
# # print("summary prediction")
#  # print(df.describe(include="all"))
#  # print("missing values")
#  # print(df.isnull().sum())

# =======================
# Encode Categorical Data
# =======================
le = LabelEncoder()

df['internet'] = le.fit_transform(df['internet'])   # yes=1, no=0
df['passed'] = le.fit_transform(df['passed'])       # yes=1, no=0


# =======================
# Feature Selection
# =======================
# ⚠️ Make sure these column names EXACTLY match your CSV
features = ['hours', 'attendence', 'score', 'sleepHours']

# Normalize data (important for ML models)
scaler = StandardScaler()

df_scaled = df.copy()
df_scaled[features] = scaler.fit_transform(df[features])

# Split features and target
X = df_scaled[features]
y = df_scaled['passed']

# =======================
# Train-Test Split
# =======================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42   # better split
)
# =======================
# Train Model
# =======================
model = LogisticRegression()
model.fit(X_train, y_train)

# =======================
# Predictions & Evaluation
# =======================
y_pred = model.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred))
# =======================
# Confusion Matrix
# =======================
conf_matrix = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 4))
sns.heatmap(
    conf_matrix,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Fail", "Pass"],
    yticklabels=["Fail", "Pass"]
)
plt.xlabel("Predicted")
plt.ylabel("Actual")   # fixed typo
plt.title("Confusion Matrix")
plt.show()

# =======================
# User Prediction Section
# =======================
print("----------- Predict Your Result -----------")
try:
    # Take input from user
    study_hour = float(input("Enter your Study Hours: "))
    attendence = float(input("Enter attendence: "))
    score = float(input("Enter Score: "))
    sleep_hour = float(input("Enter Sleep Hours: "))
    # Create DataFrame with SAME column names as training data
    user_input_df = pd.DataFrame([{
        'hours': study_hour,
        'attendence': attendence,
        'score': score,
        'sleepHours': sleep_hour
    }])
    # Apply SAME scaling used during training
    user_input_scaled = scaler.transform(user_input_df)

    # Make prediction (no indexing mistake)
    prediction = model.predict(user_input_scaled)[0]
    result = "Pass" if prediction == 1 else "Fail"
    print(f"Prediction: {result}")

except Exception as e:
    print("An error occurred:", e)