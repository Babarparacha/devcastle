numbers = [1, 2, 3, 4, 5, 6]

# Map: Squaring every number in the list
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Mapped (Squared):", squared_numbers)

# Filter: Extracting only numbers greater than 3
filtered_numbers = list(filter(lambda x: x > 3, numbers))
print("Filtered (Greater than 3):", filtered_numbers)


