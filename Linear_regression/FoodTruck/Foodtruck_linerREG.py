# -*- coding: utf-8 -*-
"""
Created on Thu May  2 08:02:52 2019

@author: PRINCE
"""

''' Food Truck  '''

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

pd = pd.read_csv("Foodtruck.csv")

pd.isna()

pd.describe()

pd['Profit'].max()

from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split

X = pd.iloc[:,:-1].values

y= pd.iloc[:,1].values

X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.33, random_state=42)

regressor = LinearRegression()

regressor.fit(X_train,y_train)

predictions = regressor.predict(X_test)

plt.scatter(X_train,y_train)
plt.plot(X_test,predictions,'r')

plt.xlabel('Population')
plt.ylabel('Profit')


regressor.score(X_train,y_train)
regressor.predict(3.073)
