# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 14:09:48 2018

@author: User
"""

import pandas as pd
from pandas import Series,DataFrame
df=pd.read_csv('C:\\Users\\User\\Documents\\GitHub\\L4Python\\character-deaths.csv') 

#路徑記得要加上\\ 雙斜線

print(df)

df=df.fillna(0)
#將 缺失值補上0

print(df)

df.iloc[ : ,0 ]
df.iloc[ : ,1 ]
df.iloc[ : ,2 ]

df1=df.iloc[ : ,0:3 ]  #抽出第一行到第3行
df2=df.iloc[ : ,5:13] #抽出第6行到第12行

Y=df1.iloc[:,2]  


for i in range(len(Y)):
    if  Y[i]>0:
        Y[i]=1
        
df3=pd.concat([df1,df2],axis=1)

dummies = pd.get_dummies(df3['Allegiances'])

df4=pd.concat([df3,dummies],axis=1)

datause = df4.drop(['Allegiances'],axis=1) #把Allegiances變數刪掉 因為已經dummy了

X=datause.drop(  ['Death Year','Name'],axis=1     )

from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.cross_validation import train_test_split

train_X, test_X, train_y, test_y = train_test_split(X, Y, test_size = 0.25) 

#切割training 和 testing

clf = tree.DecisionTreeClassifier()
death_clf = clf.fit(train_X, train_y) #拿訓練集來建立模型

test_y_predicted= death_clf.predict(test_X) #做預測

print(test_y_predicted)

from sklearn.metrics import accuracy_score

accuracy_score(test_y, test_y_predicted)

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
C=confusion_matrix(test_y, test_y_predicted) #confusion matrix
print(C)
from sklearn.metrics import classification_report
print(classification_report(test_y, test_y_predicted)) #precision and recall
print(accuracy_score(test_y, test_y_predicted))


from sklearn.tree import export_graphviz
export_graphviz(clf,out_file='tree.dot',max_depth=5)


