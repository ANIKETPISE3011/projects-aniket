import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots()
xmin,xmax=-0.2,1.4
ymin,ymax=-0.1,1.1
X=np.arange(xmin,xmax,0.1)
ax.scatter(0,0,color='r')
ax.scatter(0,1,color='r')
ax.scatter(1,0,color='r')
ax.scatter(1,1,color='g')
ax.set_xlim([xmin,xmax])
ax.set_ylim([ymin,ymax])
m,c=-1,1.2
ax.plot(X,m*X+c)
plt.show()
