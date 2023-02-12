from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,confusion_matrix
import numpy as np
# array of consecutive equally_spaced values within a given range
x=np.arange(10).reshape(-1,1)
# have a value for each observation in x
y=np.array([0,0,0,0,1,1,1,1,1,1])
model=LogisticRegression()
model.fit(x,y)
print('model.classes_=',model.classes_)
print('model.intercept=',model.intercept_)
print('model.coef=',model.coef_)
# to get matrix of probabilities that the predicted output is equal to zero:1-p(x) or one p(x)
p_pred=model.predict_proba(x)
y_pred=model.predict(x) # predict y values
score_=model.score(x,y)# accuracy of the model
conf_m=confusion_matrix(y,y_pred)
# to get a more comprehensive report on the classifiaction
report= classification_report(y,y_pred)
print('p_pred:',p_pred)
print('y_pred:',y_pred)
print('Accuracy-ratio of the number of correct predictions to the number of observation=',score_)
print('conf_m:',conf_m)
print('report:',report)
