import plotly.express as px
import pandas as pd

# The Expanded FBR Audit Data (Now with 4 Variables!)
audit_data = pd.DataFrame({
    "Declared_Income": [5, 8, 12, 15, 20, 50, 10],      # X-Axis (Lakhs)
    "Luxury_Cars": [0, 1, 1, 2, 2, 5, 4],               # Y-Axis (Count)
    "Unpaid_Taxes": [0.1, 0.5, 1, 0.1, 2, 0.1, 15],     # 3rd Variable -> Size of the dot
    "Risk_Level": ["Safe", "Safe", "Safe", "Safe", "Monitor", "Safe", "CRITICAL FRAUD"] # 4th Variable -> Color
})

# MULTIVARIATE PLOT: X vs Y vs Size vs Color
fig = px.scatter(
    audit_data, 
    x="Declared_Income", 
    y="Luxury_Cars",
    size="Unpaid_Taxes",     # The 3rd Dimension (Bubble Size)
    color="Risk_Level",      # The 4th Dimension (Bubble Color)
    title="FBR Multivariate Audit: Income vs Cars vs Unpaid Taxes",
    template="plotly_dark",
    size_max=50              # Makes the fraudster's bubble massively huge!
)

# Hovering over the giant red bubble will show all 4 stats at once!
fig.show()