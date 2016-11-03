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

def contar_veces(elemento, lista):
	veces = 0
	for i in lista:
		if elemento == i:
			veces += 1
	return veces


#Load data (latitude and longitude) of the province of Araba filtered by type: accident
df = pd.read_csv('incidentsarabaporaccidente.csv')
data = df.as_matrix(columns=['latitud', 'longitud'])

#reader = csv.reader(open('incidentsarabaporaccidente.csv', 'rb'))
archivo=open ("R.csv","a")
archivo.write("Clusters,Numero_de_Accidentes")
archivo.write("\n")


minPts=5
eps = 0.003

labels = sklearn.cluster.DBSCAN(eps,minPts).fit_predict(data)



for l in labels:
	archivo.write(str(l))
	archivo.write("\n")



#labels1 = labels
#labels1.sort()

'''lista_nueva = []
for i in labels1:
	if i not in lista_nueva:
		lista_nueva.append(i)
labels1 = lista_nueva


Numero_de_Accidentes_por_cluster = []

for i in labels1:
	Numero_de_Accidentes_por_cluster.append(contar_veces(i, labels))


#Distintas_Causas = []

#for index,row in enumerate(reader):
	#causa = row[4]
	#if causa not in Distintas_Causas:
		#Distintas_Causas.append(causa)

#Contador_Causas = []		
#for c in Distintas_Causas:
	#for i in labels:






x = 0
for i in labels1:
	archivo.write(str(i)+","+str(Numero_de_Accidentes_por_cluster[x]))
	archivo.write("\n")
	x = x + 1'''

archivo.close()
