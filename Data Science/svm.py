import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv(r'C:\sem2\bda\prac\social.csv')
print(df)
x=df.iloc[:,[2,3]]
y=df.iloc[:,4]
print(x)
print(y)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)

print('training data',x_train)
print('testing data',x_test)

from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
x_train=ss.fit_transform(x_train)
x_test=ss.fit_transform(x_test)

from sklearn.svm import SVC
model=SVC(kernel='linear',random_state=0)
model=model.fit(x_train,y_train)

y_pred=model.predict(x_test)
print('predicyion',y_pred)

from sklearn import metrics
print(metrics.accuracy_score(y_test,y_pred))
