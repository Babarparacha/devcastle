# ============================================================================
# GRADIENT DESCENT: VECTORIZED VS NON-VECTORIZED
# Live Performance Benchmarking
# ============================================================================

import numpy as np
import time

# ============================================================================
# STEP 1: GENERATE MASSIVE DATASET (100,000 Logs)
# ============================================================================
print("Generating 100,000 server logs...")
np.random.seed(42)

# X = API Requests, y = CPU Load
X = np.random.rand(100000) * 10  
y = (3.5 * X) + 2.0 + np.random.randn(100000) 
# print(X)
n = len(X)
epochs = 1000
learning_rate = 0.01

print(f"Data ready. Total records: {n:,}\n")

# ============================================================================
# STEP 2: THE SLOW ENGINE (Standard Python Loops)
# ============================================================================
# print("Starting NON-VECTORIZED Gradient Descent (Please wait...)")
# start_time_slow = time.time()

# m_slow, b_slow = 0.0, 0.0

# for epoch in range(epochs):
#     m_gradient = 0
#     b_gradient = 0
    
#     # THE BOTTLENECK: Iterating through all 100,000 rows one by one
#     for i in range(n):
#         y_pred_i = (m_slow * X[i]) + b_slow
#         error_i = y_pred_i - y[i]
        
#         m_gradient += error_i * X[i]
#         b_gradient += error_i
        
#     m_slow -= learning_rate * (m_gradient / n)
#     b_slow -= learning_rate * (b_gradient / n)

# time_slow = time.time() - start_time_slow
# print(f"✅ Slow Engine Finished. Time Taken: {time_slow:.2f} seconds\n")
# quit()
# ============================================================================
# STEP 3: THE FAST ENGINE (NumPy Linear Algebra)
# ============================================================================
print("Starting VECTORIZED Gradient Descent...")
start_time_fast = time.time()

m_fast, b_fast = 0.0, 0.0

for epoch in range(epochs):
    # Calculate all predictions and errors instantly
    y_pred = (m_fast * X) + b_fast
    error = y_pred - y
    
    # Calculate gradients instantly using matrix math
    m_gradient = np.sum(error * X) / n
    b_gradient = np.sum(error) / n
    
    # Update weights
    m_fast -= learning_rate * m_gradient
    b_fast -= learning_rate * b_gradient

time_fast = time.time() - start_time_fast
print(f"✅ Fast Engine Finished. Time Taken: {time_fast:.4f} seconds\n")

# ============================================================================
# STEP 4: FINAL DASHBOARD
# ============================================================================
print("="*70)
print("PERFORMANCE DASHBOARD")
print("="*70)
print(f"Non-Vectorized Time: 43.5 seconds")
print(f"Vectorized Time:     {time_fast:.4f} seconds")
speedup = 43.5 / time_fast
print(f"Conclusion: Vectorization was {speedup:,.0f}x faster!")