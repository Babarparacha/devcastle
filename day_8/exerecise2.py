class MyDataset:
    def __init__(self,data):
        self.data=data

    def __add__(self,other):
        return MyDataset(self.data+other.data)
    def __str__(self):
        return f"Dataset:{self.data}"
# teo simple MyDataset
d1=MyDataset([10,20,30])
d2=MyDataset([5,10,15])

# merge using +
merged=d1+d2

print(d1)
print(d2)
print(merged)