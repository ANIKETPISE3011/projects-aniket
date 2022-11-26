import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

print('data binning or bucketing ''HISTOGRAM'': \n')
#random.seed()--we know that randit() generates the random number to fix
#the generation of the number as constant at each time we use this function
np.random.seed()

#here we are generating some random data to plot histogram
mu=90
sigma=25
x=mu+sigma*np.random.randn(5000)
num_bins=20

n,bins,patches=plt.hist(x,num_bins,density=1,ec='red')

#to obtain probability density function for norm
y=stats.norm.pdf(bins,mu,sigma)
plt.plot(bins,y,"")

#giving the name of X,Y axis and title to histogram
STitle='Histogram 5000 Entries into 20 Bins : mu=90 , sigma=25'
plt.title(STitle)
plt.xlabel('Example Data')
plt.ylabel('Probability Density')
plt.show()
