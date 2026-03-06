import plotly.express as px
import pandas as pd

# The 3D FBR Audit Data
audit_data = pd.DataFrame({
    "Declared_Income": [5, 8, 12, 15, 20, 50, 10],   # X-Axis
    "Luxury_Cars": [0, 1, 1, 2, 2, 5, 4],            # Y-Axis
    "Properties_Owned": [1, 1, 1, 2, 2, 4, 10],      # Z-Axis (The 3rd physical dimension)
    "Risk_Level": ["Safe", "Safe", "Safe", "Safe", "Monitor", "Safe", "CRITICAL FRAUD"]
})

# 3D MULTIVARIATE PLOT: X vs Y vs Z
fig = px.scatter_3d(
    audit_data, 
    x="Declared_Income", 
    y="Luxury_Cars",
    z="Properties_Owned",    # Adding the Z-Axis makes it a 3D cube!
    color="Risk_Level",
    title="3D AI Audit Hologram",
    template="plotly_dark"
)

# Spin it around with your mouse!
fig.show()