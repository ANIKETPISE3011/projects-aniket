import pandas as pd
print('filling the missing field with the mean, mode, median,max,min:\n')
print('******************************************')
sfilename='C:\\DS\\DATA SCIENCE\\GOOD-or-BAD.csv'
sfilenameM='C:\\DS\\DATA SCIENCE\\GOOD-or-BAD.csv'
sfilenameMDN='C:\\DS\\DATA SCIENCE\\GOOD-or-BAD.csv'
sfilenameMD='C:\\DS\\DATA SCIENCE\\GOOD-or-BAD.csv'
sfilenameMAX='C:\\DS\\DATA SCIENCE\\GOOD-or-BAD.csv'
sfilenameMIN='C:\\DS\\DATA SCIENCE\\GOOD-or-BAD.csv'
data=pd.read_csv(sfilename,header=0)
print('data details with the missing values:', data.head())
print('***************************************')
print('field is missing filled with mena value:\n')
dataM=pd.read_csv(sfilenameM,header=0)
testdataM=dataM.fillna(dataM.mean(numeric_only=True))
print(testdataM.head())
print('*******************************************')
print('field is missing filled with median value :\n')
dataMDN=pd.read_csv(sfilenameMDN,header=0)
testdataMDN=dataMDN.fillna(dataMDN.median(numeric_only=True))
print(testdataMDN.head())
print('******************************************')
print('field is missing filled with mode value  :\n')
dataMD=pd.read_csv(sfilenameMD,header=0)
testdataMD=dataMD.fillna(dataMD.mode(numeric_only=True))
print(testdataMD.head())
print('*******************************************')
print('field is missing filled with max value:\n')
dataMAX=pd.read_csv(sfilenameMAX,header=0)
testdataMAX=dataMAX.fillna(dataMAX.max(numeric_only=True))
print(testdataMAX.head())
print('******************************************')
print('field is missing filled with min value:\n')
dataMIN=pd.read_csv(sfilenameMIN,header=0)
testdataMIN=dataMIN.fillna(dataMIN.min(numeric_only=True))
print(testdataMIN.head())
                           
                           
                           
