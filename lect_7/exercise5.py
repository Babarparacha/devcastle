class Engine:
    def __init__(self,horsepower):
        self.horsepower=horsepower
    def start(self):
        print("engine with",self.horsepower,"hp started!")
class Car:
    def __init__(self,horsepower):
        #engine created inside car
        self.engine=Engine(horsepower)

    def start_car(self):
        self.engine.start()
# car1=Car(150)
# car1.start_car()

# 2ND EXAMPLE
class Doctor:
    def heal(self,patient):
        print("doctor is treating",patient.name)
class Patient:
    def __init__(self,name):
        self.name=name
d1=Doctor()
p1=Patient("babar")
d1.heal(p1)