# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 20:13:37 2018

@author: User
"""

def k_fold(k,data):
    A=[data//k]*k
    for i in range (data-(data//k)*k):
        A[i]=A[i]+1
    return(A)

    
        

x=k_fold(10,len(df))
type(x)
import numpy as np
import pandas as pd
import pandas as pd

from pandas import Series,DataFrame

df=pd.read_csv('C:\\Users\\User\\Documents\\GitHub\\datamining\\data.csv') 

df=df.replace('?',np.nan)

col=df.columns[df.isnull().any()]
df[col]=df[col].apply(lambda x:x.fillna(x.mode, inplace=True))

Y=df.iloc[:,14]

for i in range(len(Y)):
    if  Y[i]=='<=50K':
        Y[i]=0
    else:
        Y[i]=1



len(df)
idxs=np.arange(len(df))
np.random.shuffle(idxs)


idxs


x=idxs[k_fold(10,len(df))]


df.iloc[[0,4]]
df.iloc[0:4]
df[idxs[5]]
a=df.iloc[31770]


k_fold(10,len(df))[1]

type(k_fold(10,len(df)))
for i in range(10):
    train = df.iloc[idxs[i]]
    valid = df.iloc[idxs[other]]







    
    