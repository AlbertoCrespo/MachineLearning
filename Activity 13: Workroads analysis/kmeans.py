# -*- coding: utf-8 -*-

#Authors: Alberto Crespo Sánchez and Juan Alfredo García García

import pandas as pd, numpy as np, matplotlib.pyplot as plt
import sklearn.cluster
from sklearn import metrics
from sklearn.cluster import KMeans
import csv



#Load data (latitude and longitude) of the province of Araba filtered by type: accident
df = pd.read_csv('../1-Data/Works2007Features.csv')
data = df.as_matrix(columns=['Numero de Obras por Cluster'])

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



#We write the results in a new CSV file
reader = csv.reader(open('../1-Data/Works2007Features.csv', 'rb'))
archivo=open ('../1-Data/Works2007FeaturesC.csv',"a")

x = 0
y = 0

for index,row in enumerate(reader):
	if x == 0:
		archivo.write(row[0]+","+row[1]+", cluster")
		archivo.write("\n")
	else:
		archivo.write(row[0]+","+row[1]+","+str(labels[y]))
		archivo.write("\n")
		y = y + 1
	x = x + 1

archivo.close()