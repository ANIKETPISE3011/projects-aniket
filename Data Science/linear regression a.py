import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

df=pd.read_csv(r'C:\sem2\bda\prac\homeprices.csv')
print(df.head(3))
print(df.shape)

newdata=df.drop('price',axis=1)
print(newdata)

model=linear_model.LinearRegression()
model.fit(newdata,df.price)

area=pd.read_csv(r'C:\sem2\bda\prac\area.csv')
print(area)


pred=model.predict(area)
print(pred)

print(model.coef_)
print(model.intercept_)

plt.scatter(x='area',y='price',color='green',marker='*',data=df)
plt.plot(df.area,model.predict(df.area.values.reshape(-1,1)),color='red')
plt.show()
