class Add:
    def calculate(self,a,b):
        return a+b 
class Multiply:
    def calculate(self,a,b):
        return a*b 
class mathOperation(Add,Multiply):
    pass

obj=mathOperation()
print(obj.calculate(4,5))
print(mathOperation.__mro__)

        