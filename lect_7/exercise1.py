class Dog:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def bark(self):
        print(self.name,"bark")
my_dog=Dog("max","brown")
my_dog.bark()
        