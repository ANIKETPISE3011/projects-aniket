import pandas as pd
# here we are importing the file and storing it into variable
datafile='C:\DS\DATA SCIENCE\Country_code.csv'
data= pd.read_csv(datafile,header=0)
print('data details:',data.head())

# here we are going to drop some column to make it simple
#it is not possible to drop more than one column at a time
data.drop('ISO-2-CODE',axis=1,inplace= True)
data.drop('ISO-3-Code',axis=1, inplace= True)
print('******************************************')
print('\n After droping the columns:', data.head(2))

# here we are renaming some column name
data.rename(columns={'Country':'RCountry Name', 'ISO-M49':'RCountry Number'},inplace= True)
print('\n After renaming the columns: \n',data.head(2))

# here we are setting index columns as country number
data.set_index('RCountry Number', inplace=True)
print('*******************************************')
print('\n After setting index as RCountry NUmber\n:',data.head(2))

#here we are sorting the data by currencyNumber
data.sort_values('RCountry Name',inplace=True)
print('*********************************************')
print('\n After sorting values\n:',data.head())

soutput='C:\DS\DATA SCIENCE\HORUS-CSV-Country.csv'
outputdata=data
outputdata.to_csv(soutput,index=False)

# here we have done with CSV to HORUS
print('\n CSV to HORUS IS DONE')
