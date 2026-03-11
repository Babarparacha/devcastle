class Model:
    def train(self):
        print("Training using basic method")

class NeuralNetwork(Model):
    def train(self):
        print("Training using backpropagation")

class LinearRegression(Model):
    def train(self):
        print("Training using least squares")

models = [NeuralNetwork(), LinearRegression()]
# print(type(models[0]))
for m in models:
    m.train()



