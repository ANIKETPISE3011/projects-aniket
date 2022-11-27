import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import os

print('Buliding a directed acyclic graph:\n')
sfilename='C:\DS\DATA SCIENCE\Retrieve_Router_Location.csv'
Data=pd.read_csv(sfilename,header=0)
print('Retive Router Location data details :\n', Data.head(2))
#throws the number of rows
print(Data.shape[0])
#here we are looking of concatcention example which is used furthur
Placename=Data['Place_Name'] [1]+'-'+Data['Country'][1]
print('Concatenating:PlaceName and Country:\n',Placename,'\n')

#from here graph come into the picture
G1=nx.DiGraph()
G2=nx.DiGraph()
for i in range(Data.shape[0]):
    G1.add_node(Data['Country'][i])
    Placename=Data['Place_Name'][i]+'-'+Data['Country'][i]

#from here frist graph constructed
for i in G1.nodes():
    for j in G1.nodes():
        if i!=j:
            print('Link:', i,'to', j)
            G1.add_edge(i,j)
print('\n Nodes of the graph:\n',G1.nodes())
print('Edges of the graph: \n',G1.nodes())
nx.draw(G1,node_color='yellow',edge_color='blue',with_labels=True,node_size=500,font_size=12)
plt.show()
      
