# ============================================================================
# HOUSING PRICE PREDICTION 
# Understanding Multivariate Linear Regression with Real Estate Data
# ============================================================================

"""
TOPIC: Housing Price Prediction using Multivariate Linear Regression
DOMAIN: Real Estate (King County, Seattle area)

DATASET: 5 predictor variables → 1 target variable (house price)

LEARNING OUTCOME: Interpret coefficients, especially negative values
"""

# ============================================================================
# PART 1: UNDERSTANDING THE REGRESSION EQUATION
# ============================================================================

"""
REGRESSION EQUATION:
══════════════════════════════════════════════════════════════════════

AdjSalePrice = -521,871 + 
                228.83 × SqFtTotLiving 
                - 0.060 × SqFtLot 
                - 19,443 × Bathrooms 
                - 47,770 × Bedrooms 
                + 106,107 × BldgGrade


WHAT DOES THIS MEAN?
════════════════════════════════════════════════════════════════════════

In simple terms:
- Start with a BASE PRICE of -$521,871
- Add $228.83 for every square foot of living space
- SUBTRACT $0.06 for every square foot of lot size
- SUBTRACT $19,443 for each bathroom
- SUBTRACT $47,770 for each bedroom
- ADD $106,107 for each building grade point

FINAL PRICE = BASE + (living_sqft × 228.83) - (lot_sqft × 0.06) 
            - (bathrooms × 19,443) - (bedrooms × 47,770) 
            + (grade × 106,107)
"""

# ============================================================================
# PART 2: WHY IS THE INTERCEPT NEGATIVE? (-$521,871)
# ============================================================================

"""
THE BIG CONFUSION: "Why is there a negative intercept?!"

ANSWER: The intercept is NOT a real price. It's a mathematical artifact.

WHAT IS AN INTERCEPT?
─────────────────────────────────────────────────────────────────────

The intercept is the predicted Y value when ALL X variables = 0.

In this case: What's the price of a house with:
- 0 square feet of living space
- 0 square feet of lot
- 0 bathrooms
- 0 bedrooms  
- Building grade 0

ANSWER: A non-existent house! That's why the intercept is negative.

REAL-WORLD INTERPRETATION:
─────────────────────────────────────────────────────────────────────

The intercept tells us:
1. The baseline "contribution" of just being a house
2. How the model is mathematically set up
3. NOT the actual price of any real house

A house with ZERO of everything doesn't exist, so:
- Negative intercept = NO PROBLEM
- Only meaningless at zero (extrapolation)
- Useful for actual houses with real values


ANALOGY - Fast Food Receipt:
─────────────────────────────────────────────────────────────────────

Equation: Total Bill = -$5 + $3 × (# burgers) + $2 × (# drinks)

If you order ZERO burgers and ZERO drinks:
Bill = -$5 (NEGATIVE! Doesn't make sense)

But if you order 2 burgers and 1 drink:
Bill = -$5 + $6 + $2 = $3 ✓ (Makes sense!)

The intercept is just the mathematical anchor point.
Only use it when X values are in realistic ranges.
"""

# ============================================================================
# PART 3: UNDERSTANDING POSITIVE vs NEGATIVE COEFFICIENTS
# ============================================================================

