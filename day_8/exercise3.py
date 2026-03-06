from abc import ABC,abstractmethod

class AIModel(ABC):
    @abstractmethod
    def preprocess(self,data):
        pass
    @abstractmethod
    def train(self,data):
        pass
class MyModel(AIModel):
     def preprocess(self,data):
        return data**2
     def train(self,data):
        return data+4
model=MyModel()
print(model.preprocess(7))
print(model.train(7))