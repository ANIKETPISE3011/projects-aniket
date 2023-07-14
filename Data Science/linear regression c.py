import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
df=pd.read_csv(r'C:\sem2\bda\prac\weightwaist.csv')
print(df)
#df.plot(kind='scatter', x='waist_cm',y='weight_kg',color='green',marker='*')
plt.xlabel('waist_cm')
plt.ylabel('weight_kg')
plt.scatter(df.waist_cm,df.weigt_kg,color='green',marker='*')
newdata=df.drop('weight_kg',axis=1)
model=linear_model.LinearRegression()
model.fit(newdata,df.weight_kg)
print(model.coef_)
print(model.intercept_)
print(model.score(newdata,df.weight_kg))
model=linear_model.LinearRegression()
model.fit(newdata.values,df.weight_kg.values)
prediction=model.predict([[98]])
print('Prediction for weight 98 is :',prediction)
plt.plot(df.waist_cm,model.predict(df.waist_cm.values.reshape(-1,1)),color='r')
plt.show()
