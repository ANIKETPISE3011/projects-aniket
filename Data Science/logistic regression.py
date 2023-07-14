from sklearn.datasets import make_classification
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import pandas as pd

x,y=make_classification(n_samples=100,n_features=1,n_classes=2,n_clusters_per_class=1,flip_y=0.03,n_informative=1,n_redundant=0,n_repeated=0)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=1)
print(x_train.shape,y_train.shape,x_test.shape,y_test.shape)

lr=LogisticRegression()
lr.fit(x_train,y_train)

lr.coef_
lr.intercept_
print(lr.score(x_train,y_train))

y_pred=lr.predict(x_test)
print('predicted value:',y_pred)

print(confusion_matrix(y_test,y_pred))

plt.scatter(x,y,c=y,cmap='rainbow')
plt.title('Scatter plot of logistic Regression')
plt.show()
