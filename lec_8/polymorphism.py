class Model:
    def train(self):
        print("training using basic method")
class NeuralNetwork(Model):
    def train(self):
        print("training using backpropagation")
class LinearRegression(Model):
    def train(self):
        print("training using least  square")

model=[NeuralNetwork(),LinearRegression()]
# print(type(model[0]))
for m in model:
    m.train()