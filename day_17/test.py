import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# set theme
sns.set_theme(style="darkgrid")

# create sample data
data = {
    "Days": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun","anothedDay"],
    "Sales": [200, 300, 250, 400, 300, 500,250,600]
}

df = pd.DataFrame(data)
# print(df)
# create chart
sns.lineplot(x="Days", y="Sales", data=df, marker="o")

# chart title and labels
plt.title("Weekly Sales Chart")
plt.xlabel("Days")
plt.ylabel("Sales")

# show chart
plt.show()
