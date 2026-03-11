from dataclasses import dataclass

@dataclass
class Student:
    name: str
    marks: int

s1 = Student("Ali", 85)
print(s1)

'_________________________________________________'

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

s1 = Student("Ali", 85)

'__________________________________________________'

from dataclasses import dataclass

@dataclass
class ModelConfig:
    learning_rate: float
    epochs: int
    batch_size: int

config = ModelConfig(0.01, 50, 32)
print(config)


