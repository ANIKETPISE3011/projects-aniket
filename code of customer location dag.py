import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import os

print('building a code for customer location dag:\n')
#here we are importing data.
sfilename='C:\\DS\\DATA SCIENCE\\Retrieve_Router_Location.csv'
Data=pd.read_csv(sfilename,header=0)
print('Retrieve Router Location Data details:|n',Data.head(2))
print(Data.shape[0])
# here we are concatenating the data placename and country name.
Placename=Data['Place_Name'][1]+'-'+Data['Country'][1]
print('Concatenating:PlaceName and Country:\n',Placename,'\n')
#here we are drawing the graph.
G1=nx.DiGraph()
G2=nx.DiGraph()
for i in range (Data.shape[0]):
    Placename=Data['Place_Name'][i]+'-'+Data['Country'][i]
    G2.add_node(Placename)

for i in G2.nodes():
    for j in G2.nodes():
        print('Link:',i,'to',j)
        G2.add_edge(i,j)
print('\nNodes of the graph :\n',G2.nodes())
print('Edges of the graph :\n',G2.edges())
nx.draw(G2,node_color='b',edge_color='g',with_labels=True,node_size=1000,font_size=8)
plt.show()
