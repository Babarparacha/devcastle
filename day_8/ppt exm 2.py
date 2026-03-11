from abc import ABC, abstractmethod

class AIModel(ABC):

    @abstractmethod
    def preprocess(self, data):
        pass

    @abstractmethod
    def train(self, data):
        pass


class MyModel(AIModel):
    pass

model = MyModel()   


















# class NeuralNetwork(AIModel):

#     def preprocess(self, data):
#         print("Normalizing and encoding data")

#     def train(self, data):
#         print("Training using backpropagation")


# model = NeuralNetwork()
# model.train("dataset")