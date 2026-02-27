# the mean average 

import statistics
# a normal list of property prices
prices=[150000,160000,145000,155000]

# the python library doea the heavy lifting 
market_mean=statistics.mean(prices)

print(f"the average price is Rs:{market_mean}")