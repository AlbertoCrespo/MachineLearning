# -*- coding: utf-8 -*-

#Authors: Alberto Crespo Sánchez and Juan Alfredo García García

import pandas as pd, numpy as np, matplotlib.pyplot as plt
import sklearn.cluster
from sklearn import metrics
from sklearn.cluster import KMeans
import csv



#Load data Number Accident with Zone
df = pd.read_csv('../1-Data/Caracteristicas.csv')
data = df.as_matrix(columns=['Numero de Accidentes por Cluster'])


# 2. Setting parameters (ad-hoc)
k = 3 # number of clusters
init = 'random' # initialization method 
iterations = 10 # to run 10 times with different random centroids to choose the final model as the one with the lowest SSE
max_iter = 300 # maximum number of iterations for each single run
tol = 1e-04 # controls the tolerance with regard to the changes in the within-cluster sum-squared-error to declare convergence
random_state = 0 # random

# 3. Clustering execution
km = KMeans(k, init, n_init = iterations ,max_iter= max_iter, tol = tol,random_state = random_state)
labels= km.fit_predict(data)


#Write Results
reader = csv.reader(open('../1-Data/Caracteristicas.csv', 'rb'))
archivo=open ("../1-Data/FeaturesClass.csv","a")

x = 0
y = 0

for index,row in enumerate(reader):
	if x == 0:
		archivo.write(str(row[0])+","+str(row[1])+","+str(row[2])+","+str(row[3])+","+str(row[4])+","+str(row[5])+","+str(row[6])+","+str(row[7])+","+str(row[8])+","+str(row[9])+","+str(row[10])+",Class")
		archivo.write("\n")
		x = x + 1
	else:
		archivo.write(str(row[0])+","+str(row[1])+","+str(row[2])+","+str(row[3])+","+str(row[4])+","+str(row[5])+","+str(row[6])+","+str(row[7])+","+str(row[8])+","+str(row[9])+","+str(row[10])+","+str(labels[y]))
		archivo.write("\n")
		y = y +1

archivo.close()