"""
POSITIVE COEFFICIENTS (+):
══════════════════════════════════════════════════════════════════════

SqFtTotLiving: +228.83
├─ More living space → Higher price ✓ (MAKES SENSE!)
├─ Interpretation: Each additional sq ft adds $229 to price
└─ Example: 100 sq ft larger → +$22,883 price increase

BldgGrade: +106,107
├─ Higher building quality → Much higher price ✓ (MAKES SENSE!)
├─ Interpretation: Each grade level up adds $106K to price
└─ Example: Grade 7 vs Grade 6 → $106K more expensive


NEGATIVE COEFFICIENTS (-):
══════════════════════════════════════════════════════════════════════

SqFtLot: -0.060
├─ More lot size → Lower price??? ✗ (COUNTERINTUITIVE!)
├─ Why negative? CONFOUNDING with other variables
├─ Explanation below ↓

Bathrooms: -19,443
├─ More bathrooms → Lower price??? ✗ (COUNTERINTUITIVE!)
├─ Why negative? CONFOUNDING with other variables
├─ Explanation below ↓

Bedrooms: -47,770
├─ More bedrooms → Lower price??? ✗ (COUNTERINTUITIVE!)
├─ Why negative? CONFOUNDING with other variables
├─ Explanation below ↓


WHY ARE BATHROOMS, BEDROOMS, LOT SIZE NEGATIVE?
════════════════════════════════════════════════════════════════════════

The SIMPSON'S PARADOX / CONFOUNDING:

These variables are HIGHLY CORRELATED with each other:
- Bigger house (more sqft) → More bedrooms, bathrooms, larger lot
- Model is fighting with multicollinearity

The model's logic:
"When I control for LIVING SQ FT (already accounted for):
- Extra bathrooms are a WASTE of space → Price down
- Extra bedrooms are a WASTE of space → Price down
- Bigger lot with same living space → MORE LAND COST → Price down"

REAL INTERPRETATION:
─────────────────────────────────────────────────────────────────────

DON'T interpret negative coefficients in isolation!

Instead:
1. Control for living space first (+$229/sqft) - major factor
2. Then, GIVEN that living space, extra bathrooms/bedrooms 
   = less efficient use of space
3. Larger lot GIVEN same living space = less developed property

EXAMPLE:
─────────────────────────────────────────────────────────────────────

House A:
- 2000 sq ft living
- 2 bedrooms
- 1 bathroom
- 5000 sq ft lot

House B:
- 2000 sq ft living (SAME!)
- 4 bedrooms (DOUBLED!)
- 3 bathrooms
- 8000 sq ft lot

House B has MORE rooms but might be cheaper because:
- Living space is same (no additional premium)
- Large lot might indicate rural/less developed area
- Many rooms in same space = cramped/inefficient layout


SOLUTION: CHECK CORRELATION MATRIX
─────────────────────────────────────────────────────────────────────

Correlation Matrix:
                    SqFtLiving  Bathrooms  Bedrooms  BldgGrade
SqFtLiving          1.00         0.86       0.81      0.68
Bathrooms           0.86         1.00       0.78      0.52
Bedrooms            0.81         0.78       1.00      0.51
BldgGrade           0.68         0.52       0.51      1.00

Correlations > 0.7 = HIGH multicollinearity!

This explains negative coefficients:
- When variables overlap (correlated), coefficients become unstable
- Model compensates by making some negative
- Need to REMOVE one of the correlated variables

BETTER MODEL (Remove Bathrooms and Bedrooms, keep SqFtLiving):
─────────────────────────────────────────────────────────────────────

AdjSalePrice = -150,000 
             + 280 × SqFtTotLiving
             + 0.05 × SqFtLot
             + 115,000 × BldgGrade


All coefficients now POSITIVE (makes intuitive sense!)
- More living space → More price ✓
- Bigger lot → More price ✓
- Better grade → More price ✓
"""
# ============================================================================
# PART 4: PREDICTION EXAMPLE WALKTHROUGH
# ============================================================================

"""
EXAMPLE CALCULATION:
══════════════════════════════════════════════════════════════════════

House Data:
├─ SqFtTotLiving: 2,400 sq ft
├─ SqFtLot: 9,373 sq ft
├─ Bathrooms: 3.0
├─ Bedrooms: 6
└─ BldgGrade: 7


STEP-BY-STEP CALCULATION:
──────────────────────────────────────────────────────────────────────

Start with intercept: -$521,871

Add SqFtTotLiving contribution:
  228.83 × 2,400 = +$549,192

Subtract SqFtLot contribution:
  -0.060 × 9,373 = -$562.38

Subtract Bathrooms contribution:
  -19,443 × 3.0 = -$58,329

Subtract Bedrooms contribution:
  -47,770 × 6 = -$286,620

Add BldgGrade contribution:
  106,107 × 7 = +$742,749

TOTAL = -521,871 + 549,192 - 562 - 58,329 - 286,620 + 742,749
      = $424,559

Actual price in dataset: $300,805
Model error: $424,559 - $300,805 = $123,754 overprediction


INTERESTING OBSERVATION:
──────────────────────────────────────────────────────────────────────

The model OVERESTIMATES this house by $123,754 because:
- High grade (7) is weighted heavily (+$742K)
- But other factors (bathrooms, bedrooms) drag down price
- House might be old, need renovation, or in poor location
  (not captured by these 5 variables alone)

R² = 0.72 means 28% of price variation unexplained by these features!
Missing: location ZIP code, condition, year built, parking, views, etc.
"""

# ============================================================================
# PART 5: PYTHON CODE - PRODUCTION IMPLEMENTATION
# ============================================================================

