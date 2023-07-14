from numpy import unique
from numpy import where
from sklearn.datasets import make_classification
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

X,_ =make_classification(n_samples=1000,n_features=2,n_informative=2,n_redundant=0,
                         n_clusters_per_class=1,random_state=4)
model=KMeans(n_clusters=2)
model.fit(X)

y_pred=model.predict(X)

clusters=unique(y_pred)

for cluster in clusters:
    row=where(y_pred==cluster)
    plt.scatter(X[row,0],X[row,1])
plt.show()
