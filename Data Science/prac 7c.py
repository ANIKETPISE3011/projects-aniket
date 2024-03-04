from sklearn import datasets
from sklearn.cluster import KMeans

iris_df=datasets.load_iris()

model=KMeans(n_clusters=3)

model.fit(iris_df.data)

pred=model.predict([[1.6,7.8,6.9,1.4]])
ypred=model.predict(iris_df.data)

print(pred)
print(ypred)
