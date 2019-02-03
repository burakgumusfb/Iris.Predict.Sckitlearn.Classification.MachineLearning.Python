
from sklearn import tree
from sklearn.model_selection import train_test_split  
from sklearn.datasets import load_iris
iris=load_iris()

x = iris.data
y = iris.target

xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size = 1/3, random_state = 0)

clf = tree.DecisionTreeClassifier()
clf.fit(xTest, yTest)

def Iris(flower):
		if flower==0:
			print("setosa")
		elif flower==1:
			print("versicolor")
		else:
			print("virginica")
            
clf = tree.DecisionTreeClassifier()
clf.fit(xTrain, yTrain)

d1 = float(input("Enter sepal length : "))
d2 = float(input("Enter sepal width : "))
d3 = float(input("Enter petal length : "))
d4 = float(input("Enter petal width : "))

data = [[d1, d2, d3, d4]]

num = clf.predict(data)

Iris(num)

print (clf.score(xTest,yTest))

#6.3,3.3,4.7,1.6