import numpy

# W3Schools Array: Ages of people living on a specific street
ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]

# What is the 75th percentile? 
age_75 = numpy.percentile(ages, 75)

print(f"75% of the people on this street are younger than: {age_75}")


