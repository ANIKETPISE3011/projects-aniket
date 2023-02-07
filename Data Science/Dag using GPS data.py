import networkx as nx
import matplotlib.pyplot as plt
import sys
import os
import pandas as pd
sfilename='C:\DS\DATA SCIENCE\Retrive-Router-Location.csv'
sOutputFilename='Assess-Dag-Company-Gps.png'
print('loading:',sfilename)
print('##############################')
Companydata=pd.read_csv(sfilename,header=0,low_memory=False,encoding='latin-1')
print('loaded Company:',Companydata.columns.values)
print('####################################')
print(Companydata)
print('##########################################')
G=nx.Graph()
for i in range(Companydata.shape[0]):
    nLatitude=round(Companydata['Latitude'][i],1)
    nLongitude=round(Companydata['Longitude'][i],1)

if nLatitude<0:
    sLatitude=str(nLatitude*-1)+'S'
else:
    sLatitude=str(nLatitude)+'N'

if nLongitude<0:
    sLongitude=str(nLongitude*-1)+'W'
else:
    sLongitude=str(nLongitude)+'E'

sGPS=sLatitude+'-'+sLongitude
G.add_node(sGPS)
print('########################################')
for n1 in G.nodes():
    for n2 in G.nodes():
        if n1!=n2:
            print('Link:',n1,'TO',n2)
            G.add_edge(n1,n2)
print('##################################')
print('Nodes of graph:')
print(G.nodes())
print('Egdes of graph:')
print(G.edges())
print('############################################')
Base='C:\DS\DATA SCIENCE'
sfiledir=Base
if not os.path.exists(sfiledir):
    os.makedirs(sfiledir)
sfilename=sfiledir+'/'+sOutputFilename
print('###################################')
print('storing:',sfilename)
print('#########################################')
pos=nx.circular_layout(G,dim=2,scale=2)
nx.draw(G,pos=pos,node_color='r',edge_color='b',with_labels=True,node_size=4000,font_size=9)
plt.savefig(sfilename)
plt.show()
