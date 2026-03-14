# ============================================================================
# UNIVARIATE LINEAR REGRESSION WITH GRADIENT DESCENT
# Building the Machine Learning Engine from Scratch
# ============================================================================

"""
TOPIC: Gradient Descent Algorithm
DOMAIN: Cloud Infrastructure (Hexora Cloud Solutions)

SCENARIO: 
We have 1 predictor variable (API Requests per second) 
We want to predict 1 target variable (Server CPU Load %)

LEARNING OUTCOME: Understand how the AI updates its weights iteratively
using the Cost Function and Learning Rate, without using scikit-learn.
"""

import numpy as np
import matplotlib.pyplot as plt

# ============================================================================
# PART 1: THE LABELED DATA
# ============================================================================

# X = API Requests per second (in hundreds)
# y = CPU Load Percentage (%)
X = np.array([1, 2, 3, 4, 5]) 
y = np.array([20, 41, 58, 82, 101]) 

n = len(X) # Number of data points

# ============================================================================
# PART 2: INITIALIZING THE COMPONENTS
# ============================================================================

# 1. The Starting Weights (The AI starts completely blind!)
m = 0.0  # Weight (Slope)
b = 0.0  # Intercept (Base load)

# 2. The Optimizer Settings
learning_rate = 0.01  # How big of a step we take down the mountain
epochs = 500          # How many times we repeat the guessing process

print("\n" + "="*70)
print("Starting GRADIENT DESCENT OPTIMIZER...")
print("="*70)

# ============================================================================
# PART 3: THE GRADIENT DESCENT LOOP (THIS IS WHAT .fit() ACTUALLY DOES)
# ============================================================================

for i in range(epochs):
    
    # STEP 1: THE HYPOTHESIS (Make a prediction using current weights)
    # Equation: y = mx + b
    y_predicted = (m * X) + b
    
    # STEP 2: THE COST FUNCTION (How wrong were we?)
    # We calculate the error (Difference between our guess and reality)
    error = y_predicted - y
    cost = (1/n) * sum(error**2) # Mean Squared Error (MSE)
    
    # STEP 3: THE CALCULUS (Find the slope of the mountain)
    # Derivative with respect to 'm'
    m_derivative = (2/n) * sum(X * error)
    # Derivative with respect to 'b'
    b_derivative = (2/n) * sum(error)
    
    # STEP 4: THE OPTIMIZER UPDATE (Take a step down the mountain)
    # We subtract the slope to move toward the minimum error
    m = m - (learning_rate * m_derivative)
    b = b - (learning_rate * b_derivative)
    
    # Print the dashboard every 100 epochs to watch the AI learn
    if i % 100 == 0:
        print(f"Epoch {i:>3} | Cost (Error): {cost:>8.2f} | Weight (m): {m:>5.2f} | Intercept (b): {b:>5.2f}")

print("\n" + "="*70)
print("TRAINING COMPLETE:")
print("="*70)
print(f"Final CPU Load Equation: CPU% = ({m:.2f} × API Requests) + {b:.2f}")

# ============================================================================
# PART 4: REAL-WORLD TESTING
# ============================================================================

print("\n" + "-"*70)
print("TESTING THE CUSTOM ENGINE")
print("-"*70)

# A massive spike hits our cloud servers: 800 API requests per second (X=8)
new_api_spike = 2.5
predicted_cpu = (m * new_api_spike) + b

print(f"Traffic Spike Detected: {new_api_spike}00 Requests/sec")
print(f"AI Predicted CPU Load:  {predicted_cpu:.1f}%")

if predicted_cpu > 90:
    print("SYSTEM ALERT: Auto-scaling to secondary node.")

# ============================================================================
# PART 5: VISUALIZATION
# ============================================================================

plt.figure(figsize=(8, 5))

# Plot the real historical server logs
plt.scatter(X, y, color='red', s=100, label='Actual Server Logs')

# Plot the line our custom math figured out
regression_line = (m * X) + b
plt.plot(X, regression_line, color='blue', linewidth=3, label=f'Our AI: y = {m:.1f}x + {b:.1f}')

plt.title('Hexora Cloud: API Requests vs CPU Load', fontsize=14, fontweight='bold')
plt.xlabel('API Requests (in hundreds)', fontsize=12)
plt.ylabel('Server CPU Load (%)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# ============================================================================
# TEACHER'S SUMMARY FOR THE CLASS
# ============================================================================
"""
What just happened here? 
1. The AI started at m=0 and b=0. Its first guess was a flat line (terrible).
2. The Cost Function screamed: "Your error is massive!"
3. Gradient Descent calculated the derivatives to find out which direction 
   to tweak 'm' and 'b'.
4. It repeated this loop 500 times, tweaking the line millimeter by millimeter, 
   until the Cost hit rock bottom and the line perfectly fit the data.

You just built an AI engine from raw scratch using pure Calculus and Algebra.
"""