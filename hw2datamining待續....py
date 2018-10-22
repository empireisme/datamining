# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 20:43:29 2018

@author: User
"""

import pandas as pd
from pandas import Series,DataFrame
df=pd.read_excel('C:\\Users\\User\\Documents\\GitHub\\datamining\\hw2data.xls') 

df1=df.iloc[  4914:6569 ,:   ] #抽出了10月份到12月份的資料 但是使用目測法 
dfNR0=df.replace('NR',0) #把NR用0來替換


# ＴＥＳＴ這是測試!

find=dfNR0['00'].str.contains('#*x')  #找出缺失值


df3=dfNR0.iloc[ 4914:6569 ,3: 100 ]
         
type(find)

#把時間序列的資料串起來
    
for i in range(0,1):
    for j in range(18,1000,18):
        b=df3.iloc[i,:].append(df3.iloc[i+j,:])
        for x in range(18,1654,18):
            b=b.append(df3.iloc[i+x,:])
    d0=b[0:27].append(b[ 54: 2511  ])
    
for i in range(1,2):
    for j in range(18,1000,18):
        b=df3.iloc[i,:].append(df3.iloc[i+j,:])
        for x in range(18,1654,18):
            b=b.append(df3.iloc[i+x,:])
    d1=b[0:27].append(b[ 54: 2511  ])
    
for i in range(2,3):
    for j in range(18,1000,18):
        b=df3.iloc[i,:].append(df3.iloc[i+j,:])
        for x in range(18,1654,18):
            b=b.append(df3.iloc[i+x,:])
    d2=b[0:27].append(b[ 54: 2511  ])
    
for i in range(3,4):
    for j in range(18,1000,18):
        b=df3.iloc[i,:].append(df3.iloc[i+j,:])
        for x in range(18,1654,18):
            b=b.append(df3.iloc[i+x,:])
    d3=b[0:27].append(b[ 54: 2511  ])
    
for i in range(4,5):
    for j in range(18,1000,18):
        b=df3.iloc[i,:].append(df3.iloc[i+j,:])
        for x in range(18,1654,18):
            b=b.append(df3.iloc[i+x,:])
    d4=b[0:27].append(b[ 54: 2511  ])

for i in range(5,6):
    for j in range(18,1000,18):
        b=df3.iloc[i,:].append(df3.iloc[i+j,:])
        for x in range(18,1654,18):
            b=b.append(df3.iloc[i+x,:])
    d5=b[0:27].append(b[ 54: 2511  ])
    

for i in range(6,7):
    for j in range(18,1000,18):
        b=df3.iloc[i,:].append(df3.iloc[i+j,:])
        for x in range(18,1654,18):
            b=b.append(df3.iloc[i+x,:])
    d6=b[0:27].append(b[ 54: 2511  ])
    
for i in range(7,8):
    for j in range(18,1000,18):
        b=df3.iloc[i,:].append(df3.iloc[i+j,:])
        for x in range(18,1654,18):
            b=b.append(df3.iloc[i+x,:])
    d7=b[0:27].append(b[ 54: 2511  ])
    
for i in range(8,9):
    for j in range(18,1000,18):
        b=df3.iloc[i,:].append(df3.iloc[i+j,:])
        for x in range(18,1654,18):
            b=b.append(df3.iloc[i+x,:])
    d8=b[0:27].append(b[ 54: 2511  ])
    
for i in range(9,10):
    for j in range(18,1000,18):
        b=df3.iloc[i,:].append(df3.iloc[i+j,:])
        for x in range(18,1654,18):
            b=b.append(df3.iloc[i+x,:])
    d9=b[0:27].append(b[ 54: 2511  ])
    

for i in range(10,11):
    for j in range(18,1000,18):
        b=df3.iloc[i,:].append(df3.iloc[i+j,:])
        for x in range(18,1654,18):
            b=b.append(df3.iloc[i+x,:])
    d10=b[0:27].append(b[ 54: 2511  ])
    
for i in range(11,12):
    for j in range(18,1000,18):
        b=df3.iloc[i,:].append(df3.iloc[i+j,:])
        for x in range(18,1654,18):
            b=b.append(df3.iloc[i+x,:])
    d11=b[0:27].append(b[ 54: 2511  ])
    
for i in range(12,13):
    for j in range(18,1000,18):
        b=df3.iloc[i,:].append(df3.iloc[i+j,:])
        for x in range(18,1654,18):
            b=b.append(df3.iloc[i+x,:])
    d12=b[0:27].append(b[ 54: 2511  ])
    
for i in range(13,14):
    for j in range(18,1000,18):
        b=df3.iloc[i,:].append(df3.iloc[i+j,:])
        for x in range(18,1654,18):
            b=b.append(df3.iloc[i+x,:])
    d13=b[0:27].append(b[ 54: 2511  ])
    
for i in range(14,15):
    for j in range(18,1000,18):
        b=df3.iloc[i,:].append(df3.iloc[i+j,:])
        for x in range(18,1654,18):
            b=b.append(df3.iloc[i+x,:])
    d14=b[0:27].append(b[ 54: 2511  ])
    

for i in range(15,16):
    for j in range(18,1000,18):
        b=df3.iloc[i,:].append(df3.iloc[i+j,:])
        for x in range(18,1654,18):
            b=b.append(df3.iloc[i+x,:])
    d15=b[0:27].append(b[ 54: 2511  ])
    
for i in range(16,17):
    for j in range(18,1000,18):
        b=df3.iloc[i,:].append(df3.iloc[i+j,:])
        for x in range(18,1654,18):
            b=b.append(df3.iloc[i+x,:])
    d16=b[0:27].append(b[ 54: 2511  ])
    
for i in range(17,18):
    for j in range(18,1000,18):
        b=df3.iloc[i,:].append(df3.iloc[i+j,:])
        for x in range(18,1654,18):
            b=b.append(df3.iloc[i+x,:])
    d17=b[0:27].append(b[ 54: 2511  ])
    
list(range(17,18))

use=pd.concat([d0,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16],axis=1)

#未完待續......
    
  


    
    




    

    







             
  


print(df1.iloc[1,:])      
        

a=[]
for i in range(5):    
    a.append(i)
a # the list with the new items.
        
    


        







