import numpy as np
from sklearn import tree
from sklearn import metrics 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.externals.six import StringIO  
from sklearn.model_selection import cross_validate
from matplotlib import pyplot as plt

#import data from file
x = np.loadtxt(open("set_a.csv","rb"),delimiter=",",unpack = True)
X = np.loadtxt(open("set_b.csv","rb"),delimiter=",",unpack = True)

#spilt data to x and y 
y = x[len(x)-1]
x = x.transpose()
Y = X[len(X)-1]
X = X.transpose()


#create decision tree classifier
classifier = DecisionTreeClassifier(criterion='entropy',max_depth=10)  
classifier.fit(x, y)
pred = classifier.predict(X)
print('the accuracy of train x is %s'% (accuracy_score(Y,pred) * 100))

