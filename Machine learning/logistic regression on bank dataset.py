import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
plt.rc('font',size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
df=pd.read_csv(r'C:\DS\DATA SCIENCE\bank-full.csv',sep=';',header=0)
print(df.head())
print(df.shape)
print(list(df.columns))
df=df.dropna()
data=pd.get_dummies(df,columns=['job','marital','default','housing','loan','poutcome'])
print(data.head())
print(data.columns)
data.drop(data.columns[[0,1,2,3,4,5,6,7,8,9,10,11,12,16,  18,  21,  24]],axis=1,inplace=True)
X=data.iloc[:,1:]
Y=data.iloc[:,0]
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=0)
classifier=LogisticRegression(solver='lbfgs',random_state=0)
classifier.fit(X_train,Y_train)
predicted_y=classifier.predict(X_test)
print(predicted_y)
for x in range(len(predicted_y)):
    if (predicted_y[x]==1):
        print(x,end='\t')
print('Accuracy:{:.2f}'.format(classifier.score(X_test,Y_test)))