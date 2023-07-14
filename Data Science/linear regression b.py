import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

df=pd.read_csv(r'C:\sem2\bda\prac\canada_per_capita_income.csv')
print(df)
plt.xlabel('year')
plt.ylabel('income')
plt.scatter(df.year,df.income,color='black',marker='*')
newdata=df.drop('income',axis=1)
print(newdata)
print('prediction values')

model=linear_model.LinearRegression()
model.fit(newdata.values,df.income.values)
prediction=model.predict([[2050]])
print('prediction values',prediction)
plt.plot(df.year,model.predict(df.year.values.reshape(-1,1)),color='r')
plt.show()
