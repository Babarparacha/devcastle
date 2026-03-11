# Polymorphism - compute average differently
class Average:
    def compute(self, numbers):
        return sum(numbers) / len(numbers)

class WeightedAverage:
    def compute(self, numbers):
        # give last number double weight
        return (sum(numbers[:-1]) + numbers[-1]*2) / (len(numbers)+1)

scores = [80, 90, 70]
methods = [Average(), WeightedAverage()]

for method in methods:
    print(f"{type(method).__name__}: {method.compute(scores)}")


    