# -*- coding: utf-8 -*-
"""
Created on Thu May  2 08:04:57 2019

@author: PRINCE
"""

''' IQ Size '''

import numpy as np
import pandas as pd
dataset = pd.read_csv('C:/Users/Suraj  kumar/Desktop/Forsk_Lab/Forsk_Regression/iq_size.csv')
X = dataset.iloc[:, 1:4].values
y = dataset.iloc[:, 0].values

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X, y)
print(regressor.score(X,y))
X
z=[[90,70,150]]
y_pred = regressor.predict(z)
print(y_pred)

import statsmodels.formula.api as sm
X = np.append ( arr = np.ones([38,1]).astype(float), values = X, axis =1 )
X_opt = X[:,[0,1,2,3]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X[:,[0,1,2]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X[:,[1,2]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X[:,[1]]
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regressor_OLS.summary()

# Best Feature is Brain Size
 