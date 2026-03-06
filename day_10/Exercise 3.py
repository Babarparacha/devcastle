import numpy

class NationalTaxAuditor:
    def __init__(self, region_name, income_data):
        self.region = region_name
        self.incomes = income_data
        
        # Using Numpy to find the Baseline and the Spread
        self.mean_income = numpy.mean(self.incomes) 
        self.sd_income = numpy.std(self.incomes)#Standard deviation is a measure of the amount of variation or dispersion of a set of values.
       

    def audit_citizen(self, citizen_name, declared_income):
        print(f"\n---FBR Audit: {citizen_name} in {self.region} ---")
        
        # Calculate the Z-Score! 
        z_score = (declared_income - self.mean_income) / self.sd_income
        
        print(f"Calculated Z-Score: {z_score:.2f}")
        
        # AI Business Logic for Fraud Detection
        if z_score < -2.0:
            print("FRAUD ALERT: Declared income is mathematically impossible. Audit triggered!")
        elif z_score > 2.0:
            print("High Net Worth Individual: Apply Luxury Tax Bracket.")
        else:
            print("Approved: Income matches regional data spread.")

# ==========================================
# EXECUTION: RUNNING THE PIPELINE
# ==========================================
# Regional Incomes in Lakhs
regional_incomes = [12, 14, 15, 13, 16, 14, 15, 12, 14]

auditor = NationalTaxAuditor("Punjab Zone A", regional_incomes)

# Citizen 1 declares a normal income of 15 Lakhs
auditor.audit_citizen("Ali", 15)

# Citizen 2 tries to hide wealth and declares only 2 Lakhs!
auditor.audit_citizen("Waleed", 2)