# -*- coding: utf-8 -*-

#Authors: Alberto Crespo Sánchez and Juan Alfredo García García

import pandas as pd, numpy as np, matplotlib.pyplot as plt
import sklearn.cluster
from sklearn import metrics
from sklearn.mixture import GMM

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
df = pd.read_csv('../1-Data/incidentsarabaporaccidente.csv')
data = df.as_matrix(columns=['latitud', 'longitud'])


classifier = GMM(n_components=5,covariance_type='full', init_params='wc', n_iter=20)
classifier.fit(data)
labels =  classifier.predict(data)
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)


#Print the Silohouette Coefficient, number of clusters and graphic clusters
sc= str("SC:%0.3f" % metrics.silhouette_score(np.asarray(data), labels))
print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(np.asarray(data), labels))
print('Numero de clusteres obtenidos: %d' % n_clusters_)
plotdata(data,labels,'EM NC:'+str(n_clusters_)+' '+sc)