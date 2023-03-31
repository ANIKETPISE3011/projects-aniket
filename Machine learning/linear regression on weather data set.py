import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
dataset=pd.read_csv(r'C:\DS\DATA SCIENCE\DATA\weather.csv')
dataset.plot(x='MinTemp',y='MaxTemp',style='o')
plt.title('MinTemp vs MaxTemp')
plt.xlabel('MinTemp')
plt.ylabel('MaxTemp')
plt.show()
from sklearn.model_selection import train_test_split
X=dataset['MinTemp'].values.reshape(-1,1)
y=dataset['MaxTemp'].values.reshape(-1,1)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)
from sklearn.linear_model import LinearRegression
lm=LinearRegression()
lm.fit(X_train,y_train)
print(lm.intercept_)
print(lm.coef_)
pred=lm.predict(X_test)
df=pd.DataFrame({'Actual':y_test.flatten(),'predicted':pred.flatten()})
df1=df.head(25)
df1.plot(kind='bar',figsize=(16,10))
plt.grid(which='major',linestyle='-',linewidth='0.5',color='green')
plt.grid(which='minor',linestyle=':',linewidth='0.5',color='black')
plt.show()
plt.scatter(X_test,y_test,color='gray')
plt.plot(X_test,y_test,pred,color='r',linewidth=2)
plt.show()
from sklearn import metrics
print('Mean Absolute Error:',metrics.mean_absolute_error(y_test,pred))
print('Mean squared Error:',metrics.mean_squared_error(y_test,pred))
print('Root Mean Squared Error:',np.sqrt(metrics.mean_squared_error(y_test,pred)))

