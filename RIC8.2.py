import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)
#1000 random integers between 0 to 50
x = np.random.randint(0,50,1000)
#positive correlation with some noise
y=x + np.random.normal(0,10,1000)

np.corrcoef(x,y)
plt.style.use('ggplot')

plt.scatter(x,y)
plt.show()
