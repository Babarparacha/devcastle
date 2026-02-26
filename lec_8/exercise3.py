from abc import ABC,abstractmethod

class AIMOdel(ABC):
    @abstractmethod
    def preprocess(self,data):
        pass
    @abstractmethod
    def train(self,data):
        pass
class MyModel(AIMOdel):
    pass
model=MyModel()
print(model)