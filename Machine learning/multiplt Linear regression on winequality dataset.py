import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
dataset=pd.read_csv(r'C:\DS\DATA SCIENCE\DATA\winequality-red.csv')
dataset.isnull().any()
dataset=dataset.fillna(method='ffill')
X=dataset[['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','pH','sulphates','alcohol']].values
y=dataset['quality'].values
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)
lr=LinearRegression()
lr.fit(X_train,y_train)
pred=lr.predict(X_test)
df=pd.DataFrame({'Actual':y_test,'Predicted':pred})
df1=df.head(25)
df1.plot(kind='bar',figsize=(10,8))
plt.grid(which='major',linestyle='-',linewidth='0.5',color='green')
plt.grid(which='minor',linestyle=':',linewidth='0.5',color='black')
plt.show()
print('Mean Absolute Error:',metrics.mean_absolute_error(y_test,pred))
print('Mean squared Error:',metrics.mean_squared_error(y_test,pred))
print('Root Mean Squared Error:',np.sqrt(metrics.mean_squared_error(y_test,pred)))