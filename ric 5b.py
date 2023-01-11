import pandas as pd
from statsmodels.stats import weightstats as stests
data='C:\\RIC\\blood_pressure.csv'
df= pd.read_csv(data)
df[['bp_before','bp_after']].describe()
print(df)
ztest,pval=stests.ztest(df['bp_before'],x2=df['bp_after'],value=0, alternative='two-sided')
print(float(pval))
if pval<0.05:
    print('reject null hypothesis')
else:
    print('accept null hypothesis')
