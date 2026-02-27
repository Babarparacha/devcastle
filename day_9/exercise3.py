# the mean average 

import statistics
# a normal list of property prices
bedroom_requests=[3,4,3,2,3,5,3,4]

# find the most frequent 
most_popular=statistics.mode(bedroom_requests)

print(f"Most clents want a Rs:{most_popular}-bedroom house")