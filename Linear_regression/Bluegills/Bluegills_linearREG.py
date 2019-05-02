# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 11:30:41 2019

@author: PRINCE
"""

  

''' Bluegills  '''
 
dataset3 = pd.read_csv('bluegills.csv')
 
dataset3.head(10) 
 
plt.scatter(dataset3['age'], dataset3['length'], color='red')

from sklearn.preprocessing import PolynomialFeatures

from sklearn.linear_model import LinearRegression

reg3 = LinearRegression()


poly_features = PolynomialFeatures(degree=2)
 
X = dataset3.iloc[:,:-1].values
y = dataset3.iloc[:,1].values
 

 
feature = poly_features.fit_transform(X)

poly_features.fit(feature,y)

reg3.fit(feature,y)

predictions = reg3.predict(feature)


from sklearn.metrics import mean_squared_error, r2_score
  # evaluating the model on test dataset
  rmse_test = np.sqrt(mean_squared_error(y, predictions))
  r2_test = r2_score(y, predictions)


predictions = reg3.predict(feature)

plt.scatter(dataset3['age'], dataset3['length'], color='red')
plt.plot(X,predictions,'b')

reg3.score(feature,y)

