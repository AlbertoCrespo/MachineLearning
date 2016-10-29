# -*- coding: utf-8 -*-

#Authors: Alberto Crespo Sánchez and Juan Alfredo García García

import pandas as pd, numpy as np, matplotlib.pyplot as plt
import sklearn.cluster
from sklearn import metrics
from sklearn import cluster

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


spectral = cluster.SpectralClustering(n_clusters=5, eigen_solver='arpack', affinity="nearest_neighbors")
labels = spectral.fit_predict(data)
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)


#Print the Silohouette Coefficient, number of clusters and graphic clusters
sc= str("SC:%0.3f" % metrics.silhouette_score(np.asarray(data), labels))
print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(np.asarray(data), labels))
print('Numero de clusteres obtenidos: %d' % n_clusters_)
plotdata(data,labels,'SpectralClustering NC:'+str(n_clusters_)+' '+sc)