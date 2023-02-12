from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
boston_data=load_boston()
print(boston_data.keys())
boston=pd.DataFrame(boston_data.data,columns=boston_data.feature_names)
print(boston.head())

boston['MEDV']=boston_data.target
#count the number of missing values for each feature
print(boston.isnull().sum())
correlation_matrix=boston.corr().round(2)
# annot= true to print the values inside the square
plt.show()
sns.heatmap(data=correlation_matrix,annot=True)
X=pd.DataFrame(np.c_[boston['LSTAT'],boston['RM']],columns=['LSTAT','RM'])
y=boston['MEDV']
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=5)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
lin_model=LinearRegression()
lin_model.fit(X_train,y_train)
# model evalution for traning set
y_train_predict=lin_model.predict(X_train)
rmse=(np.sqrt(mean_squared_error(y_train,y_train_predict)))

print('The model performance for traning set')
print('--------------------------------------------')
print('RSME is{}'.format(rmse))
# model evaluation for testing set
y_test_predict=lin_model.predict(X_test)
rmse=(np.sqrt(mean_squared_error(y_test,y_test_predict)))
print('The model performance for testing set')
print('------------------------------------------')
print('RMSE is {}'.format(rmse))
