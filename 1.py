import pandas as pd
import networkx as nx
import csv
import operator

data = pd.read_csv('F:/大三上/社群/qmza/當選.csv')

check = pd.read_csv('F:/大三上/社群/qmza/party表.csv')

G = nx.Graph()

for index in range(data.shape[0]):
    G.add_edge(data['Name'][index],data['Donater'][index])
    
common_neigh = [(e[0],e[1],len(list(nx.common_neighbors(G,e[0],e[1]))))for e in nx.non_edges(G)]
graph_data = sorted(common_neigh,key=operator.itemgetter(2),reverse=True)

with open('F:/大三上/社群/qmza/2.csv',mode='w',encoding='utf-8') as f:
    fieldnames = ['A','a-p', 'B','b-p','Weight']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()  
    for line in graph_data:
        for i in range(len(check)):
            if line[0]==check['Name'][i]:
                ap=check['Party'][i]
            if line[1]==check['Name'][i]:
                bp=check['Party'][i]
        if line[2]!=0:
            writer.writerow({'A':line[0],'a-p':ap,'B':line[1],'b-p':bp,'Weight':line[2]})
