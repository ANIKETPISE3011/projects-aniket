import pandas as pd
print('Averaging of data:\n')

sfilename='‪'C:\\DS\\DATA SCIENCE||IP_DATA_CORE.csv''
Data=pd.read_csv(sfilename,header=0)
print('Data details:\n',Data.head())
print('********************************')

#there are some many columns but we only have to use some columns
print('Only this columns we want from above columns:')
Data=pd.read_csv(sfilename,header=0,usecols=['Country','Place Name','Latitude','Longitude'])
print('\n',Data.head(2))
print('********************************')

#here we are renaming the column names
Data.rename(columns={'Place Name':'City Name'},inplace=True)
print('\n After Renaming the columns:', Data.head(2))
print('*******************************')

#By doing this we going to use only this columns
DataJod=Data[['Country', 'City Name', 'Latitude']]
print('\n ',DataJod.head(5))
print('*******************************')

#now here we are going to find mean of the latitude
#here we are using groupby()-- to group all the country and City Name , with the same name types
Meandata=DataJod.groupby(['Country','City Name'])['Latitude'].mean()
print('The mean of the data is ;\n',Meandata)
