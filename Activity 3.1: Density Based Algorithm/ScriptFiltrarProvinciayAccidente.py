#!/usr/bin/env python
# -*- coding: utf-8 -*-


from xml.dom import minidom
import csv

doc = minidom.parse('../1-Data/inc2006.xml')
archivo=open ('../1-Data/incidentsarabaporaccidente.csv',"a")
archivo.write("tipo,autonomia,provincia,matricula,causa,poblacion,fechahora_ini,nivel,carretera,pk_inicial,pk_final,sentido,longitud,latitud")
archivo.write("\n")

# Incidents for ARABA and the type Accident

incidencias = doc.getElementsByTagName("incidenciaGeolocalizada")
for incidencia in incidencias:


	try:
		provincia = incidencia.getElementsByTagName("provincia")[0].firstChild.data.encode('utf-8')
	except:
		provincia = str(None)

	try:
		tipo = incidencia.getElementsByTagName("tipo")[0].firstChild.data.encode('utf-8')
	except:
		tipo = str(None)

	if(provincia == "ARABA" and tipo == "Accidente"):

		try:
			tipo = incidencia.getElementsByTagName("tipo")[0].firstChild.data.encode('utf-8')
		except:
			tipo = str(None)

		try:
			autonomia = incidencia.getElementsByTagName("autonomia")[0].firstChild.data.encode('utf-8')
		except:
			autonomia = str(None)

		try:
			provincia = incidencia.getElementsByTagName("provincia")[0].firstChild.data.encode('utf-8')
		except:
			provincia = str(None)

		try:
			matricula = incidencia.getElementsByTagName("matricula")[0].firstChild.data.encode('utf-8')
		except:
			matricula = str(None)

		try:
			causa = incidencia.getElementsByTagName("causa")[0].firstChild.data.encode('utf-8')
		except:
			causa = str(None)

		try:
			poblacion = incidencia.getElementsByTagName("poblacion")[0].firstChild.data.encode('utf-8')
		except:
			poblacion = str(None)

		try:
			fechahora_ini = incidencia.getElementsByTagName("fechahora_ini")[0].firstChild.data.encode('utf-8')
		except:
			fechahora_ini = str(None)

		try:
			nivel = incidencia.getElementsByTagName("nivel")[0].firstChild.data.encode('utf-8')
		except:
			nivel = str(None)

		try:
			carretera = incidencia.getElementsByTagName("carretera")[0].firstChild.data.encode('utf-8')
		except:
			carretera = str(None)

		try:
			pk_inicial = incidencia.getElementsByTagName("pk_inicial")[0].firstChild.data.encode('utf-8')
		except:
			pk_inicial = str(None)

		try:
			pk_final = incidencia.getElementsByTagName("pk_final")[0].firstChild.data.encode('utf-8')
		except:
			pk_final = str(None)

		try:
			sentido = incidencia.getElementsByTagName("sentido")[0].firstChild.data.encode('utf-8')
		except:
			sentido = str(None)

		try:
			longitud = incidencia.getElementsByTagName("longitud")[0].firstChild.data.encode('utf-8')
		except:
			longitud = str(None)

		try:
			latitud = incidencia.getElementsByTagName("latitud")[0].firstChild.data.encode('utf-8')
		except:
			latitud = str(None)


		archivo.write(tipo+","+autonomia+","+provincia+","+matricula+","+causa+","+poblacion+","+fechahora_ini+","+nivel+","+carretera+","+pk_inicial+","+pk_final+","+sentido+","+longitud+","+latitud)
		archivo.write("\n")


archivo.close()

