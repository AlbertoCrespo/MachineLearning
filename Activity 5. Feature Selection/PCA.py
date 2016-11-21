# -*- coding: utf-8 -*-

#Authors: Alberto Crespo Sánchez and Juan Alfredo García García


import codecs
import matplotlib.pyplot as plt
import numpy
from sklearn.decomposition import PCA
from sklearn import preprocessing 
import sklearn.cluster

# 0. Load Data
f = codecs.open("Caracteristicas.csv", "r", "utf-8")
states = []
count = 0
for line in f:
	if count > 0: 
		# remove double quotes
		row = line.replace ('"', '').split(",")
		row.pop(0)
		if row != []:
			data = [int(el) for el in row]
			states.append(data)
	count += 1

#1. Normalization of the data
min_max_scaler = preprocessing.MinMaxScaler()
states = min_max_scaler.fit_transform(states)
print states
        
#2. PCA Estimation
estimator = PCA (n_components = 2)
X_pca = estimator.fit_transform(states)
print X_pca

#3. k-means clustering
k = 3
centroids, labels, z =  sklearn.cluster.k_means(states, k, init="k-means++" )

#4.  plot 
colors = ['blue', 'red', 'green']
numbers = numpy.arange(len(X_pca))

fig, ax = plt.subplots()

for i in range(len(X_pca)):
    plt.text(X_pca[i][0], X_pca[i][1], 'x', color=colors[labels[i]])
   
plt.xlim(-2, 3)
plt.ylim(-0.8, 1)


ax.grid(True)
fig.tight_layout()

plt.show()