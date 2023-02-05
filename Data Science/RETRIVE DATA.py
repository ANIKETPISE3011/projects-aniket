import sys
import os
import pandas as pd
Base='C:\DS'
sFileName='C:\DS\DATA SCIENCE\IP_DATA_ALL.csv'
print('Loading:',sFileName)
IP_DATA_ALL=pd.read_csv(sFileName,header=0,low_memory=False,encoding='latin-1')
sFileDir=Base+'/DATA SCIENCE'
if not os.path.exists(sFileDir):
    os.makedirs(sFileDir)
print('Rows:',IP_DATA_ALL.shape[0])
print('Columns:',IP_DATA_ALL.shape[1])
print('###RAW DATA SET###############################')
for i in range(0,len(IP_DATA_ALL.columns)):
    print(IP_DATA_ALL.columns[i],type(IP_DATA_ALL.columns[i]))
print('### FIXED DATA SET ################################')
IP_DATA_ALL_FIX=IP_DATA_ALL
for i in range(0,len(IP_DATA_ALL.columns)):
    cNameOld=IP_DATA_ALL_FIX.columns[i]+' '
    cNameNew=cNameOld.strip().replace(" ",".")
    IP_DATA_ALL_FIX.columns.values[i]=cNameNew
    print(IP_DATA_ALL.columns[i],type(IP_DATA_ALL.columns[i]))
print(IP_DATA_ALL_FIX.head())
print('Fixed data set with ID')
IP_DATA_ALL_with_ID=IP_DATA_ALL_FIX
IP_DATA_ALL_with_ID.index.names=['RowID']
print(IP_DATA_ALL_with_ID.head())
sFileName2=sFileDir+'/Retrive_IP_DATA.csv'
IP_DATA_ALL_with_ID.to_csv(sFileName2,index=True,encoding='latin-1')
print('###DONE##############################')
