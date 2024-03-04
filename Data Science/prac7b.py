from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

diabetes=datasets.load_diabetes()

print(diabetes)
diabetes_x=diabetes.data[:,np.newaxis,2]

x_train=diabetes_x[:-20]
x_test=diabetes_x[-20:]
y_train=diabetes.target[:-20]
y_test=diabetes.target[-20:]


lr=LinearRegression()
lr.fit(x_train,y_train)


ypred=lr.predict(x_test)
print(ypred)

plt.scatter(x_test,y_test,color='black')
plt.plot(x_test,ypred,color='red',linewidth=1)
plt.show()
