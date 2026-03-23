"""
Logistic Regression is a supervised machine learning algorithm used for classification 
problems. Unlike linear regression which predicts
 continuous values it predicts the probability that an input belongs to a specific class.
It is used for binary classification where the output can be one of
 two possible categories such as Yes/No, True/False or 0/1.
It uses sigmoid function to convert inputs into a probability value between 0 and 
"""
# Import necessary library
from sklearn.linear_model import LogisticRegression
import numpy as np

# Example data: X = independent variable(s), y = dependent variable
# Make sure X is 2D array (n_samples, n_features)
X = np.array([[1], [2], [3], [4], [5]])  # old data (feature)
y = np.array([2, 4, 6, 8, 10])           # old data (target/output)


model = LogisticRegression()

X=[[1],[2],[3],[4],[5]]
y=[40,50,65,75,90]
model.fit(X, y)


hours=float(input("enter how many hours you study:"))
result=model.predict([[hours]])[0]
if result==1:
    print(f"based on your {hours} you are likely to passed")
else:
    print(f"based on your {hours} you are likely to failed")
