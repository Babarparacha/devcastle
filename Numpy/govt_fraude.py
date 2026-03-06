import pandas as pd
import matplotlib.pyplot as plt

# =========================
# MODEL CLASSES
# =========================

class Citizen:
    def __init__(self, cnic, declared_income, bank_inflow,
                 property_value, vehicle_value,
                 luxury_spending, travel_cost):
        self.cnic = cnic
        self.declared_income = declared_income
        self.bank_inflow = bank_inflow
        self.property_value = property_value
        self.vehicle_value = vehicle_value
        self.luxury_spending = luxury_spending
        self.travel_cost = travel_cost


class RiskCalculator:
    def calculate(self, citizen):
        return (
            0.30 * citizen.bank_inflow +
            0.25 * citizen.property_value +
            0.20 * citizen.luxury_spending +
            0.15 * citizen.travel_cost +
            0.10 * citizen.vehicle_value
        )


class FraudDetector:
    def __init__(self, threshold=15_000_000):
        self.threshold = threshold

    def is_fraud(self, citizen, risk_score):
        if citizen.bank_inflow > 2 * citizen.declared_income:
            return True
        if risk_score > self.threshold:
            return True
        return False


class TaxCalculator:
    def calculate_tax(self, income):
        if income <= 1_200_000:
            return 0
        elif income <= 5_000_000:
            return income * 0.10
        else:
            return income * 0.20


class TaxEvasionSystem:
    def __init__(self):
        self.risk_calculator = RiskCalculator()
        self.detector = FraudDetector()
        self.tax_calculator = TaxCalculator()

    def process(self, citizen):
        risk = self.risk_calculator.calculate(citizen)
        fraud = self.detector.is_fraud(citizen, risk)

        actual_income = citizen.bank_inflow
        tax_due = self.tax_calculator.calculate_tax(actual_income) if fraud else 0

        return {
            "CNIC": citizen.cnic,
            "Declared Income": citizen.declared_income,
            "Bank Inflow": citizen.bank_inflow,
            "Risk Score": round(risk, 2),
            "Suspected": fraud,
            "Tax Due": round(tax_due, 2)
        }


# =========================
# SAMPLE DATA
# =========================

citizens = [
    Citizen("12345", 1_200_000, 6_000_000, 40_000_000, 10_000_000, 1_500_000, 900_000),
    Citizen("67890", 2_500_000, 2_800_000, 8_000_000, 3_000_000, 200_000, 100_000),
    Citizen("54321", 900_000, 5_000_000, 30_000_000, 7_000_000, 1_200_000, 800_000)
]

system = TaxEvasionSystem()

results = []
for c in citizens:
    results.append(system.process(c))

df = pd.DataFrame(results)
print(df)

# =========================
# SYSTEM FLOW DIAGRAM
# =========================

plt.figure(figsize=(10, 6))

boxes = [
    (0.1, 0.7, "Citizen Data"),
    (0.4, 0.7, "Risk Calculator"),
    (0.7, 0.7, "Fraud Detector"),
    (0.4, 0.4, "Tax Calculator"),
    (0.7, 0.4, "Pay Tax / Exit")
]

for x, y, text in boxes:
    plt.text(x, y, text, fontsize=11,
             bbox=dict(boxstyle="round,pad=0.4"))

arrows = [
    ((0.22, 0.72), (0.38, 0.72)),
    ((0.52, 0.72), (0.68, 0.72)),
    ((0.72, 0.68), (0.72, 0.45)),
    ((0.52, 0.42), (0.68, 0.42))
]

for start, end in arrows:
    plt.arrow(start[0], start[1],
              end[0] - start[0],
              end[1] - start[1],
              length_includes_head=True,
              head_width=0.01)

plt.title("OOP-Based Tax Evasion Detection System")
plt.axis("off")
plt.show() #not work in vscode 

# %matplotlib inline  #this works in jupyter notebook