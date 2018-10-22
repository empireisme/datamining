# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 20:43:29 2018

@author: User
"""

import pandas as pd
from pandas import Series,DataFrame
df=pd.read_excel('C:\\Users\\User\\Documents\\GitHub\\datamining\\hw2data.xls') 

df1=df.iloc[  4914:6569 ,:   ] #抽出了10月份到12月份的資料 但是使用目測法 
dfNR0=df1.replace('NR',0) #把NR用0來替換
# ＴＥＳＴ這是測試!

find=dfNR0['00'].str.contains('#*x')






