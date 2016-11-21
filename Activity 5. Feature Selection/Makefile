all : borrar ejecutar

borrar:
	rm incidentsarabaporaccidenteC.csv
	rm BD.db
	rm Caracteristicas.csv

ejecutar: 
	python SacarLabels.py
	python ScriptBD.py 
	python Caracteristicas.py
	python PCA.py 
  