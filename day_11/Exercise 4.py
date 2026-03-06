# FBR Database for a specific commercial sector
total_businesses_audited = 150
businesses_fined_for_fraud = 120

# Calculating the raw probability
fraud_probability = businesses_fined_for_fraud / total_businesses_audited

# Converting to a readable percentage for the dashboardprint
print(fraud_probability)
print(f"Probability of a business committing fraud in this sector: {fraud_probability * 100:.1f}%")
