# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 20:43:29 2018

@author: User
"""

import pandas as pd
from pandas import Series,DataFrame
df=pd.read_excel('C:\\Users\\User\\Documents\\GitHub\\L4Python\\hw2data.xls') 

df1=df.iloc[  4914:6569 ,:   ] #抽出了10月份到12月份的資料 但是使用目測法

