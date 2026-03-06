import numpy

# Example 1: Safe Highway (Everyone drives similar speeds)
safe_speeds = [86, 87, 88, 86, 87, 85, 86]
safe_sd = numpy.std(safe_speeds)
print(f"Safe Highway SD: {safe_sd:.2f}") 
# Output: 0.90 (Very tight spread!)

# Example 2: Dangerous Highway (Wildly different speeds)
danger_speeds = [32, 111, 138, 28, 59, 77, 97]
danger_sd = numpy.std(danger_speeds)
print(f"Dangerous Highway SD: {danger_sd:.2f}") 
# Output: 37.85 (Massive spread, high danger!)




