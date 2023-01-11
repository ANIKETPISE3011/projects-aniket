import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)
#1000 random integers between o and 50
x=np.random.randint(0,50,1000)

#negative correlation with some noise
y=100-x+np.random.normal(0,5,1000)

np.corrcoef(x,y)
plt.scatter(x,y)
plt.show()
