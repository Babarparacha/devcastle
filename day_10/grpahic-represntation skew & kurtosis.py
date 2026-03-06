import plotly.express as px
import random
import numpy as np
import pandas as pd
from scipy.stats import skew, kurtosis

# ==========================================
# 1. GENERATE THE MOCK CENSUS DATA
# ==========================================
# We create 1000 normal citizens (average wealth 8 Lakhs)
normal_citizens = np.random.normal(loc=8, scale=2, size=1000)

# We create 50 extreme billionaires (average wealth 80 Lakhs) to ruin the curve
billionaires = np.random.normal(loc=80, scale=10, size=50)

# Combine them into one national database
national_wealth = np.concatenate([normal_citizens, billionaires])
print(national_wealth)
# Convert to a Pandas DataFrame (Plotly loves DataFrames)
df = pd.DataFrame({'Wealth (in Lakhs)': national_wealth})

# ==========================================
# 2. CALCULATE THE STATS FOR THE TITLE
# ==========================================
data_skew = skew(national_wealth)
data_kurt = kurtosis(national_wealth)
chart_title = f"National Wealth Distribution<br><sup>Right Skewness: {data_skew:.2f} | Kurtosis (Fat Tails): {data_kurt:.2f}</sup>"

# ==========================================
# 3. RENDER THE PLOTLY INTERACTIVE GRAPH
# ==========================================
fig = px.histogram(
    df, 
    x='Wealth (in Lakhs)', 
    nbins=60, 
    title=chart_title,
    marginal='box', # THIS IS THE MAGIC! It adds a box plot on top showing the exact outliers.
    color_discrete_sequence=['#1f77b4'],
    opacity=0.8
)

# Make it look like a professional dashboard
fig.update_layout(
    xaxis_title="Property Value (in Lakhs)",
    yaxis_title="Number of Citizens",
    template="plotly_dark" # Looks badass on a projector
)

# Pop the graph open in their browser!
fig.show()