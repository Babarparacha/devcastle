class Dog:
    speicies="canine"
    legs=4
    def __init__(self,name):
        self.name=name
        print(self.name,"has been barking")
    def __del__(self):
        print(self.name,"has been removed from memory")
my_dog=Dog("max")
print("species",my_dog.speicies)
        