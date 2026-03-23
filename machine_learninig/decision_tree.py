"""A decision tree is a supervised learning algorithm used for both classification and regression tasks. 
It has a hierarchical tree structure which consists of a root node, branches, internal nodes and leaf nodes.
 It works like a flowchart that helps in making step by step decision, where:
1-Internal nodes represent attribute tests
2-Branches represent attribute values
3-Leaf nodes represent final decisions or predictions.
doctor example:
if fever>100
yes=cough? 
yes>flue
no>Maybe
no>no flue"""
from sklearn.tree import DecisionTreeClassifier
X=[[7,2], #apple
   [8,3], #apple
   [9,8], #orange
   [10,9] #orange
   ]
y=[0,0,1,1] #0=apple ,1=orange
model=DecisionTreeClassifier()
model.fit(X,y)
size=float(input("enter the fruit size in cm:"))
shade=float(input("enter color shade[1-10]:"))

result=model.predict([[size,shade]])[0]
if result==0:
    print("this is likely an apple")
else:
    print("this is likely an orange")