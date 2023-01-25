import pandas as  pd
print('Averaging of data :')

sfilename='C:\DS\DATA SCIENCE\IP_DATA_CORE.csv'
data=pd.read_csv(sfilename, header=0)
print('Data details \n:',data.head(2))
print('**************************')
#there are so many columns bur we want to use only few columns
print('Only this columns but we wants from the above columns:')
data=pd.read_csv(sfilename,header=0,usecols=['Country','Place Name', 'Latitude','Longitude'])
print('\n',data.head(2))
print('**********************************')

#here we are changing place name
data.rename(columns={'Place Name':'Jagha Name'},inplace=True)
print('\n After renaming: \n',data.head(2))
print('************************************')

#by doing so we can use only this column
Alldata=data[['Country','Jagha Name','Latitude']]
print('\n',Alldata.head(5))
print('*************************************')

#now here we are going to perform mean of the latitude
#here use of gropuby() to group all the country and jagha name, with  the same name type
meandata=Alldata.groupby(['Country','Jagha Name',])['Latitude'].mean()
print('The mean of the datais :\n',meandata)
