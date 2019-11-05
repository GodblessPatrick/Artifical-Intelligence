#import librabies
import numpy as np
from sklearn import tree
from sklearn import metrics 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.externals.six import StringIO  
from sklearn.model_selection import cross_validate
from matplotlib import pyplot as plt

#Simple list chunker function
def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0
    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg
    return out

#create decision tree and train on validation set
def dt(x,y,X,Y,depth):
    classifier = DecisionTreeClassifier(criterion='entropy',max_depth = depth)  
    classifier.fit(x,y)
    pred = classifier.predict(x)
    pred2 = classifier.predict(X)
    return accuracy_score(y,pred),accuracy_score(Y,pred2)

#cross validation 
def cross_validation(X_total,Y_total,chunks,chunksY):
    train_list = np.zeros((10,10))
    vad_list = np.zeros((10,10))
    index = 0
    for depth in range(1,11):
        for i in range(10):
            train,vad = dt(X_total[i],Y_total[i],chunks[i],chunksY[i],depth)
            train_list[index][i] = train
            vad_list[index][i] = vad
        index += 1
    return train_list,vad_list

#import data from file
x = np.loadtxt(open("set_a.csv","rb"),delimiter=",",unpack = True)

#spilt data to x and y 
y = x[len(x)-1]
x= np.delete(x,4,0)
x = x.transpose()

#divide data to 10 chunks
chunks = chunkIt(x,10)
chunksY = chunkIt(y,10)

#train sets for cross validation
X1 = np.concatenate((chunks[1],chunks[2],chunks[3],chunks[4],chunks[5],chunks[6],chunks[7],chunks[8],chunks[9]))

X2 = np.concatenate((chunks[0],chunks[2],chunks[3],chunks[4],chunks[5],chunks[6],chunks[7],chunks[8],chunks[9]))

X3 = np.concatenate((chunks[1],chunks[0],chunks[3],chunks[4],chunks[5],chunks[6],chunks[7],chunks[8],chunks[9]))

X4 = np.concatenate((chunks[1],chunks[2],chunks[0],chunks[4],chunks[5],chunks[6],chunks[7],chunks[8],chunks[9]))

X5 = np.concatenate((chunks[1],chunks[2],chunks[3],chunks[0],chunks[5],chunks[6],chunks[7],chunks[8],chunks[9]))

X6 = np.concatenate((chunks[1],chunks[2],chunks[3],chunks[4],chunks[0],chunks[6],chunks[7],chunks[8],chunks[9]))

X7 = np.concatenate((chunks[1],chunks[2],chunks[3],chunks[4],chunks[5],chunks[0],chunks[7],chunks[8],chunks[9]))

X8 = np.concatenate((chunks[1],chunks[2],chunks[3],chunks[4],chunks[5],chunks[6],chunks[0],chunks[8],chunks[9]))

X9 = np.concatenate((chunks[1],chunks[2],chunks[3],chunks[4],chunks[5],chunks[6],chunks[7],chunks[0],chunks[9]))

X10 = np.concatenate((chunks[1],chunks[2],chunks[3],chunks[4],chunks[5],chunks[6],chunks[7],chunks[8],chunks[0]))

Y1 = np.concatenate((chunksY[1],chunksY[2],chunksY[3],chunksY[4],chunksY[5],chunksY[6],chunksY[7],chunksY[8],chunksY[9]))

Y2 = np.concatenate((chunksY[0],chunksY[2],chunksY[3],chunksY[4],chunksY[5],chunksY[6],chunksY[7],chunksY[8],chunksY[9]))

Y3 = np.concatenate((chunksY[1],chunksY[0],chunksY[3],chunksY[4],chunksY[5],chunksY[6],chunksY[7],chunksY[8],chunksY[9]))

Y4 = np.concatenate((chunksY[1],chunksY[2],chunksY[0],chunksY[4],chunksY[5],chunksY[6],chunksY[7],chunksY[8],chunksY[9]))

Y5 = np.concatenate((chunksY[1],chunksY[2],chunksY[3],chunksY[0],chunksY[5],chunksY[6],chunksY[7],chunksY[8],chunksY[9]))

Y6 = np.concatenate((chunksY[1],chunksY[2],chunksY[3],chunksY[4],chunksY[0],chunksY[6],chunksY[7],chunksY[8],chunksY[9]))

Y7 = np.concatenate((chunksY[1],chunksY[2],chunksY[3],chunksY[4],chunksY[5],chunksY[0],chunksY[7],chunksY[8],chunksY[9]))

Y8 = np.concatenate((chunksY[1],chunksY[2],chunksY[3],chunksY[4],chunksY[5],chunksY[6],chunksY[0],chunksY[8],chunksY[9]))

Y9 = np.concatenate((chunksY[1],chunksY[2],chunksY[3],chunksY[4],chunksY[5],chunksY[6],chunksY[7],chunksY[0],chunksY[9]))

Y10 = np.concatenate((chunksY[1],chunksY[2],chunksY[3],chunksY[4],chunksY[5],chunksY[6],chunksY[7],chunksY[8],chunksY[0]))

#If i put the train sets in one list,it's easily to use them
X_total = [X1,X2,X3,X4,X5,X6,X7,X8,X9,X10]
Y_total = [Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9,Y10]

#create decision tree classifier and using cv to test max_depth
#the candidate depth is 1 2 3
train,vad = cross_validation(X_total,Y_total,chunks,chunksY)

#plot graphs
#train set 
for i in range(10):
    plt.plot([1,2,3,4,5,6,7,8,9,10],train[i])
    plt.title('Train set accuracy with max depth = %s' %(i+1))
    plt.xlabel("Times")
    plt.ylabel("Test accuracy")
    plt.show()
#validation set
for i in range(10):
    plt.plot([1,2,3,4,5,6,7,8,9,10],vad[i])
    plt.title('validation set accuracy with max depth = %s' %(i+1))
    plt.xlabel("Times")
    plt.ylabel("Test accuracy")
    plt.show()

#output the tree
classifier = DecisionTreeClassifier(criterion='entropy',max_depth = 10)  
classifier.fit(x,y)
pred = classifier.predict(x)
dot_data = StringIO() 
tree.export_graphviz(classifier,out_file='tree2.dot') 
