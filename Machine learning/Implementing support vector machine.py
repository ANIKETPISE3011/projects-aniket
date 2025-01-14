from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import plot_confusion_matrix
#Configuration options
blobs_random_seed=42
centers=[(0,0),(5,5)]
clusters_std=1
frac_test_split=0.33
num_features_for_samples=2
num_samples_total=1000
#genetics data
inputs,targets=make_blobs(n_samples=num_samples_total,centers=centers,n_features=num_features_for_samples,cluster_std=clusters_std)
X_train,X_test,y_train,y_test=train_test_split(inputs,targets,test_size=frac_test_split,random_state=blobs_random_seed)
#Save and load temporarily
# np.save('./data.npy',(X_train,X_test,y_train,y_test))
X_train,X_test,y_train,y_test=np.load('./data.npy',allow_pickle=True)
#Generate scatter plot for traning data
plt.scatter(X_train[:,0],X_train[:,1])
plt.title('Linearly separable data')
plt.xlabel('X1')
plt.ylabel('X2')
plt.show()
#Initialize SVM classifier
clf=svm.SCV(kernel='Linear')
#Fit data
clf=clf.fit(X_train,y_train)
#predictions the test set
predictions=clf.predict(X_test)
#Generate confusion matrix
matrix=plot_confusion_matrix(clf,X_test,y_test,cmap=plt.cm.Blues,normalizes='true')
plt.title('Confusion matrix for our classifier')
plt.show()
support_vectors=clf.support_vectors_
plt.scatter(X_train[:,0],X_train[:,1])
plt.scatter(support_vectors[:,0],support_vectors[:,1],color='red')
plt.title('Linearly separable data with support vectors')
plt.xlabel('X1')
plt.ylabel('X2')