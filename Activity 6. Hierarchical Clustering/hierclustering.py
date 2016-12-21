# -*- coding: utf-8 -*-

#Authors: Alberto Crespo Sánchez and Juan Alfredo García García

import codecs
import pandas as pd, numpy as np, matplotlib.pyplot as plt
import numpy
import csv


#http://docs.scipy.org/doc/scipy/reference/cluster.html
from scipy import cluster
from sklearn import preprocessing 
import sklearn.neighbors
from sklearn.decomposition import PCA


# 0. Load Data
f = codecs.open('../1-Data/Caracteristicas.csv', "r", "utf-8")
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
#http://scikit-learn.org/stable/modules/preprocessing.html
min_max_scaler = preprocessing.MinMaxScaler()
states = min_max_scaler.fit_transform(states)
        
#2. PCA Estimation
estimator = PCA (n_components = 2)
X_pca = estimator.fit_transform(states)
	
# 2. Compute the similarity matrix
dist = sklearn.neighbors.DistanceMetric.get_metric('euclidean')
matsim = dist.pairwise(states)
avSim = numpy.average(matsim)
print "%s\t%6.2f" % ('Distancia Media', avSim)

# 3. Building the Dendrogram	
# http://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html#scipy.cluster.hierarchy.linkage
clusters = cluster.hierarchy.linkage(matsim, method = 'ward')
# http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.cluster.hierarchy.dendrogram.html
cluster.hierarchy.dendrogram(clusters, color_threshold=0)
plt.show()

cut = 8

labels = cluster.hierarchy.fcluster(clusters, cut , criterion = 'distance')
print 'Number of clusters %d' % (len(set(labels)))


reader = csv.reader(open('../1-Data/Caracteristicas.csv', 'rb'))
archivo=open ('../1-Data/CaracteristicasC.csv',"a")
#archivo.write("Cluster, Numero de Accidentes por Cluster, Numero de accidentes por salida,  numero de accidentes por Alcance,  Numero de accidentes por Vuelco,  Numero de accidentes por tijera,  numero de accidentes por atropello,  Numero de accidentes por nivel Amarillo,  Numero de Accidentes por Nivel Blanco,  Numero de accidentes por nivel Negro,  Numero de accidentes por nivel Rojo")

x = 0
y = 0

for index,row in enumerate(reader):
	if x == 0:
		archivo.write(str(row[0])+","+str(row[1])+","+str(row[2])+","+str(row[3])+","+str(row[4])+","+str(row[5])+","+str(row[6])+","+str(row[7])+","+str(row[8])+","+str(row[9])+","+str(row[10])+",clusterC")
		archivo.write("\n")
		x = x + 1
	else:
		archivo.write(str(row[0])+","+str(row[1])+","+str(row[2])+","+str(row[3])+","+str(row[4])+","+str(row[5])+","+str(row[6])+","+str(row[7])+","+str(row[8])+","+str(row[9])+","+str(row[10])+","+str(labels[y]))
		archivo.write("\n")
		y = y +1

archivo.close()

Lista_accidentes = []
Lista_accidentes.append(0)
Lista_accidentes.append(0)
Lista_accidentes.append(0)
Lista_accidentes.append(0)
Lista_numero = []
Lista_numero.append(0)
Lista_numero.append(0)
Lista_numero.append(0)
Lista_numero.append(0)

a = 0

reader = csv.reader(open('../1-Data/CaracteristicasC.csv', 'rb'))
for index,row in enumerate(reader):
	if a > 0:
		if int(row[11]) == 1:
			Lista_accidentes[0] = Lista_accidentes[0] + int(row[1])
			Lista_numero[0] = Lista_numero[0] + 1
		if int(row[11]) == 2:
			Lista_accidentes[1] = Lista_accidentes[1] + int(row[1])
			Lista_numero[1] = Lista_numero[1] + 1
		if int(row[11]) == 3:
			Lista_accidentes[2] = Lista_accidentes[2] + int(row[1])
			Lista_numero[2] = Lista_numero[2] + 1	
		if int(row[11]) == 4:
			Lista_accidentes[3] = Lista_accidentes[3] + int(row[1])
			Lista_numero[3] = Lista_numero[1] + 1
	a = a + 1


Medias = []
Medias.append(int(Lista_accidentes[0]/Lista_numero[0]))
Medias.append(int(Lista_accidentes[1]/Lista_numero[1]))	
Medias.append(int(Lista_accidentes[2]/Lista_numero[2]))	
Medias.append(int(Lista_accidentes[3]/Lista_numero[3]))	




colors = numpy.array([x for x in 'bgrcmykbgrcmykbgrcmykbgrcmyk'])
colors = numpy.hstack([colors] * 20)



print("La media del numero de accidentes del Cluster 1 (Color: "+str(colors[1])+" ) es: "+str(Medias[0]))
print("La media del numero de accidentes del Cluster 2 (Color: "+str(colors[2])+" ) es: "+str(Medias[1]))
print("La media del numero de accidentes del Cluster 3 (Color: "+str(colors[3])+" ) es: "+str(Medias[2]))
print("La media del numero de accidentes del Cluster 4 (Color: "+str(colors[4])+" ) es: "+str(Medias[3]))

fig, ax = plt.subplots()
# ad-hoc
plt.xlim(-3, 1)
plt.ylim(-2, 1)

for i in range(len(X_pca)):
    plt.text(X_pca[i][0], X_pca[i][1], 'x', color=colors[labels[i]])  
    
ax.grid(True)
fig.tight_layout()
plt.show()


