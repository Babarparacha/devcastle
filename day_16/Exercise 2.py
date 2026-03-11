import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample dataset
data = pd.DataFrame({
    "Month":["Jan","Feb","Mar","Apr","May","Jun"],
    "Sales":[200,300,250,400,350,500],
    "Profit":[50,80,60,120,90,150],
    "Users":[1000,1200,1100,1500,1700,2000]
})

data.set_index("Month", inplace=True)

# -----------------------------
# Area Plot
# -----------------------------
data.plot.area(title="Area Plot")
plt.show()

# -----------------------------
# Bar Plot
# -----------------------------
data.plot.bar(title="Bar Plot")
plt.show()

# -----------------------------
# Horizontal Bar Plot
# -----------------------------
data.plot.barh(title="Horizontal Bar Plot")
plt.show()

# -----------------------------
# Line Plot
# -----------------------------
data.plot.line(title="Line Plot")
plt.show()

# -----------------------------
# Histogram
# -----------------------------
data["Sales"].plot.hist(title="Histogram")
plt.show()

# -----------------------------
# Density Plot
# -----------------------------
data["Sales"].plot.density(title="Density Plot")
plt.show()

# -----------------------------
# Box Plot
# -----------------------------
data.plot.box(title="Box Plot")
plt.show()

# -----------------------------
# KDE Plot
# -----------------------------
data["Profit"].plot.kde(title="KDE Plot")
plt.show()

# -----------------------------
# Scatter Plot
# -----------------------------
data.plot.scatter(x="Sales", y="Profit", title="Scatter Plot")
plt.show()

# -----------------------------
# Hexbin Plot
# -----------------------------
data.plot.hexbin(x="Sales", y="Profit", gridsize=10, title="Hexbin Plot")
plt.show()

# -----------------------------
# Pie Plot
# -----------------------------
data["Sales"].plot.pie(autopct="%1.1f%%", title="Pie Chart")
plt.show()