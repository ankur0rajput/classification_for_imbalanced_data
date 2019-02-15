# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 18:09:14 2019

@author: hp
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

# Importing the dataset
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
test_target=np.int64(test_target)

#remove the income level from both train amd test
del train['income_level']
del test['income_level']

l=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,27,29,30,31,32,33,34,35,36,37,38,39]
test=test[test.columns[l]]
train=train[train.columns[l]]

#Now, let’s separate categorical variables & numerical variables
train_num_cols = train._get_numeric_data().columns
train_cols = train.columns
train_cat_cols=list(set(train_cols) - set(train_num_cols))

test_num_cols = test._get_numeric_data().columns
test_cols = test.columns
test_cat_cols=list(set(test_cols) - set(test_num_cols))

train_num=[]
train_cat=[]
for i,j in enumerate(train):
    for s in train_num_cols:
        if j==s:
            train_num.append(i)
    for t in train_cat_cols:
        if j==t:
            train_cat.append(i)

test_num=[]
test_cat=[]
for i,j in enumerate(test):
    for s in test_num_cols:
        if j==s:
            test_num.append(i)
    for t in test_cat_cols:
        if j==t:
            test_cat.append(i)

#del train_num[-1]
#del test_cat[-1]
'''            
num_train=train.iloc[:,train_num].values
cat_train=train.iloc[:,train_cat].values

num_test=test.iloc[:,test_num].values
cat_test=test.iloc[:,test_cat].values

'''
num_train=train[train.columns[train_num]]
cat_train=train[train.columns[train_cat]]

num_test=test[test.columns[test_num]]
cat_test=test[test.columns[test_cat]]

#selecting columns with missing value less than 5%
#cat_train=cat_train[cat_train.columns[cat_train.isnull().mean() < 0.05]]

#cat_test=cat_test[cat_test.columns[cat_test.isnull().mean() < 0.05]]

cat_train=cat_train.fillna('Unavailable')
cat_test=cat_test.fillna('Unavailable')

####Data manipulation
#combine factor levels with less than 5% values
#replace the values from certain columns in a pandas.DataFrame that occur rarely,
# i.e. with low frequency i.e 5% (while ignoring NaNs)
p=0.05
cat_train=cat_train.apply(lambda x: x.mask(x.map(x.value_counts())<(p*(x.value_counts().sum())), 'other') if x.name!='C' else x)
cat_test=cat_test.apply(lambda x: x.mask(x.map(x.value_counts())<(p*(x.value_counts().sum())), 'other') if x.name!='C' else x)

#cat_train=cat_train.stack().pipe(lambda s: pd.Series(pd.factorize(s.values)[0], s.index)).unstack()
#cat_test=cat_test.stack().pipe(lambda s: pd.Series(pd.factorize(s.values)[0], s.index)).unstack()

class MultiColumnLabelEncoder:
    def __init__(self,columns = None):
        self.columns = columns # array of column names to encode

    def fit(self,X,y=None):
        return self # not relevant here

    def transform(self,X):
        '''
        Transforms columns of X specified in self.columns using
        LabelEncoder(). If no columns specified, transforms all
        columns in X.
        '''
        output = X.copy()
        if self.columns is not None:
            for col in self.columns:
                output[col] = LabelEncoder().fit_transform(output[col])
        else:
            for colname,col in output.iteritems():
                output[colname] = LabelEncoder().fit_transform(col)
        return output

    def fit_transform(self,X,y=None):
        return self.fit(X,y).transform(X)
m=[]
n=[]
for i in cat_train:
    m.append(i)
for i in cat_test:
    n.append(i)
    
cat_train=MultiColumnLabelEncoder(columns = m).fit_transform(cat_train)
cat_test=MultiColumnLabelEncoder(columns = n).fit_transform(cat_test)

####data manipulation by binning in num_train and num_test

#age column into young,adult,old levels in num_train and num_test
bins=[0,30,60,90]
group_names=['Young','Adult','Old']
num_train['age']=pd.cut(num_train['age'],bins,labels=group_names)
num_test['age']=pd.cut(num_test['age'],bins,labels=group_names)

#wage_per_hour,capital_gains,capital_losses,dividend_from_Stocks columns into Zeo,MoreThanZero levels in num_train and num_test 
bins_1=[-1,0,9999]
bins_2=[-1,0,99999]
bins_3=[-1,0,4608]

group_names_1=['Zero','MoreThanZero']

num_train['wage_per_hour']=pd.cut(num_train['wage_per_hour'],bins_1,labels=group_names_1)
num_train['capital_gains']=pd.cut(num_train['capital_gains'],bins_2,labels=group_names_1)
num_train['capital_losses']=pd.cut(num_train['capital_losses'],bins_3,labels=group_names_1)
num_train['dividend_from_Stocks']=pd.cut(num_train['dividend_from_Stocks'],bins_2,labels=group_names_1)

num_test['wage_per_hour']=pd.cut(num_test['wage_per_hour'],bins_1,labels=group_names_1)
num_test['capital_gains']=pd.cut(num_test['capital_gains'],bins_2,labels=group_names_1)
num_test['capital_losses']=pd.cut(num_test['capital_losses'],bins_3,labels=group_names_1)
num_test['dividend_from_Stocks']=pd.cut(num_test['dividend_from_Stocks'],bins_2,labels=group_names_1)

a=['age','wage_per_hour','capital_gains','capital_losses','dividend_from_Stocks']
num_train=MultiColumnLabelEncoder(columns = a).fit_transform(num_train)
num_test=MultiColumnLabelEncoder(columns = a).fit_transform(num_test)

num_train['age']=num_train['age'].fillna('Young')
num_test['age']=num_test['age'].fillna('Young')

a=['age','wage_per_hour','capital_gains','capital_losses','dividend_from_Stocks']
num_train=MultiColumnLabelEncoder(columns = a).fit_transform(num_train)
num_test=MultiColumnLabelEncoder(columns = a).fit_transform(num_test)