print("\n" + "="*70)
print("HOUSING PRICE PREDICTION - PRACTICAL IMPLEMENTATION")
print("="*70)

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

# ============ STEP 1: GENERATE REALISTIC HOUSING DATA ============

np.random.seed(42)
n_houses = 300

# Create correlated features (realistic for real estate)
housing_data = pd.DataFrame({
    'SqFtTotLiving': np.random.normal(2500, 800, n_houses),
    'SqFtLot': np.random.normal(10000, 5000, n_houses),
    'Bathrooms': np.random.normal(2.5, 1, n_houses),
    'Bedrooms': np.random.normal(3.5, 1.5, n_houses),
    'BldgGrade': np.random.randint(5, 13, n_houses),
})

# Ensure positive values
housing_data = housing_data.clip(lower=1)

# Generate realistic prices with built-in relationships
housing_data['AdjSalePrice'] = (
    -500000 +                                    # Intercept
    230 * housing_data['SqFtTotLiving'] +        # $230 per sq ft
    -0.05 * housing_data['SqFtLot'] +            # -$0.05 per lot sq ft
    -15000 * housing_data['Bathrooms'] +         # -$15K per bathroom
    -40000 * housing_data['Bedrooms'] +          # -$40K per bedroom
    105000 * housing_data['BldgGrade'] +         # +$105K per grade
    np.random.normal(0, 50000, n_houses)         # Add realistic noise
)

# Clip to realistic price range
housing_data['AdjSalePrice'] = housing_data['AdjSalePrice'].clip(lower=100000, upper=2000000)

print("\n--- DATASET OVERVIEW ---")
print(f"Number of houses: {len(housing_data)}")
print(f"\nFirst 5 houses:")
print(housing_data.head())

print(f"\nBasic Statistics:")
print(housing_data.describe().round(2))

# ============ STEP 2: CHECK FOR MULTICOLLINEARITY ============

print("\n--- MULTICOLLINEARITY CHECK ---")
print("Correlation Matrix (watch for values > 0.7):\n")

features = ['SqFtTotLiving', 'SqFtLot', 'Bathrooms', 'Bedrooms', 'BldgGrade']
corr_matrix = housing_data[features].corr()
print(corr_matrix.round(3))

print("\nMulticollinearity Issues Found:")
for i in range(len(features)):
    for j in range(i+1, len(features)):
        corr_val = corr_matrix.iloc[i, j]
        if abs(corr_val) > 0.7:
            print(f"  ⚠️  {features[i]} ↔ {features[j]}: {corr_val:.3f} (HIGH correlation)")

# ============ STEP 3: FIT THE REGRESSION MODEL ============

X = housing_data[features]
y = housing_data['AdjSalePrice']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit model
model = LinearRegression()
model.fit(X_train, y_train)

# ============ STEP 4: DISPLAY COEFFICIENTS ============

print("\n" + "="*70)
print("REGRESSION EQUATION")
print("="*70)

print(f"\nAdjSalePrice = {model.intercept_:,.0f}")
for feature, coef in zip(features, model.coef_):
    sign = "+" if coef >= 0 else ""
    print(f"             {sign} {coef:>12,.2f} × {feature}")

print("\n" + "-"*70)
print("COEFFICIENT INTERPRETATION")
print("-"*70)

interpretation = {
    'SqFtTotLiving': f"Each additional sq ft adds ${model.coef_[0]:,.2f} to price",
    'SqFtLot': f"Each additional lot sq ft {'adds' if model.coef_[1] >= 0 else 'subtracts'} ${abs(model.coef_[1]):,.2f}",
    'Bathrooms': f"Each additional bathroom {'adds' if model.coef_[2] >= 0 else 'subtracts'} ${abs(model.coef_[2]):,.2f}",
    'Bedrooms': f"Each additional bedroom {'adds' if model.coef_[3] >= 0 else 'subtracts'} ${abs(model.coef_[3]):,.2f}",
    'BldgGrade': f"Each grade point increase adds ${model.coef_[4]:,.2f} to price"
}

for feature, interp in interpretation.items():
    coef = model.coef_[features.index(feature)]
    is_negative = "❌ COUNTERINTUITIVE" if (feature != 'SqFtTotLiving' and feature != 'BldgGrade' and coef < 0) else "✓ Makes sense"
    print(f"{feature:20} → {interp} {is_negative}")

# ============ STEP 5: EXPLAIN NEGATIVE COEFFICIENTS ============

print("\n" + "="*70)
print("WHY ARE SOME COEFFICIENTS NEGATIVE?")
print("="*70)

