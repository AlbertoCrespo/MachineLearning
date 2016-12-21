# -*- coding: utf-8 -*-

#Authors: Alberto Crespo Sánchez and Juan Alfredo García García

import pandas as pd, numpy as np, matplotlib.pyplot as plt
import sklearn.cluster
import csv
from sklearn import metrics

from sklearn.cluster import DBSCAN



#Load data (latitude and longitude) of the province of Araba filtered by type: accident
df = pd.read_csv('../1-Data/incidentsarabaporaccidente.csv')
data = df.as_matrix(columns=['latitud', 'longitud'])

reader = csv.reader(open('../1-Data/incidentsarabaporaccidente.csv', 'rb'))
archivo=open ('../1-Data/incidentsarabaporaccidenteC.csv',"a")



minPts=5
eps = 0.003

labels = sklearn.cluster.DBSCAN(eps,minPts).fit_predict(data)

x = 0
y = 0
for index,row in enumerate(reader):
	if x == 0:
		archivo.write(str(row[0])+","+str(row[1])+","+str(row[2])+","+str(row[3])+","+str(row[4])+","+str(row[5])+","+str(row[6])+","+str(row[7])+","+str(row[8])+","+str(row[9])+","+str(row[10])+","+str(row[11])+","+str(row[12])+","+str(row[13])+",cluster")
		archivo.write("\n")
		x = x + 1
	else:
		archivo.write(str(row[0])+","+str(row[1])+","+str(row[2])+","+str(row[3])+","+str(row[4])+","+str(row[5])+","+str(row[6])+","+str(row[7])+","+str(row[8])+","+str(row[9])+","+str(row[10])+","+str(row[11])+","+str(row[12])+","+str(row[13])+","+str(labels[y]))
		archivo.write("\n")
		y = y +1


archivo.close()
