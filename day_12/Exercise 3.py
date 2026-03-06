# THE SCENARIO: 
# Historically, only 5% of the population are active Tax Evaders (P_Evader).
# When someone IS an evader, we know 60% of them buy Mansions to hide cash (P_Mansion_given_Evader).
# However, honest rich people buy Mansions too! 10% of ALL citizens buy Mansions (P_Mansion_Total).

# 1. The Historical Setup
P_Evader = 0.05 
P_Mansion_given_Evader = 0.60 
P_Mansion_Total = 0.10 

# 2. Bayes Theorem (The AI updates its brain with the new evidence)
# Formula: P(Evader | Mansion) = (P(Mansion | Evader) * P(Evader)) / P(Mansion_Total)
P_Evader_given_Mansion = (P_Mansion_given_Evader * P_Evader) / P_Mansion_Total

print("🚨 SYSTEM ALERT: Citizen just purchased a Sector G Mansion!")
print(f"Old baseline probability of tax evasion: {P_Evader * 100}%")
print(f"NEW Bayesian probability of tax evasion: {P_Evader_given_Mansion * 100:.1f}%")

# Output: NEW Bayesian probability of tax evasion: 30.0%