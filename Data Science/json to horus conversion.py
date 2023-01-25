import pandas as pd

#here we are importing .json file and storing it into  variable
datafile='C:\\DS\\DATA SCIENCE\\Country_Code.json'
Data=pd.read_json(datafile,orient='index')
print('Data details \n:',Data.head())

#here we are going to drop some columns to make it simple
#it is impossible to drop more than one column at a time
Data.drop('ISO-2-CODE',axis=1,inplace=True)
Data.drop('ISO-3-Code',axis=1,inplace=True)
print('********************')
print('\n After dropping coumns:',Data.head(2))

#here are renaminng the column name
Data.rename(columns={'Country':'RCountry Name','ISO-M49':'RCountry Number'},inplace=True)
print('\n After renaming columns:',Data.head(2))

#here we are setting index column as country number
Data.set_index('RCountry Number',inplace=True)
print('***********************')
print('\n After setting index as RCountry Number:',Data.head(2))

#here we are sorting data of currencynumber
Data.sort_values('RCountry Number',inplace=True)
print('********************')
print('\n After sorting values \n',Data.head(2))

#here we are done with JSON to HORUS
print('\n JSON to HORUS IS DONE')
