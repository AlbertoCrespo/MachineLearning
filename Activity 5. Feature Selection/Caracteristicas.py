# -*- coding: utf-8 -*-

#Authors: Alberto Crespo Sánchez and Juan Alfredo García García

import csv
import sqlite3

def iniciar(lista):
	for i in range(0, 124):
		lista.append(str(0))
	return lista


lista_de_cluster = []
Numero_accidentes_por_cluster = []
Numero_de_accidentes_por_Salida = []
Numero_de_accidentes_por_Salida = iniciar(Numero_de_accidentes_por_Salida)
Numero_de_accidentes_por_Alcance = []
Numero_de_accidentes_por_Alcance = iniciar(Numero_de_accidentes_por_Alcance)
Numero_de_accidentes_por_Vuelco = []
Numero_de_accidentes_por_Vuelco = iniciar(Numero_de_accidentes_por_Vuelco)
Numero_de_accidentes_por_Tijera = []
Numero_de_accidentes_por_Tijera = iniciar(Numero_de_accidentes_por_Tijera)
Numero_de_accidentes_por_Atropello= []
Numero_de_accidentes_por_Atropello = iniciar(Numero_de_accidentes_por_Atropello)



archivo=open ("Carectiristicas.csv","a")
archivo.write("Cluster,Numero de Accidentes por Cluster,Numero de accidentes por salida, numero de accidentes por Alcance, Numero de accidentes por Vuelco, Numero de accidentes por tijera, numero de accidentes por atropello")
archivo.write("\n")


con = sqlite3.connect('BD.db')
cursor = con.cursor()


#Numero de Clusters
cursor.execute("SELECT cluster FROM ACCIDENTES GROUP BY cluster")
for i in cursor:
	lista_de_cluster.append(str(i[0]))


#Numero de Accidentes por Cluster
cursor.execute("SELECT COUNT(cluster) FROM ACCIDENTES GROUP BY cluster")
for i in cursor:
	Numero_accidentes_por_cluster.append(str(i[0]))


#Distitntos tipos de acccidentes por Salida
cursor.execute("SELECT cluster,count(causa) FROM ACCIDENTES where causa='Salida' GROUP BY cluster")
for i in cursor:
	Numero_de_accidentes_por_Salida[int(i[0]+1)] = str(i[1])

#Distitntos tipos de acccidentes por Alcance
cursor.execute("SELECT cluster,count(causa) FROM ACCIDENTES where causa='Alcance' GROUP BY cluster")
for i in cursor:
	Numero_de_accidentes_por_Alcance[int(i[0]+1)] = str(i[1])

#Distitntos tipos de acccidentes por Vuelco
cursor.execute("SELECT cluster,count(causa) FROM ACCIDENTES where causa='Vuelco' GROUP BY cluster")
for i in cursor:
	Numero_de_accidentes_por_Vuelco[int(i[0]+1)] = str(i[1])

#Distitntos tipos de acccidentes por Tijera
cursor.execute("SELECT cluster,count(causa) FROM ACCIDENTES where causa='Tijera camión' GROUP BY cluster")
for i in cursor:
	Numero_de_accidentes_por_Tijera[int(i[0]+1)] = str(i[1])

#Distitntos tipos de acccidentes por Atropello
cursor.execute("SELECT cluster,count(causa) FROM ACCIDENTES where causa='Atropello' GROUP BY cluster")
for i in cursor:
	Numero_de_accidentes_por_Atropello[int(i[0]+1)] = str(i[1])


cursor.close()
con.close()


x = 0
for i in lista_de_cluster:
	archivo.write(str(i)+","+str(Numero_accidentes_por_cluster[x])+","+str(Numero_de_accidentes_por_Salida[x])+","+str(Numero_de_accidentes_por_Alcance[x])+","+str(Numero_de_accidentes_por_Vuelco[x])+","+str(Numero_de_accidentes_por_Tijera[x])+","+str(Numero_de_accidentes_por_Atropello[x]))
	archivo.write("\n")
	x = x + 1

archivo.close()
