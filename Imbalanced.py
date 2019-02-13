# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 18:23:50 2019

@author: hp
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

# Importing the dataset

#..............................................training.....................................
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

    
train_target=train.iloc[:,[40]].values

test_target=test.iloc[:,[40]].values

for item in train_target:
    if item[0] == -50000:
        item[0] = 0
    else:
        item[0] = 1
        
for item in test_target:
    #item[0].astype(int)
    if item[0] == "-50000":
        item[0] = 0
        #item[0].astype(str).astype(int)
    else:
        item[0] = 1
        
test_target=test_target.astype(str).astype(int) 

#p=train.describe()
#......................................Data Cleaning..........
train=train.replace('N/A',np.NaN)

#train['class_of_worker'].value_counts().sum()
'''
for i,j in enumerate(train):
    print(i,train[j].value_counts().sum(),j)
'''

#11 198649 hispanic_origin, 21 198815 state_of_previous_residence
    
#24 99827 migration_msa..............almost 50% missing data
#25 99827 migration_reg..............almost 50% missing data
#26 99827 migration_within_reg..............almost 50% missing data
#28 99827 migration_sunbelt..............almost 50% missing data
    
#31 192810 country_father....
#32 193404 country_mother....
#33 196130 country_self .....
    
#train_features=train.iloc[:,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,27,29,30,31,32,33,34,35,36,37,38,39,40]].values

#train_features=train_features.replace('N/A',np.NaN)

#train1=train.columns[train.isnull().mean() < 0.5]
train2=train[train.columns[train.isnull().mean() < 0.05]]

'''
for i,j in enumerate(train2):
    print(i,train2[j].value_counts().sum(),j)
    
'''

#finding corelation we weeks_worked_in_a_year automatically get cancelled
del train2['weeks_worked_in_year']  
  
train2=train2.fillna('Unavailable')

#................................Data Manipulation...........
def which(self):
    try:
        self = list(iter(self))
    except TypeError as e:
        raise Exception("""'which' method can only be applied to iterables.
        {}""".format(str(e)))
    indices = [i for i, x in enumerate(self) if bool(x) == True]
    return(indices)

bins=[0,30,60,90]
group_names=['Young','Adult','Old']
train2['age']=pd.cut(train2['age'],bins,labels=group_names)

#train2['wage_per_hour'].max()----9999,train2['capital_gains'].max()----99999,train2['capital_losses'].max()----4608,train2['dividend_from_Stocks'].max()----99999
#train2['wage_per_hour'].min()-------0,train2['capital_gains'].min()----0,train2['capital_losses'].min()----0,train2['dividend_from_Stocks'].min()----0

bins_1=[-1,0,9999]
bins_2=[-1,0,99999]
bins_3=[-1,0,4608]

group_names_1=['Zero','MoreThanZero']

train2['wage_per_hour']=pd.cut(train2['wage_per_hour'],bins_1,labels=group_names_1)
train2['capital_gains']=pd.cut(train2['capital_gains'],bins_2,labels=group_names_1)
train2['capital_losses']=pd.cut(train2['capital_losses'],bins_3,labels=group_names_1)
train2['dividend_from_Stocks']=pd.cut(train2['dividend_from_Stocks'],bins_2,labels=group_names_1)

def percConvert(ser):
  return ser/float(ser[-1])
pd.crosstab(train2["wage_per_hour"],train2["income_level"],margins=True).apply(percConvert, axis=1)
  
t=pd.crosstab(index=train2["wage_per_hour"],columns="count")#.apply(percConvert,axis=1)
t/t.sum()

 
  
  
  
