import numpy as np
from sklearn.linear_model import LinearRegression

# Training Data
square_ft = np.array([2000, 2500, 3000, 3500, 4000]).reshape(-1,1)
price = np.array([300000, 350000, 400000, 450000, 500000])

# Create Model
model = LinearRegression()

# Train Model
model.fit(square_ft, price)

# Get parameters
m = model.coef_[0]
b = model.intercept_

print("Slope (m):", m)
print("Intercept (b):", b)

# Prediction
new_house = [[3200]]
predicted_price = model.predict(new_house)

print("Predicted Price:", predicted_price[0])