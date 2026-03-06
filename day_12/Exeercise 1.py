# ==========================================
# BAYESIAN PROBABILITY: THE FBR RISK ENGINE
# ==========================================

# STEP 1: Define the "Prior" (Our baseline belief before any evidence)
# Historically, only 5% of the total population are active Tax Evaders.
# If we know nothing else about a person, their risk is 5%.
p_evader = 0.05 

# STEP 2: Define the "Likelihood" (How criminals behave)
# When we look ONLY at confirmed Tax Evaders, we know 60% of them 
# buy massive Mansions to launder their money. 
p_mansion_given_evader = 0.60 

# STEP 3: Define the "Marginal Likelihood" (The total evidence)
# We can't just arrest everyone with a mansion. Honest business owners 
# buy mansions too! In our total database, 10% of ALL citizens buy mansions.
p_mansion_total = 0.10 

# ==========================================
# THE TRIGGER: NEW EVIDENCE ARRIVES
# ==========================================
print("SYSTEM ALERT: Citizen just purchased a Sector G Mansion!")
print(f"Old baseline probability of tax evasion: {p_evader * 100}%")

# STEP 4: Apply Bayes' Theorem
# Formula: P(A|B) = [ P(B|A) * P(A) ] / P(B)
# In code: (Likelihood * Prior) / Total Evidence
p_evader_given_mansion = (p_mansion_given_evader * p_evader) / p_mansion_total

# The AI has successfully updated its belief based on the new data!
print(f"NEW Bayesian probability of tax evasion: {p_evader_given_mansion * 100:.1f}%")
# Output: NEW Bayesian probability of tax evasion: 30.0%