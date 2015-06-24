'''
Created on 24.06.2015

@author: niklas
'''
from sklearn.datasets import load_iris
from sklearn import cross_validation
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm

iris = load_iris()

#print iris.data.shape

X = iris.data[:,:2]

y = iris.target

X_train = X[:90]

y_train = y[:90]

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size = 0.2)

#--------------------------------------------

clf = DecisionTreeClassifier()

clf_fitted = clf.fit(X_train, y_train)

print clf_fitted.score(X_test, y_test)

#---------------------------------------------

clf = svm.LinearSVC(C = 5)

clf_fitted = clf.fit(X_train, y_train)

print clf_fitted.score(X_test, y_test)

#---------------------------------------------

Clist = [10**i for i in range(-5, 5)]

for C in Clist:
    clf = svm.LinearSVC(C = C)
    scores = cross_validation.cross_val_score(clf, X, y, cv = 5)
    print ("C = %0.5f" % (C)) 
    print ("Accurancy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std()*2))

