from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('C:\RIC\blood_pressure.csv')
print(df[['bp_before','bp_after']].descirbe())
df[['bp_before','bp_after']].plot(kind='box')
plt.savefig('boxplot_outliers.png')
df['bp_difference']=df['bp_before']-df['bp_after']
df['bp_diffrence'].plot(kind='hist',title='Blood pressure difference Histogram')
plt.savefig('blodd pressure difference histogram.png')
stats.probplot(df['bp_diffrence'],plot=plt)
plt.title('blood presure difference Q-Q plot')
plt.savefig('blood pressure diffrence qq plot.png')
stats.shapiro(df['bp_diffrence'])
stats.ttest_rel(df['bp_before'],df['bp_after''])