import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error
import numpy as np 

data=pd.read_csv("F:\Python course\devcastle\machine_learninig\std.csv")
# print(data.head())
X=data[['hours']]
y=data[['score']]
model=LinearRegression()
model.fit(X,y)
predicted_Score=model.predict(X)

#evaluate
mae=mean_absolute_error(y,predicted_Score)
mse=mean_squared_error(y,predicted_Score)
rmse=np.sqrt(mse)

#show results
print("mean absolute error(MAE):",mae)
print("mean squared error(MAE):",mse)
print("root mean squared error(MAE):",rmse)


new_hour=float(input("enter a hour:"))
new_pred=model.predict([[new_hour]])
print(f"prediction for {new_hour} is score={new_pred[0]} ")