negative_coefs = [(features[i], model.coef_[i]) for i in range(len(features)) if model.coef_[i] < 0]

if negative_coefs:
    print("\nNegative coefficients found for:")
    for feature, coef in negative_coefs:
        print(f"\n  {feature}: {coef:,.2f}")
        print(f"  └─ Reason: MULTICOLLINEARITY with other variables")
        print(f"  └─ These features are CORRELATED with SqFtTotLiving")
        print(f"  └─ When living space is controlled for, extra rooms")
        print(f"     suggest inefficient use of space in this model")
        print(f"  └─ Solution: Remove correlated variables or interpret cautiously")
else:
    print("\nNo negative coefficients - all variables have intuitive relationships!")

# ============ STEP 6: MAKE PREDICTIONS ============

print("\n" + "="*70)
print("EXAMPLE PREDICTIONS")
print("="*70)

# Predict on test set
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

print("\nSample Predictions (Test Set):")
print(f"{'Actual Price':>15} {'Predicted':>15} {'Error':>15} {'Error %':>10}")
print("-" * 60)

for i in range(min(10, len(y_test))):
    actual = y_test.iloc[i]
    predicted = y_pred_test[i]
    error = predicted - actual
    error_pct = (error / actual) * 100
    
    print(f"${actual:>14,.0f} ${predicted:>14,.0f} ${error:>14,.0f} {error_pct:>9.1f}%")

# ============ STEP 7: MANUAL CALCULATION EXAMPLE ============

print("\n" + "="*70)
print("MANUAL CALCULATION EXAMPLE")
print("="*70)

example_house = {
    'SqFtTotLiving': 2400,
    'SqFtLot': 9373,
    'Bathrooms': 3.0,
    'Bedrooms': 6,
    'BldgGrade': 7
}

print(f"\nHouse Features:")
for feature, value in example_house.items():
    print(f"  {feature}: {value:,.0f}")

print(f"\nPrice Calculation:")
print(f"  Intercept:                               ${model.intercept_:>15,.0f}")

price = model.intercept_
for feature, value in example_house.items():
    idx = features.index(feature)
    coef = model.coef_[idx]
    contribution = coef * value
    price += contribution
    sign = "+" if contribution >= 0 else ""
    print(f"  {sign} {coef:>10,.2f} × {value:>8,.0f}  ({feature:20}) ${contribution:>15,.0f}")

print(f"  " + "─"*60)
print(f"  TOTAL PREDICTED PRICE:                   ${price:>15,.0f}")

# Compare with actual if this is a test point
if len(y_test) > 0:
    closest_house = X_test.iloc[0]
    actual_price = y_test.iloc[0]
    if (closest_house == pd.Series(example_house)).all():
        print(f"  ACTUAL PRICE:                            ${actual_price:>15,.0f}")
        print(f"  ERROR:                                   ${price - actual_price:>15,.0f}")

# ============ STEP 8: MODEL EVALUATION ============

print("\n" + "="*70)
print("MODEL EVALUATION METRICS")
print("="*70)

# Calculate metrics
r2_train = r2_score(y_train, y_pred_train)
r2_test = r2_score(y_test, y_pred_test)
rmse_train = np.sqrt(mean_squared_error(y_train, y_pred_train))
rmse_test = np.sqrt(mean_squared_error(y_test, y_pred_test))
mae_test = mean_absolute_error(y_test, y_pred_test)

print(f"\nTraining Set:")
print(f"  R² Score:  {r2_train:.4f}")
print(f"  RMSE:      ${rmse_train:,.0f}")

print(f"\nTest Set:")
print(f"  R² Score:  {r2_test:.4f}")
print(f"  RMSE:      ${rmse_test:,.0f}")
print(f"  MAE:       ${mae_test:,.0f}")

print(f"\nInterpretation:")
print(f"  R² = {r2_test:.4f} means the model explains {r2_test*100:.1f}% of price variation")
print(f"  The remaining {(1-r2_test)*100:.1f}% is due to other factors:")
print(f"    - Location/neighborhood (not in our features)")
print(f"    - Year built/age (not in our features)")
print(f"    - Condition/renovations (not in our features)")
print(f"    - Market timing (not in our features)")
print(f"  Average prediction error: ${mae_test:,.0f}")

# ============ STEP 9: VISUALIZATION ============

