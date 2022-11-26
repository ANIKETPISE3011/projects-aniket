import pandas as pd
#here we are importing .csv file and storing it into a variable
datafile='C:\\DS\\DATA SCIENCE\\Country_code.csv'
Data=pd.read_csv(datafile,header=0)
print('data detail: \n',Data.head())

#here we are going to drop some columns to make it simple
#its impossible to more than one column at a time
Data.drop('ISO-2-CODE',axis=1,inplace=True)
Data.drop('ISO-3-Code',axis=1,inplace=True)
print('*******************')
print('\n After droping columns : \n',Data.head(2))

#here we are going to rename some column name
Data.rename(columns={'Country':'RCountry Name','ISO-M49':'RCountry Number'},inplace=True)
print('\n After renaming columns:',Data.head(2))

# here we are setting index as country number
Data.set_index('RCountry Number',inplace=True)
print('*************************')
print('\n After setting index :',Data.head(2))

#here we are sorting data by CurrencyNumber
Data.sort_values('RCountry Name',inplace=True)
print('*************************')
print('\n After sorting the Values:',Data.head(2))

#here we are done with csv to horus
print('\n CSV to HORUS is DONE')
