"""K‑Nearest Neighbor (KNN) is a simple and widely used machine learning technique for
 classification and regression tasks. It works by identifying the K closest data points 
 to a given input and making predictions 
based on the majority class or average value of those neighbors.
Classifies data based on similarity with nearby data points
Uses distance metrics like Euclidean distance to find nearest neighbors
Since KNN makes no assumptions about the underlying data distribution,
 it makes it a non-parametric and instance-based learning method.
 use slow for big data and use odd numbers always
 If k = 3, the algorithm looks at the 3 closest fruits to the new one.
If 2 of those 3 fruits are apples and 1 is a banana, 
the algorithm says the new fruit is an apple because most of its neighbors are apples.
 """

from sklearn.neighbors import KNeighborsClassifier

X=[[180,7],
   [200,7.5],
   [250,8],
   [300,8.5],
   [330,9],
   [360,9.5]
   ]
#0=apple 1=orange #let assume
y=[0,0,0,1,1,1]

model=KNeighborsClassifier(n_neighbors=3) #pass neighbours to look

model.fit(X,y)
weight=float(input("enter the weight in grams:"))
size=float(input("enter the size in cm:"))

prediction=model.predict([[weight,size]])[0]
if prediction==0:
    print("this is likely an apple")
else:
    print("this is likely an orange")