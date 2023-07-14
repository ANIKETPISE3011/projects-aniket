import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
import nltk

df=pd.read_csv(r'C:\sem2\bda\prac\Tweets.csv')
df.head()
plot_size=plt.rcParams['figure.figsize']
print(plot_size[0])
print(plot_size[1])
plot_size[0]=8
plot_size[1]=6
plt.rcParams['figure.figsize']=plot_size

df.airline.value_counts().plot(kind='pie',autopct='%1.0f%%')
plt.show()
df.airline_sentiment.value_counts().plot(kind='pie',autopct='%1.0f%%',colors=['red','yellow','green'])
plt.show()
airline_sentiment=df.groupby(['airline','airline_sentiment']).airline_sentiment.count().unstack()
airline_sentiment.plot(kind='bar')
plt.show()

sns.barplot(x='airline_sentiment',y='airline_sentiment_confidence',data=df)
plt.show()
