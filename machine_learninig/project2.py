"""
3 step formula
1- x and y numeric? scatter plot (relationship)
2-one column category (bar plot/countt plot)
3- want to see distribution
shape? histogram/KDE plot/box plot
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import matplotlib.pyplot as plt
import numpy as np 

data=pd.read_csv("F:\Python course\devcastle\machine_learninig\student_records.csv")
#input and output
X = data[['study_hour_per_week']]   # 2D input required
y=data['final_score']
#train model
model=LinearRegression()
model.fit(X,y)
predicted_score=model.predict(X)
#============valid regression matrix==========

mae=mean_absolute_error(y,predicted_score)
mse=mean_squared_error(y,predicted_score)
rmse=np.sqrt(mse)
r2=r2_score(y,predicted_score)

#show results
print("mean absolute error(MAE):",round(mae,2))
print("mean squared error(MAE):",round(mse,2))
print("root mean squared error(MAE):",round(rmse,2))
print("R^2 score (Model accuracy):",round(r2,2))

#=========histogram==============
plt.figure(figsize=(10, 6))
plt.hist(data['final_score'], bins=10, color='skyblue', edgecolor='black')
plt.title("Distribution of Final Exam Score")
plt.xlabel("Final Score")
plt.ylabel("numbe of Students")
plt.grid(True)
plt.savefig("F:\Python course\devcastle\machine_learninig\histogram_plot.png")
plt.show()

## =======scattered plot
plt.figure(figsize=(10, 6))
plt.scatter(X, y ,label="Actual Data")
plt.plot(X, predicted_score,color="red",label="predicted score(Regression Line)")
plt.title("Model Prediction vs Actual predcition")
plt.xlabel("Study Hours Per Week")
plt.ylabel("Final output")
# plt.legend()
plt.grid(True)
plt.savefig("F:\Python course\devcastle\machine_learninig\scatter_plot.png", dpi=300, bbox_inches='tight')
plt.show()
# ============ box plot ============
plt.figure(figsize=(8, 5))
plt.boxplot(data['final_score'])
plt.ylabel("Final Score")
plt.title("Box Plot of Final Score")
plt.grid(True)
plt.savefig("F:\Python course\devcastle\machine_learninig\Box_plot.png")
plt.show()