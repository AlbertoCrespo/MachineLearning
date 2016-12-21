all : borrar ejecutar

borrar:
	rm '../1-Data/incidentsarabaporaccidenteC.csv'
	rm '../1-Data/BD.db'
	rm '../1-Data/Caracteristicas.csv'

ejecutar: 
	python SacarLabels.py
	python ScriptBD.py 
	python Caracteristicas.py
	python PCA.py 
  