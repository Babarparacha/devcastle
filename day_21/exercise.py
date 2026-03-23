import numpy as np
from sklearn.linear_model import LinearRegression

# Training Data
# square_ft = np.array([2000, 2500, 3000, 3500, 4000]).reshape(-1,1)
square_ft = np.array([2000, 2500, 3000, 3500, 4000])
price = np.array([300000, 350000, 400000, 450000, 500000])

# Create Model
model = LinearRegression()
# 1st way of doing it 
# # ===============Train Model===============
# model.fit(square_ft, price)

# # Get parameters
# m = model.coef_[0]
# b = model.intercept_

# print("Slope (m):", m)
# print("Intercept (b):", b)

# # Prediction
# new_house = [[3200]]
# predicted_price = model.predict(new_house)

# print("Predicted Price:", predicted_price[0])

#==============second way ==============

#====calculate_mean===========
x_mean=np.mean(square_ft)
y_mean=np.mean(price)
#=======calculate slope ==========
num_1=np.sum((square_ft-x_mean)*(price-y_mean))
num_2=np.sum((square_ft-x_mean)**2)
# =========find slope============
m=num_1/num_2
print("slope",m)
#===========find================
b=y_mean-m*x_mean
print("intercept",b)
#==========predict price using formula y=mx+b =============
x=3200
y=m*x+b
print(y)
