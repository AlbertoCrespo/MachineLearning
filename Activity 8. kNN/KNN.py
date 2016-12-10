# -*- coding: utf-8 -*-

#Authors: Alberto Crespo Sánchez and Juan Alfredo García García

import pandas as pd, numpy as np, matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import random
import csv
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets



#Method to calculate the error at the time of predicting
def CalculateError(Z,test):
	x =  0
	for i in range(len(test)):
		if (test[i] != Z[i]):
			x = x + 1
	e = float(float(x)/float(len(test)))
	return e


#Reading the initial data
df = pd.read_csv('incidentsarabaaccidentC.csv')
data = df.as_matrix(columns=['latitud', 'longitud','cluster'])


#Division of original data to train and predict
trainingX = []
trainingY = []
testX = []
testY = []

for i in range(len(data)):
	if (random.uniform(0, 1) < 0.6):
		trainingX.append([data[i][0],data[i][1]])
		trainingY.append(data[i][2])
	else:
		testX.append([data[i][0],data[i][1]])
		testY.append(data[i][2])



errorres = []

#Algorithm Training ,Prediction and storage of errors
for n_neighbors in range(1, 123):
	clf = neighbors.KNeighborsClassifier(n_neighbors, weights='distance')
	clf.fit(trainingX, trainingY)
	Z = clf.predict(testX)
	errorres.append(CalculateError(Z,testY))


#It shows the graph with the errors made to predict in each K

plt.title('Error Curve')
plt.ylabel('Error')
plt.xlabel('K')
plt.xlim(0, 122)
plt.plot(errorres)
plt.show()



#Based on the graph, we introduce the best K that will be the highest and that has produced the least errors
K = int(input("Best K:"))


#We train the algorithm with all the data and the best K selected
trainingXT = []
trainingYT = []

for i in range(len(data)):
	trainingXT.append([data[i][0],data[i][1]])
	trainingYT.append(data[i][2])


clf = neighbors.KNeighborsClassifier(K, weights = 'distance')
clf.fit(trainingXT, trainingYT)



#We read the data of incidents of type "Works" of the province of Araba
df = pd.read_csv('incidentsarabaworks.csv')
data = df.as_matrix(columns=['latitud', 'longitud'])

data_works = []

for i in range(len(data)):
	data_works.append([data[i][0],data[i][1]])


#With the algorithm trained previously we predict the cluster to which it belongs
Z = clf.predict(data_works)


#We write the results in a new CSV file
reader = csv.reader(open('incidentsarabaworks.csv', 'rb'))
archivo=open ("incidentsarabaworksC.csv","a")

x = 0

for index,row in enumerate(reader):
	if x == 0:
		archivo.write(row[0]+","+row[1]+","+row[2]+","+row[3]+","+row[4]+","+row[5]+","+row[6]+","+row[7]+","+row[8]+","+row[9]+","+row[10]+","+row[11]+","+row[12]+","+row[13]+", cluster")
		archivo.write("\n")
	else:
		archivo.write(row[0]+","+row[1]+","+row[2]+","+row[3]+","+row[4]+","+row[5]+","+row[6]+","+row[7]+","+row[8]+","+row[9]+","+row[10]+","+row[11]+","+row[12]+","+row[13]+","+str(int(Z[x-1])))
		archivo.write("\n")
	x = x + 1

archivo.close()














