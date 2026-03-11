class MyDataset:
    def __init__(self, data):
        self.data = data  # just a list of numbers

    # Overloading the '+' operator
    def __add__(self, other):
        # When you add two datasets, we merge their numbers
        return MyDataset(self.data + other.data)

    # Overloading the print() output
    def __str__(self):
        return f"Dataset: {self.data}"

# Two simple datasets
d1 = MyDataset([10, 20, 30])
d2 = MyDataset([5, 15, 25])

# Merge using '+'
merged = d1 + d2

print(d1)       
print(d2)       
print(merged)   


