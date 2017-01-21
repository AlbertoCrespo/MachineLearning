# -*- coding: utf-8 -*-

#Authors: Alberto Crespo Sánchez and Juan Alfredo García García

import csv
import sqlite3


lista_de_cluster = []
Numero_accidentes_por_cluster = []



archivo=open ('../1-Data/Works2007Features.csv',"a")
archivo.write("Cluster,Numero de Obras por Cluster")
archivo.write("\n")


con = sqlite3.connect('../1-Data/BD1.db')
cursor = con.cursor()


#Numero de Clusters
cursor.execute("SELECT cluster FROM ACCIDENTES GROUP BY cluster")
for i in cursor:
	lista_de_cluster.append(str(i[0]))


#Numero de Accidentes por Cluster
cursor.execute("SELECT COUNT(cluster) FROM ACCIDENTES GROUP BY cluster")
for i in cursor:
	Numero_accidentes_por_cluster.append(str(i[0]))




cursor.close()
con.close()


x = 0
for i in lista_de_cluster:
	archivo.write(str(i)+","+str(Numero_accidentes_por_cluster[x]))
	archivo.write("\n")
	x = x + 1

archivo.close()
