import pandas as pd
sfilename='C:\DS\DATA SCIENCE\IP_DATA_CORE.csv'
print('loading:',sfilename)
IP_DATA_ALL=pd.read_csv(sfilename,header=0,low_memory= False,usecols=['Country','Place Name','Latitude','Longitude'],encoding='latin-1')
IP_DATA_ALL.rename(columns={'Place Name':'Place_Name'},inplace=True)
london_data=IP_DATA_ALL.loc[IP_DATA_ALL['Place_Name']=='London']
alldata=london_data[['Country','Place_Name','Latitude']]
print('Alldata:',alldata)
meandata=alldata.groupby(['Country','Place_Name'])['Latitude'].mean()
stddata=alldata.groupby(['Country','Place_Name'])['Latitude'].std()
print('Outliners:\n')
upperbound=float(meandata+stddata)
print('Higher than:',upperbound)
outlinerhigher=alldata[alldata.Latitude>upperbound]
print(outlinerhigher)
lowerbound=float(meandata-stddata)
print('Lower than:',lowerbound)
outlinerlower=alldata[alldata.Latitude<lowerbound]
print(outlinerlower)
print('not Outliner:')
outlinernot=alldata[(alldata.Latitude>=lowerbound)&(alldata.Latitude<=upperbound)]
print(outlinernot)
