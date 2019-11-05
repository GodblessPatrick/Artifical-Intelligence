#import librabies
import numpy as np
from sklearn import tree
from sklearn import metrics 
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.externals.six import StringIO  
from sklearn.model_selection import cross_validate

#import data from file
x = np.loadtxt(open("set_a.csv","rb"),delimiter=",",unpack = True)

#spilt data to x and y 
y = x[len(x)-1]
x = x.transpose()

#create decision tree classifier
classifier = DecisionTreeClassifier(criterion='entropy')  
classifier.fit(x, y)
pred = classifier.predict(x)
print('the accuracy of train x is %s'% (accuracy_score(y,pred) * 100))

#output the tree
dot_data = StringIO() 
tree.export_graphviz(classifier,out_file='tree.dot') 