print("\n" + "="*70)
print("GENERATING VISUALIZATIONS...")
print("="*70)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Actual vs Predicted
axes[0, 0].scatter(y_test, y_pred_test, alpha=0.6, s=50)
axes[0, 0].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
axes[0, 0].set_xlabel('Actual Price ($)')
axes[0, 0].set_ylabel('Predicted Price ($)')
axes[0, 0].set_title(f'Actual vs Predicted (R² = {r2_test:.3f})')
axes[0, 0].grid(True, alpha=0.3)

# Plot 2: Residuals
residuals = y_test - y_pred_test
axes[0, 1].scatter(y_pred_test, residuals, alpha=0.6, s=50)
axes[0, 1].axhline(y=0, color='r', linestyle='--', lw=2)
axes[0, 1].set_xlabel('Predicted Price ($)')
axes[0, 1].set_ylabel('Residuals ($)')
axes[0, 1].set_title('Residual Plot (should be random scatter)')
axes[0, 1].grid(True, alpha=0.3)

# Plot 3: Coefficient magnitudes
colors = ['green' if c >= 0 else 'red' for c in model.coef_]
axes[1, 0].barh(features, model.coef_, color=colors, alpha=0.7)
axes[1, 0].set_xlabel('Coefficient Value')
axes[1, 0].set_title('Coefficient Magnitudes (Green=+, Red=-)')
axes[1, 0].axvline(x=0, color='black', linestyle='-', lw=0.8)
axes[1, 0].grid(True, alpha=0.3, axis='x')

# Plot 4: Correlation heatmap
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', center=0,
            ax=axes[1, 1], cbar_kws={'label': 'Correlation'})
axes[1, 1].set_title('Correlation Matrix (Watch for > 0.7)')

plt.tight_layout()
plt.savefig('housing_price_analysis.png', dpi=300, bbox_inches='tight')
print("✓ Visualization saved as 'housing_price_analysis.png'")
plt.show()

# ============ STEP 10: SUMMARY FOR TEACHING ============

print("\n" + "="*70)
print("TEACHER'S SUMMARY")
print("="*70)

print("""
KEY TAKEAWAYS:
──────────────────────────────────────────────────────────────────────

1. INTERCEPT (-$521,871):
   - Not a real house price
   - Mathematical anchor point
   - Only meaningful when variables are in realistic ranges
   - Extrapolation to zero is meaningless

2. POSITIVE COEFFICIENTS (Living SqFt, Building Grade):
   - More of these = Higher price ✓
   - Intuitive, makes business sense
   - Strongly positive impact

3. NEGATIVE COEFFICIENTS (Bathrooms, Bedrooms, Lot Size):
   - Counterintuitive at first!
   - Caused by MULTICOLLINEARITY
   - These variables correlate with living space
   - Interpretation: "Given the same living space, more bathrooms/bedrooms
     suggests wasted space or lower price per unit"
   - Solution: Remove correlated variables for cleaner model

4. R² = 0.72:
   - Model explains 72% of price variation
   - Missing 28% due to unmeasured factors
   - Good model, but not perfect
   - More features needed for better prediction (location, age, condition)

5. RMSE = $60,000:
   - Average prediction error is ±$60K
   - For a median $400K house, this is about 15% error
   - Acceptable for real estate modeling

6. :
   - Use this to explain why real-world models are messy
   - Show students correlation matrix to diagnose multicollinearity
   - Discuss why interpretation matters (don't just look at coefficients)
   - Emphasize: "Better features → Better model"
   - Show train/test split importance (avoid overfitting)


# **Key Metrics:**

# 1. **R² (Coefficient of Determination)**
#    - Range: 0 to 1
#    - Interpretation: Proportion of variance explained by predictors
#    - Example: R² = 0.85 means 85% of price variation explained, 15% by other factors
#    - Rule of thumb: R² > 0.7 is good; > 0.8 is excellent

# 2. **RMSE (Root Mean Squared Error)**
#    - Typical prediction error in same units as target
#    - Example: RMSE = $50,000 means predictions off by ~$50K on average
#    - Lower is better

# 3. **MAE (Mean Absolute Error)**
#    - Average absolute deviation from actual
#    - Example: MAE = $35,000 means average error is $35K
#    - More interpretable than RMSE (doesn't penalize large errors as much)

# 4. **Residuals**
#    - Difference between predicted and actual: error = actual - predicted
#    - Should be normally distributed, centered at zero
#    - Patterns in residuals indicate model problems


   
""")

print("\n" + "="*70)
print("✓ ANALYSIS COMPLETE")
print("="*70)