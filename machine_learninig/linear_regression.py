"""
Linear regression predicts a continuous value by fitting a straight line between 
input and output variables.
 Example: Predicting house prices based on area or predicting weight from height.
Linear regression is a type of supervised machine-learning algorithm that learns from the 
labelled datasets and maps the data points with most optimized linear functions which 
can be used for prediction on new datasets.
1- find a pattern  in old data
2-straight liney=m*x+b
"""
# Import necessary library
from sklearn.linear_model import LinearRegression,LogisticRegression
import numpy as np

# Example data: X = independent variable(s), y = dependent variable
# Make sure X is 2D array (n_samples, n_features)
X = np.array([[1], [2], [3], [4], [5]])  # old data (feature)
y = np.array([2, 4, 6, 8, 10])           # old data (target/output)

# 1. Create a Linear Regression model
# Linear regression finds a straight line y = m*x + b that fits the data
model = LinearRegression()

# 2. Fit the model on old data
# This step calculates the slope (m) and intercept (b) of the best-fit line
"""Import libraries – sklearn for regression, numpy for array handling.
1-Prepare data – X must be 2D; y can be 1D.
2-reate and fit model – Finds the best straight line.
3-Predict – Pass new values in 2D format ([[value]]).
4-Optional info – You can check the slope and intercept of the line."""

X=[[1],[2],[3],[4],[5]]
y=[40,50,65,75,90]
# fit() is used to train the model
# It learns the relationship between input data (X = study hours)
# and output data (y = scores)
model.fit(X, y)
# predict() is used after training the model
# It gives a predicted result for new input data
# Here it predicts the score based on entered study hours

# 3. Predict using the trained model
# value = 6  # new input value for prediction
# prediction = model.predict([[value]])  # model expects a 2D array

# # 4. Output the result
# print(f"Predicted value for X={value}: {prediction[0]}")

# # Optional: view the slope (m) and intercept (b)
# print(f"Slope (m): {model.coef_[0]}")
# print(f"Intercept (b): {model.intercept_}")

# second example linear regression

hours=float(input("enter how many hours you study:"))
predicted_hours=model.predict([[hours]])
print(f" based on your {hours} you have score around {predicted_hours[0]}")

