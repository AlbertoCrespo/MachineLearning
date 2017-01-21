# -*- coding: utf-8 -*-

#Authors: Alberto Crespo Sánchez and Juan Alfredo García García


import csv



def comprobar(cluster):
	reader = csv.reader(open('../1-Data/Works2007FeaturesC.csv', 'rb'))
	x = 0
	devolver = "No hay Obras"
	for index,row in enumerate(reader):
		if x == 0:
			x = x + 1
		else:
			if str(row[0]) == cluster:
				if str(row[2]) == "2":
					devolver = "Nivel Alto"
				if str(row[2]) == "0":
					devolver = "Nivel Medio"
				if str(row[2]) == "1":
					devolver = "Nivel Bajo"
	return devolver





reader = csv.reader(open('../1-Data/Caracteristicas.csv', 'rb'))
archivo=open ('../1-Data/DecisionTree.csv',"a")

x = 0


for index,row in enumerate(reader):
	if x == 0:
		archivo.write(row[0]+","+row[1]+","+row[2]+","+row[3]+","+row[4]+","+row[5]+","+row[6]+","+row[7]+","+row[8]+","+row[9]+","+row[10]+",Class")
		archivo.write("\n")
	else:
		d = comprobar(str(row[0]))
		archivo.write(row[0]+","+row[1]+","+row[2]+","+row[3]+","+row[4]+","+row[5]+","+row[6]+","+row[7]+","+row[8]+","+row[9]+","+row[10]+","+str(d))
		archivo.write("\n")
	x = x + 1

archivo.close()