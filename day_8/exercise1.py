# polymorphism ,compute average differently
class Average:
    def compute(self,numbers):
        return sum(numbers)/len(numbers)
class WeightAdverge:
    def compute(self,numbers):
        return (sum(numbers[:-1])+numbers[-1]*2)/(len(numbers)+1)
score=[80,90,70]
methods=[Average(),WeightAdverge()]
for method in methods:
    print(f"{type(method).__name__}:{method.compute(score)}")         