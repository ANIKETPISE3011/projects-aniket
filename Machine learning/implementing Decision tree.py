import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv('C:\\DS\\DATA SCIENCE\\petrol_consumption.csv')
dataset.head()
X=dataset.drop('Petrol_Consumption',axis=1)
y=dataset['Petrol_Consumption']
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)
from sklearn.tree import DecisionTreeRegressor
regressor=DecisionTreeRegressor()
regressor.fit(X_train,y_train)
y_pred=regressor.predict(X_test)
df=pd.DataFrame({'Actual':y_test,'Predicted':y_pred})
print(df.head())
from sklearn import metrics
print('Mean Absolute Error:',metrics.mean_absolute_error(y_test,y_pred))
print('Mean Squared Error:',metrics.mean_squared_error(y_test,y_pred))
print('Root Mean Squared Error:',np.sqrt(metrics.mean_squared_error(y_test,y_pred)))