# ============================================================================
# LOGISTIC REGRESSION: BINARY CLASSIFICATION (SPAM DETECTION)
# Building the Sigmoid Engine from Scratch (Vectorized)
# ============================================================================

import numpy as np

# ============================================================================
# STEP 1: THE SIGMOID FUNCTION (Slides 4, 5, & 6)
# ============================================================================
# This is the "Squasher". It forces any number to live strictly between 0 and 1.

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# ============================================================================
# STEP 2: GENERATE THE SPAM DATASET (Slide 9)
# ============================================================================
print("Generating 2,000 synthetic emails (1,000 Legitimate, 1,000 Spam)...")
np.random.seed(42)
n_samples = 1000

# Feature 1: Links | Feature 2: Sender Reputation (0-10) | Feature 3: Spam Keywords
# Legitimate Emails (Class 0): Few links, high reputation, few keywords
legit_links = np.random.normal(2, 1, n_samples)
legit_reputation = np.random.normal(8, 1.5, n_samples)
legit_keywords = np.random.normal(1, 1, n_samples)
legit_labels = np.zeros(n_samples) # 0 = Legitimate


# Spam Emails (Class 1): Many links, low reputation, lots of keywords
spam_links = np.random.normal(8, 2, n_samples)
spam_reputation = np.random.normal(2, 1.5, n_samples)
spam_keywords = np.random.normal(7, 2, n_samples)
spam_labels = np.ones(n_samples) # 1 = Spam

# Stack them into a matrix (2000 rows, 3 columns)
X = np.vstack((
    np.column_stack((legit_links, legit_reputation, legit_keywords)),
    np.column_stack((spam_links, spam_reputation, spam_keywords))
))
y = np.concatenate((legit_labels, spam_labels))
n = len(y)

# ============================================================================
# STEP 3: GRADIENT DESCENT ENGINE (Slides 7 & 8)
# ============================================================================
print("\nBooting up Vectorized Gradient Descent...")

# Initialize weights (m) for our 3 features, and 1 bias (b)
weights = np.zeros(3) 
bias = 0.0

learning_rate = 0.05
epochs = 1000

for i in range(epochs):
    
    # 1. The Linear Part (z = m*x + b)
    # X is (2000x3), weights is (3,). Dot product gives us 2000 linear predictions.
    z = np.dot(X, weights) + bias
    
    # 2. The Sigmoid Activation (Turn z into probabilities between 0 and 1)
    probabilities = sigmoid(z)
    
    # 3. The Cost Function (Binary Cross-Entropy from Slide 9)
    # We add a tiny number (1e-9) to prevent log(0) which crashes the math...
    cost = -(1/n) * np.sum(y * np.log(probabilities + 1e-9) + (1-y) * np.log(1 - probabilities + 1e-9))
    
    # 4. Calculate Gradients (Vectorized!)
    # X.T flips the matrix so the puzzle pieces fit for multiplication
    dw = (1/n) * np.dot(X.T, (probabilities - y))
    db = (1/n) * np.sum(probabilities - y)
    
    # 5. Update Weights
    weights -= learning_rate * dw
    bias -= learning_rate * db
    
    if i % 100 == 0 or i == epochs - 1:
        print(f"Epoch {i:>4} | Binary Cross-Entropy Cost: {cost:.4f}")

print("\n" + "="*70)
print("TRAINING COMPLETE: THE AI'S LOGIC")
print("="*70)
print(f"Weight (Links):      {weights[0]:>6.2f}")
print(f"Weight (Reputation): {weights[1]:>6.2f} (Negative because high rep = NOT spam!)")
print(f"Weight (Keywords):   {weights[2]:>6.2f}")
print(f"Bias (Base):         {bias:>6.2f}")
quit()
# ============================================================================
# STEP 4: REAL-WORLD TESTING & THRESHOLDING (Slide 6 & 9)
# ============================================================================
print("\n" + "="*70)
print("TESTING A NEW INCOMING EMAIL")
print("="*70)

# A new email arrives with: 7 Links, 1.5 Reputation Score, 8 Spam Keywords
new_email = np.array([7, 1.5, 8])

# Step 1: Calculate Linear z
linear_z = np.dot(new_email, weights) + bias

# Step 2: Squash with Sigmoid
spam_probability = sigmoid(linear_z)

print(f"Email Data: 7 Links | 1.5 Reputation | 8 Spam Keywords")
print(f"Raw Math (z)       : {linear_z:.2f}")
print(f"Sigmoid Probability: {spam_probability * 100:.2f}%")

# Step 3: Apply Threshold (0.5)
if spam_probability >= 0.5:
    print("Final Decision     : 🚨 [CLASS 1] SPAM DETECTED. Sending to Junk folder.")
else:
    print("Final Decision     : ✅ [CLASS 0] LEGITIMATE. Sending to Inbox.")





    # ============================================================================
# STEP 5: VISUALIZING THE S-CURVE (Slide 5)
# ============================================================================
import matplotlib.pyplot as plt

print("\nGenerating the Sigmoid S-Curve Graph...")

# 1. Calculate the 'z' value for every single email in our 2000-email dataset
all_z = np.dot(X, weights) + bias

# 2. Sort the data from lowest z to highest z so our line draws smoothly
sort_indices = np.argsort(all_z)
z_sorted = all_z[sort_indices]
probs_sorted = sigmoid(z_sorted)
y_sorted = y[sort_indices]

plt.figure(figsize=(10, 6))

# 3. Plot the raw data points (True 0s and True 1s)
# Legitimate emails (True 0)
plt.scatter(z_sorted[y_sorted == 0], y_sorted[y_sorted == 0], 
            color='green', alpha=0.3, label='Actual Legitimate [0]')

# Spam emails (True 1)
plt.scatter(z_sorted[y_sorted == 1], y_sorted[y_sorted == 1], 
            color='red', alpha=0.3, label='Actual Spam [1]')

# 4. Draw the AI's Sigmoid S-Curve on top!
plt.plot(z_sorted, probs_sorted, color='blue', linewidth=3, 
         label='AI Sigmoid Prediction')

# 5. Draw the Decision Boundary Threshold (Slide 6)
plt.axhline(y=0.5, color='black', linestyle='--', linewidth=1.5, 
            label='Decision Boundary (0.5)')
plt.axvline(x=0.0, color='gray', linestyle=':', linewidth=1)

# Format the graph for the projector
plt.title('Spam Detection: The Sigmoid S-Curve in Action', fontsize=16, fontweight='bold')
plt.xlabel('Linear Output (z = mx + b)', fontsize=12)
plt.ylabel('AI Predicted Probability', fontsize=12)
plt.yticks([0.0, 0.25, 0.5, 0.75, 1.0])
plt.legend(loc='upper left', fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Show the graph to the class!
plt.show()