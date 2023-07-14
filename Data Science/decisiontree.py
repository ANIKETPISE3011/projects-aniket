import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeClassifier

df=pd.read_csv("C:/sem2/bda/prac/Social_Network_Ads.csv")
print(df)
X=df[['Age','EstimatedSalary']]
print(X)
Y=df['Purchased']
print(Y)

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.25)
print(X_train.shape,Y_train.shape,X_test.shape,Y_test.shape)

SS=MinMaxScaler()
SS.fit(X_train)
X_train_siddhi=SS.transform(X_train)
SS.fit(X_test)
X_test_siddhi=SS.transform(X_test)

model=DecisionTreeClassifier()
model.fit(X_train_siddhi,Y_train)

Y_predict=model.predict(X_test_siddhi)

plt.scatter(X_test[Y_test==0]['Age'],X_test[Y_test==0]['EstimatedSalary'],c='red',alpha=0.7)

plt.scatter(X_test[Y_test==1]['Age'],X_test[Y_test==1]['EstimatedSalary'],c='blue',alpha=0.7)

plt.show()

print(model.score(X_test_siddhi,Y_test))
