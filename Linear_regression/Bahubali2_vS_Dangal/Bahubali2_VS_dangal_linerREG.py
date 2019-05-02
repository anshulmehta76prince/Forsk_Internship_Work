# -*- coding: utf-8 -*-
"""
Created on Thu May  2 08:00:18 2019

@author: PRINCE
"""

''' Bahubali2 VS Dangal Movie '''

import pandas as pd

dataset = pd.read_csv('Bahubali2_vs_Dangal.csv')

dataset.head()

dataset.info()
dataset.describe()

X = dataset.iloc[:,:-2].values
y = dataset.iloc[:,:-1].values
z = dataset.iloc[:,2].values

from sklearn.linear_model import LinearRegression

reg = LinearRegression()

reg.fit(X,y)

reg.score(X,y)

print('Collection Of Bahubali2 Movie on 10th Day',reg.predict(10))

reg.fit(X,z)

reg.score(X,z)

print('Collection Of Dangal Movie on 10th Day',reg.predict(10))
