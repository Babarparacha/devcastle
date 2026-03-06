class Dog:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def bark(self):
        print(self.name,"bark")
    def add(self,a,b):
        return a+b
my_dog=Dog("max","brown")
my_dog.bark()
print(my_dog.add(5,10))
        