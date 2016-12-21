import sqlite3
import os
import csv

#CREAMOS LA BD

con = sqlite3.connect('../1-Data/BD.db')

cursor = con.cursor()

print("La base de datos se creo correctamente")

#CREAMOS LAS TABLAS

cursor.execute(''' CREATE TABLE ACCIDENTES (
  id         		integer NOT NULL PRIMARY KEY,
  tipo       		varchar(50),
  autonomia  		varchar(50),
  provincia			varchar(50),
  matricula  		varchar(50),
  causa  			varchar(50),
  poblacion  		varchar(50),
  fechahora_ini  	varchar(50),
  nivel  			varchar(50),
  carretera  		varchar(50),
  pk_inicial  	    integer,
  pk_final  	    integer,
  sentido  			varchar(50),
  longitud			real,
  latitud			real,
  cluster			integer
);''')


cursor.close()
con.close()

con = sqlite3.connect('../1-Data/BD.db')
cursor = con.cursor()

reader = csv.reader(open('../1-Data/incidentsarabaporaccidenteC.csv', 'rb'))
x = 0
y = 1
for index,row in enumerate(reader):
	if x > 0:
		id = str(y)
		tipo = str(row[0])
		autonomia = str(row[1])
		provincia = str(row[2])
		matricula = str(row[3])
		causa = str(row[4])
		poblacion = str(row[5])
		fechahora_ini = str(row[6])
		nivel = str(row[7])
		carretera = str(row[8])
		pk_inicial = str(row[9])
		pk_final = str(row[10])
		sentido = str(row[11])
		longitud = str(row[12])
		latitud = str(row[13])
		cluster = str(row[14])
		y = y +1
		cursor.execute("INSERT INTO ACCIDENTES (id, tipo, autonomia, provincia, matricula, causa, poblacion, fechahora_ini, nivel, carretera, pk_inicial, pk_final, sentido, longitud, latitud, cluster) VALUES ("+id+",'"+tipo+"','"+autonomia+"', '"+provincia+"', '"+matricula+"','"+causa+"','"+poblacion+"','"+fechahora_ini+"','"+nivel+"','"+carretera+"',"+pk_inicial+","+pk_final+",'"+sentido+"',"+longitud+","+latitud+","+cluster+");")
	x = x + 1

con.commit()
cursor.close()
con.close()