import pandas as pd
print('part-1:\n')
print('Droping the columns where all the values are missing :\n')
print('**************************************************')
#import the data file.
sfilename='C:\\DS\\DATA SCIENCE\\GOOD-or-BAD.csv'
Data=pd.read_csv(sfilename,header=0)
#here we are droping the null columns by using dropna() function.
print('This is the Good or bad data details: \n',Data.head(5))
testdata=Data.dropna(axis=1,how='all')
print('Data after droping the null columns i.e Field E : \n\n',testdata.head(5))


print('*************************************************************************************')
print('part-2:\n')
print('Drop the columns with any missing values:\n')
#here we are importing data
sfilename1='C:\\DS\\DATA SCIENCE\\GOOD-or-BAD.csv'
Data1=pd.read_csv(sfilename1,header=0)
print('This is the good or bad data details: \n',Data1.head(5))
#here we are droping the columns contaning missing values
testdata1=Data1.dropna(axis=1,how='any')
print('Data after droping the columns with any missing values:\n',testdata1.head(5))


print('***************************************************************************')
print('part-3:\n')
print('Keeping the only rows that contain maximum two missing values:\n')
print('***********************')
#here we are importing data
sfilename2='C:\\DS\\DATA SCIENCE\\GOOD-or-BAD.csv'
Data2=pd.read_csv(sfilename2,header=0)
print('This the good or bad data details:\n',Data2.head(12))
#here we are droping the rows which are having more than two missing values.
testdata2=Data2.dropna(axis=0, thresh=6)
print('********************************')
print('Data after droping the rows containing maximum of two missing values\n',testdata2.head())
