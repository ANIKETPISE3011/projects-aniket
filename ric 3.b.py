import numpy as np
import pandas as pd
import scipy.stats as stats

np.random.seed(10)
grade=np.random.choice(a=['O','A','B','C','D'],p=[0.20,0.20,0.20,0.20,0.20],size=100)
gen=np.random.choice(a=['Male','Female'],p=[0.5,0.5],size=100)
mscpart1=pd.DataFrame({'Grade':grade,'Gender':gen})
print(mscpart1)
tab=pd.crosstab(mscpart1.Grade,mscpart1.Gender,margins=True)
tab.columns=['Male','Female','row_totals']
tab.index=['O','A','B','C','D','col_totals']
observed=tab.iloc[0:5,0:2]
print(observed)
expected=np.outer(tab['row_totals'][0:5],tab.loc['col_totals'][0:2])/100
print(expected)
chi_squared_stat= (((observed-expected)**2)/expected).sum().sum()
print('Calculated:',chi_squared_stat)

crit=stats.chi2.ppf(q=0.95,df=4)
print('Table Vale:',crit)

if chi_squared_stat>=crit:
    print('HO is accepted')
else:
    print('HO is rejected')
                  
