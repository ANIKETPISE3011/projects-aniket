import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
features,true_labels=make_blobs(n_samples=200,centers=3,cluster_std=2.75,random_state=42,)
scaler=StandardScaler()
scaled_features=scaler.fit_transform(features)
print('Feartures: \n',features[:5])
print('True LABELS: \n',true_labels[:5])
print('SCALED FEATURES: \n',scaled_features[:5])
kmeans=KMeans(init='random',n_clusters=3,n_init=10,max_iter=300,random_state=42)
kmeans.fit(scaled_features)
#The lowest SSE value
print('K-means Inertia=',kmeans.inertia_)
#Final location of the centroid
print('CWENTERS:',kmeans.cluster_centers_)
print('K-Means Label:',kmeans.labels_[:5])