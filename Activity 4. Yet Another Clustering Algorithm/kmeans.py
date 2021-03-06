# -*- coding: utf-8 -*-

#Authors: Alberto Crespo Sánchez and Juan Alfredo García García

import pandas as pd, numpy as np, matplotlib.pyplot as plt
import sklearn.cluster
from sklearn import metrics
from sklearn.cluster import KMeans

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

# 2. Setting parameters (ad-hoc)
k = 5 # number of clusters
init = 'random' # initialization method 
iterations = 10 # to run 10 times with different random centroids to choose the final model as the one with the lowest SSE
max_iter = 300 # maximum number of iterations for each single run
tol = 1e-04 # controls the tolerance with regard to the changes in the within-cluster sum-squared-error to declare convergence
random_state = 0 # random

# 3. Clustering execution
km = KMeans(k, init, n_init = iterations ,max_iter= max_iter, tol = tol,random_state = random_state)
labels= km.fit_predict(data)

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)


#Print the Silohouette Coefficient, number of clusters and graphic clusters
sc= str("SC:%0.3f" % metrics.silhouette_score(np.asarray(data), labels))
print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(np.asarray(data), labels))
print('Numero de clusteres obtenidos: %d' % n_clusters_)
plotdata(data,labels,'KMeans NC:'+str(n_clusters_)+' '+sc)