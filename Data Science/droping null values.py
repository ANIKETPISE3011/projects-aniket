import pandas as pd
print('droping the columns where all the values are missing :\n')
sfilename='C:\DS\DATA SCIENCE\GOOD-or-BAD.csv'
data=pd.read_csv(sfilename, header=0)
print('This is the good and bad data details:',data.head(5))
testdata=data.dropna(axis=1,how='all')
print('***********************************************')
print('Data after droping the columns i.e. Field E :\n\n',testdata.head(5))
data1=pd.read_csv(sfilename,header=0)
print('This is the good and bad data details:',data1.head(11))
testdata1=data1.dropna(axis=1,how='any')
print('*********************************************************')
print('after droping the columns contaning any null values \n:',testdata1.head(11))
data2=pd.read_csv(sfilename,header=0)
print('This is the good and bad data details:',data2.head(12))
testdata2=data2.dropna(axis=0, thresh=6)
print('*************************************************')
print('After dropin  the null values of rows :\n',testdata2.head(12))
