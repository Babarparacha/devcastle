# the mean average 

import statistics
neighbour_prices=[100000,100000,100000,100000,100000,50000000]

# this mean ruined by the mansion
bad_average=statistics.mean(neighbour_prices)

print(f"mean lying to us Rs:{bad_average}")
#the meadidn points to the true middle of the market
true_middle=statistics.median(neighbour_prices)

print(f"median(the Truth ) Rs:{true_middle}")