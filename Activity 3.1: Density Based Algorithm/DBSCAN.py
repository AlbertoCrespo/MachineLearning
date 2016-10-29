# -*- coding: utf-8 -*-

#Authors: Alberto Crespo Sánchez and Juan Alfredo García García

import pandas as pd, numpy as np, matplotlib.pyplot as plt
import sklearn.cluster
from sklearn import metrics

from sklearn.cluster import DBSCAN


#Method for Paint results algorithm
def plotdata(data,labels,name): 
#colors = ['black']
    fig, ax = plt.subplots()
    plt.scatter([row[0] for row in data], [row[1] for row in data], c=labels)
    ax.grid(True)
    fig.tight_layout()
    plt.title(name)
    plt.show()


#Load data (latitude and longitude) of the province of Araba filtered by type: accident
df = pd.read_csv('incidentsarabaporaccidente.csv')
data = df.as_matrix(columns=['latitud', 'longitud'])

#Represent the original data
labels = [0 for x in range(len(data))]
plotdata(data,labels,'basic')


#Parameterization with Euclidean metric
dist = sklearn.neighbors.DistanceMetric.get_metric('euclidean')
matsim = dist.pairwise(data)

#The certificate chart to find appropriate values for eps Variable
minPts=5
from sklearn.neighbors import kneighbors_graph
A = kneighbors_graph(data, minPts, include_self=False)
Ar = A.toarray()

seq = []
for i,s in enumerate(data):
    for j in range(len(data)):
        if Ar[i][j] != 0:
            seq.append(matsim[i][j])
            
seq.sort()
plt.plot(seq)
plt.show()


eps = 0.003

#DBSCAN Algorithm and number of clusters
labels = sklearn.cluster.DBSCAN(eps,minPts).fit_predict(data)
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)




#Print the Silohouette Coefficient, number of clusters and graphic clusters
print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(np.asarray(data), labels))
print('Numero de clusteres obtenidos: %d' % n_clusters_)
plotdata(data,labels, 'dbscan')